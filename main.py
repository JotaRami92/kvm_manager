from PyQt4 import QtGui
from mainwindow_ui import Ui_MainWindow
from crearmaquinas_ui import Ui_Dialog1
from conexiones_ui import Ui_Dialog
from yattag import Doc, indent


class PopUpConectar(QtGui.QDialog):



    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        # self.setWindowTittle("KVM Iniciar conexion")
        self.ui.pushButton.clicked.connect(self.iniciarSesion)
        self.ui.pushButton_2.clicked.connect(self.ok)


    def iniciarSesion(self):


        self.accept

    def ok(self):
        self.accept()


class PopUpCrearMaquinas(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = Ui_Dialog1()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.finalizar)
        self.ui.pushButton_2.clicked.connect(self.salir)




    def finalizar(self):
        maquina_dict = {}
        lista1= []
        lista2= []
        for child in self.findChildren(QtGui.QLineEdit):
            lista1.append(str(child.text()))
        for child in self.findChildren(QtGui.QLabel):
            lista2.append(str(child.text()))
        for i in range(len(lista1)):
            maquina_dict[lista2[i]] = lista1[i]

        #pasar al crear
        self.accept()

    def salir(self):
        self.reject()



class MainUi(QtGui.QMainWindow):

    def __init__(self):
        #poner titulo ventana
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowTittle("KVM virtual machine manager")
        self.ui.pushButton.clicked.connect(self.conectar)
        self.ui.pushButton_5.clicked.connect(self.crearMaquinas)
        self.ui.pushButton_6.clicked.connect(self.cerrar)
        # self.ui.pushButton_2.clicked.connect(self.actualizarMaquinas)
        # self.ui.pushButton_3.clicked.connect(self.encenderMaquina)
        # self.ui.pushButton_7.clicked.connect(self.reiniciarMaquina)
        # self.ui.pushButton_4.clicked.connect(self.apagarMaquina)
        # self.ui.pushButton_8.clicked.connect(self.borrarMaquina)

    def conectar(self):
        #poner titulo ventana
        self.dialog = PopUpConectar()
        self.dialog.exec_()

    def crearMaquinas(self):

        self.dialog = PopUpCrearMaquinas()
        self.dialog.exec_()

    # def actualizarMaquinas(self):
    #     #
    #     #
    #
    # def encenderMaquina(self):
    #     #
    #
    #
    #
    # def reiniciarMaquina(self):
    #     #
    #
    #
    #
    # def apagarMaquina(self):
    #     #
    #
    # def borrarMaquina(self):
    #     #


    def cerrar(self):
        exit()



if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec_())
