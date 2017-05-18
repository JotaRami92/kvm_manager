# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
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
        MainWindow.setObjectName(_fromUtf8("KVM virtual machine manager"))
        MainWindow.resize(1100, 821)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.pushButton = QtGui.QPushButton(self.centralWidget)
        self.pushButton.setGeometry(QtCore.QRect(858, 56, 221, 51))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.pushButton_2 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_2.setGeometry(QtCore.QRect(860, 210, 211, 51))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.pushButton_3 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_3.setGeometry(QtCore.QRect(860, 360, 211, 51))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.checkBox = QtGui.QCheckBox(self.centralWidget)
        self.checkBox.setGeometry(QtCore.QRect(890, 280, 191, 22))
        self.checkBox.setObjectName(_fromUtf8("checkBox"))
        self.checkBox_2 = QtGui.QCheckBox(self.centralWidget)
        self.checkBox_2.setGeometry(QtCore.QRect(890, 320, 201, 22))
        self.checkBox_2.setObjectName(_fromUtf8("checkBox_2"))
        self.pushButton_4 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_4.setGeometry(QtCore.QRect(860, 510, 211, 51))
        self.pushButton_4.setObjectName(_fromUtf8("pushButton_4"))
        self.pushButton_5 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_5.setGeometry(QtCore.QRect(860, 130, 211, 51))
        self.pushButton_5.setObjectName(_fromUtf8("pushButton_5"))
        self.pushButton_6 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_6.setGeometry(QtCore.QRect(860, 670, 211, 51))
        self.pushButton_6.setObjectName(_fromUtf8("pushButton_6"))
        self.listView = QtGui.QListView(self.centralWidget)
        self.listView.setGeometry(QtCore.QRect(60, 70, 711, 611))
        self.listView.setObjectName(_fromUtf8("listView"))
        self.pushButton_7 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_7.setGeometry(QtCore.QRect(860, 430, 211, 51))
        self.pushButton_7.setObjectName(_fromUtf8("pushButton_7"))
        self.pushButton_8 = QtGui.QPushButton(self.centralWidget)
        self.pushButton_8.setGeometry(QtCore.QRect(860, 590, 211, 51))
        self.pushButton_8.setObjectName(_fromUtf8("pushButton_8"))
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtGui.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 1100, 25))
        self.menuBar.setObjectName(_fromUtf8("menuBar"))
        self.menuInicio = QtGui.QMenu(self.menuBar)
        self.menuInicio.setObjectName(_fromUtf8("menuInicio"))
        self.menuConfiguracion_de_M_quinas = QtGui.QMenu(self.menuBar)
        self.menuConfiguracion_de_M_quinas.setObjectName(_fromUtf8("menuConfiguracion_de_M_quinas"))
        self.menuAdministracion = QtGui.QMenu(self.menuBar)
        self.menuAdministracion.setObjectName(_fromUtf8("menuAdministracion"))
        MainWindow.setMenuBar(self.menuBar)
        self.mainToolBar = QtGui.QToolBar(MainWindow)
        self.mainToolBar.setObjectName(_fromUtf8("mainToolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.mainToolBar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.actionConectar = QtGui.QAction(MainWindow)
        self.actionConectar.setObjectName(_fromUtf8("actionConectar"))
        self.actionSalir = QtGui.QAction(MainWindow)
        self.actionSalir.setObjectName(_fromUtf8("actionSalir"))
        self.actionCrear_M_quina = QtGui.QAction(MainWindow)
        self.actionCrear_M_quina.setObjectName(_fromUtf8("actionCrear_M_quina"))
        self.actionBorrar_M_quina = QtGui.QAction(MainWindow)
        self.actionBorrar_M_quina.setObjectName(_fromUtf8("actionBorrar_M_quina"))
        self.actionActualizar_M_quinas = QtGui.QAction(MainWindow)
        self.actionActualizar_M_quinas.setObjectName(_fromUtf8("actionActualizar_M_quinas"))
        self.actionEncender_M_quina = QtGui.QAction(MainWindow)
        self.actionEncender_M_quina.setObjectName(_fromUtf8("actionEncender_M_quina"))
        self.actionApagar_M_quina = QtGui.QAction(MainWindow)
        self.actionApagar_M_quina.setObjectName(_fromUtf8("actionApagar_M_quina"))
        self.actionReiniciar_M_quina = QtGui.QAction(MainWindow)
        self.actionReiniciar_M_quina.setObjectName(_fromUtf8("actionReiniciar_M_quina"))
        self.menuInicio.addAction(self.actionConectar)
        self.menuInicio.addAction(self.actionSalir)
        self.menuConfiguracion_de_M_quinas.addAction(self.actionCrear_M_quina)
        self.menuConfiguracion_de_M_quinas.addAction(self.actionBorrar_M_quina)
        self.menuAdministracion.addAction(self.actionActualizar_M_quinas)
        self.menuAdministracion.addAction(self.actionEncender_M_quina)
        self.menuAdministracion.addAction(self.actionApagar_M_quina)
        self.menuAdministracion.addAction(self.actionReiniciar_M_quina)
        self.menuBar.addAction(self.menuInicio.menuAction())
        self.menuBar.addAction(self.menuConfiguracion_de_M_quinas.menuAction())
        self.menuBar.addAction(self.menuAdministracion.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "KVM Virtual Machine Manager", None))
        self.pushButton.setText(_translate("MainWindow", "Conectar", None))
        self.pushButton_2.setText(_translate("MainWindow", "Actualizar Máquinas", None))
        self.pushButton_3.setText(_translate("MainWindow", "Encender Máquina", None))
        self.checkBox.setText(_translate("MainWindow", "Maquinas activas", None))
        self.checkBox_2.setText(_translate("MainWindow", "Maquinas desconectadas", None))
        self.pushButton_4.setText(_translate("MainWindow", "Apagar Máquina", None))
        self.pushButton_5.setText(_translate("MainWindow", "Crear Maquina", None))
        self.pushButton_6.setText(_translate("MainWindow", "Salir", None))
        self.pushButton_7.setText(_translate("MainWindow", "Reiniciar", None))
        self.pushButton_8.setText(_translate("MainWindow", "Borrar Máquina", None))
        self.menuInicio.setTitle(_translate("MainWindow", "Inicio", None))
        self.menuConfiguracion_de_M_quinas.setTitle(_translate("MainWindow", "Máquina", None))
        self.menuAdministracion.setTitle(_translate("MainWindow", "Administracion", None))
        self.actionConectar.setText(_translate("MainWindow", "Conectar", None))
        self.actionSalir.setText(_translate("MainWindow", "Salir", None))
        self.actionCrear_M_quina.setText(_translate("MainWindow", "Crear Máquina", None))
        self.actionBorrar_M_quina.setText(_translate("MainWindow", "Borrar Máquina", None))
        self.actionActualizar_M_quinas.setText(_translate("MainWindow", "Actualizar Máquinas", None))
        self.actionEncender_M_quina.setText(_translate("MainWindow", "Encender Máquina", None))
        self.actionApagar_M_quina.setText(_translate("MainWindow", "Apagar Máquina", None))
        self.actionReiniciar_M_quina.setText(_translate("MainWindow", "Reiniciar Máquina", None))

