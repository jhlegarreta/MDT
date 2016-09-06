# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MapSpecificOptions.ui'
#
# Created by: PyQt5 UI code generator 5.4.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MapSpecificOptions(object):
    def setupUi(self, MapSpecificOptions):
        MapSpecificOptions.setObjectName("MapSpecificOptions")
        MapSpecificOptions.resize(648, 564)
        self.gridLayout = QtWidgets.QGridLayout(MapSpecificOptions)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(8)
        self.gridLayout.setObjectName("gridLayout")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 2, 0, 1, 1)
        self.frame = CollapsablePanel(MapSpecificOptions)
        self.frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_18 = CollapsablePanelHeader(self.frame)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_18.setFont(font)
        self.label_18.setObjectName("label_18")
        self.verticalLayout_5.addWidget(self.label_18)
        self.line_3 = QtWidgets.QFrame(self.frame)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout_5.addWidget(self.line_3)
        self.frame_4 = CollapsablePanelContent(self.frame)
        self.frame_4.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame_4)
        self.gridLayout_3.setContentsMargins(6, 6, 0, 0)
        self.gridLayout_3.setHorizontalSpacing(6)
        self.gridLayout_3.setVerticalSpacing(3)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_23 = QtWidgets.QLabel(self.frame_4)
        self.label_23.setObjectName("label_23")
        self.gridLayout_3.addWidget(self.label_23, 2, 0, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(-1, 4, -1, 4)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.data_scale_max = ScientificDoubleSpinBox(self.frame_4)
        self.data_scale_max.setMinimum(-9999999999.99)
        self.data_scale_max.setMaximum(9999999999.99)
        self.data_scale_max.setObjectName("data_scale_max")
        self.verticalLayout.addWidget(self.data_scale_max)
        self.data_scale_min = ScientificDoubleSpinBox(self.frame_4)
        self.data_scale_min.setSpecialValueText("")
        self.data_scale_min.setMinimum(-9999999999.99)
        self.data_scale_min.setMaximum(9999999999.99)
        self.data_scale_min.setObjectName("data_scale_min")
        self.verticalLayout.addWidget(self.data_scale_min)
        self.data_set_use_scale = QtWidgets.QCheckBox(self.frame_4)
        self.data_set_use_scale.setObjectName("data_set_use_scale")
        self.verticalLayout.addWidget(self.data_set_use_scale)
        self.gridLayout_3.addLayout(self.verticalLayout, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.frame_4)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 3, 0, 1, 1)
        self.colormap = QtWidgets.QComboBox(self.frame_4)
        self.colormap.setObjectName("colormap")
        self.gridLayout_3.addWidget(self.colormap, 3, 1, 1, 1)
        self.map_title = QtWidgets.QLineEdit(self.frame_4)
        self.map_title.setObjectName("map_title")
        self.gridLayout_3.addWidget(self.map_title, 0, 1, 1, 1)
        self.label_21 = QtWidgets.QLabel(self.frame_4)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 0, 0, 1, 1)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, -1, -1, 4)
        self.verticalLayout_2.setSpacing(2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.data_clipping_max = ScientificDoubleSpinBox(self.frame_4)
        self.data_clipping_max.setMinimum(-9999999999.99)
        self.data_clipping_max.setMaximum(9999999999.99)
        self.data_clipping_max.setObjectName("data_clipping_max")
        self.verticalLayout_2.addWidget(self.data_clipping_max)
        self.data_clipping_min = ScientificDoubleSpinBox(self.frame_4)
        self.data_clipping_min.setMinimum(-9999999999.99)
        self.data_clipping_min.setMaximum(9999999999.99)
        self.data_clipping_min.setObjectName("data_clipping_min")
        self.verticalLayout_2.addWidget(self.data_clipping_min)
        self.data_set_use_clipping = QtWidgets.QCheckBox(self.frame_4)
        self.data_set_use_clipping.setObjectName("data_set_use_clipping")
        self.verticalLayout_2.addWidget(self.data_set_use_clipping)
        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 1, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.frame_4)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 1, 0, 1, 1)
        self.verticalLayout_5.addWidget(self.frame_4)
        self.gridLayout.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_2 = CollapsablePanel(MapSpecificOptions)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_20 = CollapsablePanelHeader(self.frame_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName("label_20")
        self.verticalLayout_6.addWidget(self.label_20)
        self.line_4 = QtWidgets.QFrame(self.frame_2)
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.verticalLayout_6.addWidget(self.line_4)
        self.frame_5 = CollapsablePanelContent(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.frame_5)
        self.gridLayout_4.setContentsMargins(6, 6, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(6)
        self.gridLayout_4.setVerticalSpacing(3)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_26 = QtWidgets.QLabel(self.frame_5)
        self.label_26.setObjectName("label_26")
        self.gridLayout_4.addWidget(self.label_26, 3, 0, 1, 1)
        self.info_file_location = QtWidgets.QLabel(self.frame_5)
        self.info_file_location.setWordWrap(True)
        self.info_file_location.setObjectName("info_file_location")
        self.gridLayout_4.addWidget(self.info_file_location, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.frame_5)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 2, 0, 1, 1)
        self.label_24 = QtWidgets.QLabel(self.frame_5)
        self.label_24.setObjectName("label_24")
        self.gridLayout_4.addWidget(self.label_24, 0, 0, 1, 1)
        self.info_maximum = QtWidgets.QLabel(self.frame_5)
        self.info_maximum.setObjectName("info_maximum")
        self.gridLayout_4.addWidget(self.info_maximum, 2, 1, 1, 1)
        self.info_minimum = QtWidgets.QLabel(self.frame_5)
        self.info_minimum.setObjectName("info_minimum")
        self.gridLayout_4.addWidget(self.info_minimum, 3, 1, 1, 1)
        self.gridLayout_4.setColumnStretch(1, 1)
        self.verticalLayout_6.addWidget(self.frame_5)
        self.gridLayout.addWidget(self.frame_2, 1, 0, 1, 1)

        self.retranslateUi(MapSpecificOptions)
        QtCore.QMetaObject.connectSlotsByName(MapSpecificOptions)
        MapSpecificOptions.setTabOrder(self.map_title, self.data_scale_max)
        MapSpecificOptions.setTabOrder(self.data_scale_max, self.data_scale_min)
        MapSpecificOptions.setTabOrder(self.data_scale_min, self.data_set_use_scale)
        MapSpecificOptions.setTabOrder(self.data_set_use_scale, self.data_clipping_max)
        MapSpecificOptions.setTabOrder(self.data_clipping_max, self.data_clipping_min)
        MapSpecificOptions.setTabOrder(self.data_clipping_min, self.data_set_use_clipping)
        MapSpecificOptions.setTabOrder(self.data_set_use_clipping, self.colormap)

    def retranslateUi(self, MapSpecificOptions):
        _translate = QtCore.QCoreApplication.translate
        MapSpecificOptions.setWindowTitle(_translate("MapSpecificOptions", "Form"))
        self.label_18.setText(_translate("MapSpecificOptions", "General"))
        self.label_23.setText(_translate("MapSpecificOptions", "Clipping:"))
        self.data_set_use_scale.setText(_translate("MapSpecificOptions", "Use scaling"))
        self.label_9.setText(_translate("MapSpecificOptions", "Colormap:"))
        self.label_21.setText(_translate("MapSpecificOptions", "Title:"))
        self.data_set_use_clipping.setText(_translate("MapSpecificOptions", "Use clipping"))
        self.label_10.setText(_translate("MapSpecificOptions", "Scale:"))
        self.label_20.setText(_translate("MapSpecificOptions", "Info"))
        self.label_26.setText(_translate("MapSpecificOptions", "Minimum:"))
        self.info_file_location.setText(_translate("MapSpecificOptions", "TextLabel"))
        self.label_11.setText(_translate("MapSpecificOptions", "Maximum:"))
        self.label_24.setText(_translate("MapSpecificOptions", "Filename:"))
        self.info_maximum.setText(_translate("MapSpecificOptions", "TextLabel"))
        self.info_minimum.setText(_translate("MapSpecificOptions", "TextLabel"))

from ..widgets import CollapsablePanel, CollapsablePanelContent, CollapsablePanelHeader, ScientificDoubleSpinBox
