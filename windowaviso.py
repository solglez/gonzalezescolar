# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'windowaviso.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_windowaviso(object):
    def setupUi(self, windowaviso):
        windowaviso.setObjectName("windowaviso")
        windowaviso.resize(389, 229)
        windowaviso.setModal(True)
        self.btnBoxAviso = QtWidgets.QDialogButtonBox(windowaviso)
        self.btnBoxAviso.setGeometry(QtCore.QRect(110, 160, 161, 61))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(7)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnBoxAviso.sizePolicy().hasHeightForWidth())
        self.btnBoxAviso.setSizePolicy(sizePolicy)
        self.btnBoxAviso.setMinimumSize(QtCore.QSize(0, 0))
        self.btnBoxAviso.setSizeIncrement(QtCore.QSize(1, 0))
        self.btnBoxAviso.setBaseSize(QtCore.QSize(2, 0))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.btnBoxAviso.setFont(font)
        self.btnBoxAviso.setAutoFillBackground(False)
        self.btnBoxAviso.setStandardButtons(QtWidgets.QDialogButtonBox.No|QtWidgets.QDialogButtonBox.Yes)
        self.btnBoxAviso.setObjectName("btnBoxAviso")
        self.lblAviso = QtWidgets.QLabel(windowaviso)
        self.lblAviso.setGeometry(QtCore.QRect(120, 110, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.lblAviso.setFont(font)
        self.lblAviso.setObjectName("lblAviso")
        self.lblImageAviso = QtWidgets.QLabel(windowaviso)
        self.lblImageAviso.setGeometry(QtCore.QRect(150, 20, 91, 81))
        self.lblImageAviso.setText("")
        self.lblImageAviso.setPixmap(QtGui.QPixmap("img/warning.png"))
        self.lblImageAviso.setScaledContents(True)
        self.lblImageAviso.setObjectName("lblImageAviso")

        self.retranslateUi(windowaviso)
        self.btnBoxAviso.accepted.connect(windowaviso.accept)
        self.btnBoxAviso.rejected.connect(windowaviso.reject)
        QtCore.QMetaObject.connectSlotsByName(windowaviso)

    def retranslateUi(self, windowaviso):
        _translate = QtCore.QCoreApplication.translate
        windowaviso.setWindowTitle(_translate("windowaviso", "Aviso"))
        self.lblAviso.setText(_translate("windowaviso", "Desea salir?"))
