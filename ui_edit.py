# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Edit(object):
    def setupUi(self, Edit):
        Edit.setObjectName("Edit")
        Edit.resize(619, 324)
        self.gridLayout = QtWidgets.QGridLayout(Edit)
        self.gridLayout.setObjectName("gridLayout")
        self.parentTreeWidget = QtWidgets.QTreeWidget(Edit)
        self.parentTreeWidget.setHeaderHidden(True)
        self.parentTreeWidget.setObjectName("parentTreeWidget")
        self.parentTreeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.parentTreeWidget, 2, 1, 1, 2)
        self.saveButton = QtWidgets.QPushButton(Edit)
        self.saveButton.setObjectName("saveButton")
        self.gridLayout.addWidget(self.saveButton, 3, 1, 1, 1)
        self.label1 = QtWidgets.QLabel(Edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label1.sizePolicy().hasHeightForWidth())
        self.label1.setSizePolicy(sizePolicy)
        self.label1.setObjectName("label1")
        self.gridLayout.addWidget(self.label1, 1, 1, 1, 1)
        self.cancelButton = QtWidgets.QPushButton(Edit)
        self.cancelButton.setObjectName("cancelButton")
        self.gridLayout.addWidget(self.cancelButton, 3, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(Edit)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.parentLabel = QtWidgets.QLabel(Edit)
        self.parentLabel.setText("")
        self.parentLabel.setObjectName("parentLabel")
        self.gridLayout.addWidget(self.parentLabel, 1, 2, 1, 1)
        self.nameEdit = QtWidgets.QLineEdit(Edit)
        self.nameEdit.setObjectName("nameEdit")
        self.gridLayout.addWidget(self.nameEdit, 0, 2, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(Edit)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.delButton = QtWidgets.QPushButton(Edit)
        self.delButton.setObjectName("delButton")
        self.horizontalLayout.addWidget(self.delButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.selectTreeWidget = QtWidgets.QTreeWidget(Edit)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.selectTreeWidget.sizePolicy().hasHeightForWidth())
        self.selectTreeWidget.setSizePolicy(sizePolicy)
        self.selectTreeWidget.setHeaderHidden(True)
        self.selectTreeWidget.setObjectName("selectTreeWidget")
        self.selectTreeWidget.headerItem().setText(0, "1")
        self.selectTreeWidget.header().setVisible(False)
        self.gridLayout.addWidget(self.selectTreeWidget, 1, 0, 3, 1)

        self.retranslateUi(Edit)
        QtCore.QMetaObject.connectSlotsByName(Edit)

    def retranslateUi(self, Edit):
        _translate = QtCore.QCoreApplication.translate
        Edit.setWindowTitle(_translate("Edit", "Form"))
        self.saveButton.setText(_translate("Edit", "Enregistrer"))
        self.label1.setText(_translate("Edit", "Parent : "))
        self.cancelButton.setText(_translate("Edit", "Annuler"))
        self.label_2.setText(_translate("Edit", "Nom :"))
        self.addButton.setText(_translate("Edit", "Ajouter"))
        self.delButton.setText(_translate("Edit", "Supprimer"))

