# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(920, 467)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(10, 0, 900, 41))
        self.horizontalLayoutWidget.setObjectName(_fromUtf8("horizontalLayoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButton_8 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        self.horizontalLayout.addWidget(self.pushButton_8)
        self.pushButton_7 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.horizontalLayout.addWidget(self.pushButton_7)
        self.pushButton_6 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.horizontalLayout.addWidget(self.pushButton_6)
        self.pushButton_5 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.horizontalLayout.addWidget(self.pushButton_5)
        self.pushButton_4 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.pushButton_3 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.horizontalLayout.addWidget(self.pushButton_3)
	self.pushButton_2 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.horizontalLayout.addWidget(self.pushButton_2)
	self.pushButton_9 = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton_9.setObjectName(_fromUtf8("pushButton_9"))
        self.horizontalLayout.addWidget(self.pushButton_9)
	self.pushButton = QtGui.QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayoutWidget = QtGui.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 40, 900, 401))
        self.verticalLayoutWidget.setObjectName(_fromUtf8("verticalLayoutWidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.line = QtGui.QFrame(self.verticalLayoutWidget)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.listWidget = QtGui.QListWidget(self.verticalLayoutWidget)
        self.listWidget.setObjectName(_fromUtf8("listWidget"))
        self.verticalLayout.addWidget(self.listWidget)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.verticalLayoutWidget)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.verticalLayout.addWidget(self.plainTextEdit)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "KVM MANAGER", None))
        self.pushButton_8.setText(_translate("MainWindow", "Conectar", None))
        self.pushButton_7.setText(_translate("MainWindow", "Nueva VM", None))
        self.pushButton_6.setText(_translate("MainWindow", "Apagar VM", None))
        self.pushButton_5.setText(_translate("MainWindow", "Iniciar VM", None))
        self.pushButton_4.setText(_translate("MainWindow", "Pausar VM", None))
        self.pushButton_3.setText(_translate("MainWindow", "Reanudar VM", None))
	self.pushButton_2.setText(_translate("MainWindow", "Reiniciar VM", None))
	self.pushButton_9.setText(_translate("MainWindow", "Borrar VM", None))
	self.pushButton.setText(_translate("MainWindow", "Mostrar VM", None))

