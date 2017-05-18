# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'crearmaquinas.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        Dialog1.setObjectName(_fromUtf8("Dialog1"))
        Dialog1.resize(1002, 773)
        self.label = QtGui.QLabel(Dialog1)
        self.label.setGeometry(QtCore.QRect(50, 140, 181, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Dialog1)
        self.label_2.setGeometry(QtCore.QRect(50, 190, 181, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Dialog1)
        self.label_3.setGeometry(QtCore.QRect(50, 240, 181, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(Dialog1)
        self.label_4.setGeometry(QtCore.QRect(50, 290, 181, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(Dialog1)
        self.label_5.setGeometry(QtCore.QRect(50, 340, 181, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(Dialog1)
        self.label_6.setGeometry(QtCore.QRect(50, 390, 181, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.label_7 = QtGui.QLabel(Dialog1)
        self.label_7.setGeometry(QtCore.QRect(50, 440, 181, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(Dialog1)
        self.label_8.setGeometry(QtCore.QRect(50, 490, 181, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(Dialog1)
        self.label_9.setGeometry(QtCore.QRect(50, 540, 181, 21))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(Dialog1)
        self.label_10.setGeometry(QtCore.QRect(50, 590, 181, 21))
        self.label_10.setObjectName(_fromUtf8("label_10"))

        self.lineEdit = QtGui.QLineEdit(Dialog1)
        self.lineEdit.setGeometry(QtCore.QRect(240, 140, 491, 27))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.lineEdit_2 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_2.setGeometry(QtCore.QRect(240, 190, 491, 27))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.lineEdit_3 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_3.setGeometry(QtCore.QRect(240, 240, 491, 27))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.lineEdit_4 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_4.setGeometry(QtCore.QRect(240, 290, 491, 27))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.lineEdit_5 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_5.setGeometry(QtCore.QRect(240, 340, 491, 27))
        self.lineEdit_5.setObjectName(_fromUtf8("lineEdit_5"))
        self.lineEdit_6 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_6.setGeometry(QtCore.QRect(240, 390, 491, 27))
        self.lineEdit_6.setObjectName(_fromUtf8("lineEdit_6"))
        self.lineEdit_7 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_7.setGeometry(QtCore.QRect(240, 440, 491, 27))
        self.lineEdit_7.setObjectName(_fromUtf8("lineEdit_7"))
        self.lineEdit_8 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_8.setGeometry(QtCore.QRect(240, 490, 491, 27))
        self.lineEdit_8.setObjectName(_fromUtf8("lineEdit_8"))
        self.lineEdit_9 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_9.setGeometry(QtCore.QRect(240, 540, 491, 27))
        self.lineEdit_9.setObjectName(_fromUtf8("lineEdit_9"))
        self.lineEdit_10 = QtGui.QLineEdit(Dialog1)
        self.lineEdit_10.setGeometry(QtCore.QRect(240, 590, 491, 27))
        self.lineEdit_10.setObjectName(_fromUtf8("lineEdit_10"))


        self.pushButton = QtGui.QPushButton(Dialog1)
        self.pushButton.setGeometry(QtCore.QRect(570, 670, 181, 31))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(Dialog1)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 670, 181, 31))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))

        self.retranslateUi(Dialog1)
        QtCore.QMetaObject.connectSlotsByName(Dialog1)

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(_translate("Dialog1", "KVM Creacion de maquinas", None))
        self.label.setText(_translate("Dialog1", "Name", None))
        self.label_2.setText(_translate("Dialog1", "Description", None))
        self.label_3.setText(_translate("Dialog1", "os-type", None))
        self.label_4.setText(_translate("Dialog1", "os-variant", None))
        self.label_5.setText(_translate("Dialog1", "RAM", None))
        self.label_6.setText(_translate("Dialog1", "vcpus", None))
        self.label_7.setText(_translate("Dialog1", "disk path", None))
        self.label_8.setText(_translate("Dialog1", "graphics", None))
        self.label_9.setText(_translate("Dialog1", "cdrom", None))
        self.label_10.setText(_translate("Dialog1", "network", None))
        self.pushButton.setText(_translate("Dialog1", "Finalizar", None))
        self.pushButton_2.setText(_translate("Dialog1", "Atras", None))

