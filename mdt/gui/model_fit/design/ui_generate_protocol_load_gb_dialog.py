# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'generate_protocol_load_gb_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_LoadGBDialog:
    def setupUi(self, LoadGBDialog):
        LoadGBDialog.setObjectName("LoadGBDialog")
        LoadGBDialog.resize(831, 227)
        self.verticalLayout = QtWidgets.QVBoxLayout(LoadGBDialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_3 = QtWidgets.QLabel(LoadGBDialog)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_3.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(LoadGBDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_3.addWidget(self.label_4)
        self.verticalLayout.addLayout(self.verticalLayout_3)
        self.line = QtWidgets.QFrame(LoadGBDialog)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.bvalFileChooser = QtWidgets.QPushButton(LoadGBDialog)
        self.bvalFileChooser.setEnabled(True)
        self.bvalFileChooser.setObjectName("bvalFileChooser")
        self.horizontalLayout.addWidget(self.bvalFileChooser)
        self.bvalFileInput = QtWidgets.QLineEdit(LoadGBDialog)
        self.bvalFileInput.setEnabled(True)
        self.bvalFileInput.setObjectName("bvalFileInput")
        self.horizontalLayout.addWidget(self.bvalFileInput)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(LoadGBDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(LoadGBDialog)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(LoadGBDialog)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)
        self.label_12 = QtWidgets.QLabel(LoadGBDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 1, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.bvecFileChooser = QtWidgets.QPushButton(LoadGBDialog)
        self.bvecFileChooser.setObjectName("bvecFileChooser")
        self.horizontalLayout_2.addWidget(self.bvecFileChooser)
        self.bvecFileInput = QtWidgets.QLineEdit(LoadGBDialog)
        self.bvecFileInput.setObjectName("bvecFileInput")
        self.horizontalLayout_2.addWidget(self.bvecFileInput)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(LoadGBDialog)
        font = QtGui.QFont()
        font.setItalic(True)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 2, 1, 1)
        self.bvalScale = QtWidgets.QLineEdit(LoadGBDialog)
        self.bvalScale.setObjectName("bvalScale")
        self.gridLayout.addWidget(self.bvalScale, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(LoadGBDialog)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.line_3 = QtWidgets.QFrame(LoadGBDialog)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.buttonBox = QtWidgets.QDialogButtonBox(LoadGBDialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(LoadGBDialog)
        self.buttonBox.accepted.connect(LoadGBDialog.accept)
        self.buttonBox.rejected.connect(LoadGBDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(LoadGBDialog)
        LoadGBDialog.setTabOrder(self.bvalFileChooser, self.bvalFileInput)

    def retranslateUi(self, LoadGBDialog):
        _translate = QtCore.QCoreApplication.translate
        LoadGBDialog.setWindowTitle(_translate("LoadGBDialog", "Load g & b"))
        self.label_3.setText(_translate("LoadGBDialog", "Load g & b"))
        self.label_4.setText(_translate("LoadGBDialog", "Load the bvec (g) and bval (b) in the protocol"))
        self.bvalFileChooser.setText(_translate("LoadGBDialog", "Browse"))
        self.label_11.setText(_translate("LoadGBDialog", "(The file containing the gradient directions)"))
        self.label_5.setText(_translate("LoadGBDialog", "Bvec (g) file:"))
        self.label_6.setText(_translate("LoadGBDialog", "Bval (b) file:"))
        self.label_12.setText(_translate("LoadGBDialog", "(The file containing the b-values)"))
        self.bvecFileChooser.setText(_translate("LoadGBDialog", "Browse"))
        self.label_13.setText(_translate("LoadGBDialog", "(We expect the b-values in the\n"
"protocol in units of s/m^2)"))
        self.bvalScale.setText(_translate("LoadGBDialog", "1e6"))
        self.label_7.setText(_translate("LoadGBDialog", "B-value rescale:"))

