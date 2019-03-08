# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'questions.ui'
#
# Created by: PyQt5 UI code generator 5.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Questions(object):
    def setupUi(self, Questions):
        Questions.setObjectName("Questions")
        Questions.resize(625, 296)
        self.gridLayout = QtWidgets.QGridLayout(Questions)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget = QtWidgets.QListWidget(Questions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout.addWidget(self.listWidget, 0, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Questions)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_question = QtWidgets.QLabel(Questions)
        self.label_question.setText("")
        self.label_question.setObjectName("label_question")
        self.horizontalLayout.addWidget(self.label_question)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.yesButton = QtWidgets.QPushButton(Questions)
        self.yesButton.setObjectName("yesButton")
        self.horizontalLayout_2.addWidget(self.yesButton)
        self.mayButton = QtWidgets.QPushButton(Questions)
        self.mayButton.setObjectName("mayButton")
        self.horizontalLayout_2.addWidget(self.mayButton)
        self.noButton = QtWidgets.QPushButton(Questions)
        self.noButton.setObjectName("noButton")
        self.horizontalLayout_2.addWidget(self.noButton)
        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(Questions)
        self.treeWidget.setHeaderHidden(True)
        self.treeWidget.setObjectName("treeWidget")
        self.treeWidget.headerItem().setText(0, "1")
        self.gridLayout.addWidget(self.treeWidget, 0, 1, 3, 1)

        self.retranslateUi(Questions)
        QtCore.QMetaObject.connectSlotsByName(Questions)

    def retranslateUi(self, Questions):
        _translate = QtCore.QCoreApplication.translate
        Questions.setWindowTitle(_translate("Questions", "Form"))
        self.label.setText(_translate("Questions", "Question :"))
        self.yesButton.setText(_translate("Questions", "Oui"))
        self.mayButton.setText(_translate("Questions", "Ignorer"))
        self.noButton.setText(_translate("Questions", "Non"))

