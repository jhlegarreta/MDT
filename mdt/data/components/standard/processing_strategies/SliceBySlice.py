import os
import numpy as np
import shutil
from mdt.IO import Nifti
from mdt.utils import ModelChunksProcessingStrategy

__author__ = 'Robbert Harms'
__date__ = "2015-11-29"
__maintainer__ = "Robbert Harms"
__email__ = "robbert.harms@maastrichtuniversity.nl"


meta_info = {'title': 'Slice by slice fitting',
             'description': 'Processes a model slice by slice, saving the intermediate results.'}


class SliceBySlice(ModelChunksProcessingStrategy):

    def __init__(self, slice_dimension=2, slice_width=1):
        """Optimize a given dataset slice by slice.

        Args:
            slice_dimension: in which dimension to slice the dataset
            slice_width: the width of the slices in that dimension

        Attributes:
            slice_dimension: in which dimension to slice the dataset
            slice_width: the width of the slices in that dimension
        """
        super(SliceBySlice, self).__init__()
        self.slice_dimension = slice_dimension
        self.slice_width = slice_width

    def run(self, model, problem_data, output_path, recalculate, worker):
        mask = problem_data.mask
        chunk_mask = np.zeros_like(mask)
        indices = self._get_index_matrix(problem_data.mask)
        slices_dir = os.path.join(output_path, 'slices')

        self._prepare_chunk_dir(slices_dir, recalculate)

        for ind_start, ind_end, slicer in self._slicing_generator(mask):
            chunk_mask.fill(0)
            chunk_mask[slicer] = mask[slicer]

            chunk_indices = indices[slicer].flatten()[list(np.nonzero(mask[slicer].flatten()))[0]]

            if chunk_mask.any():
                with self._selected_indices(model, chunk_indices):
                    self._run_on_slice(model, problem_data, slices_dir, recalculate, worker,
                                       ind_start, ind_end, chunk_mask)

        self._logger.info('Computed all slices, now merging the results')
        return_data = worker.combine(output_path, slices_dir)
        shutil.rmtree(slices_dir)
        return return_data

    def _slicing_generator(self, mask):
        """Generate the slices/chunks we will use for the fitting.

        Args:
            mask (ndarray): the mask for all the slices

        Returns:
            tuple (int, int, list): the start of the slice index, the end of the slice index and the list with
                the slices to select from the mask.
        """
        slicer = [slice(None)] * len(mask.shape)
        dimension_length = mask.shape[self.slice_dimension]

        for ind_start in range(0, dimension_length, self.slice_width):
            ind_end = min(dimension_length, ind_start + self.slice_width)
            slicer[self.slice_dimension] = slice(ind_start, ind_end)

            yield ind_start, ind_end, slicer

    def _run_on_slice(self, model, problem_data, slices_dir, recalculate, worker, ind_start, ind_end, tmp_mask):
        slice_dir = os.path.join(slices_dir, '{dimension}_{start}_{end}'.format(
            dimension=self.slice_dimension, start=ind_start, end=ind_end))

        if recalculate and os.path.exists(slice_dir):
            shutil.rmtree(slice_dir)

        if worker.output_exists(model, problem_data, slice_dir):
            self._logger.info('Skipping slices {} to {}, they are already processed.'.format(ind_start, ind_end))
        else:
            self._logger.info('Computing slices {0} up to {1} ({2} slices in total, we are at {3:.2%})'.format(
                ind_start, ind_end, tmp_mask.shape[self.slice_dimension],
                float(ind_start) / tmp_mask.shape[self.slice_dimension]))

            worker.process(model, problem_data, tmp_mask, slice_dir)
            Nifti.write_volume_maps({'__mask': tmp_mask}, slice_dir, problem_data.volume_header)