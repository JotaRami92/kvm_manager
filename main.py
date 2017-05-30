import os
from PyQt4 import QtGui
from PyQt4.QtGui import QListWidgetItem, QFileDialog
from lxml import etree
from iso_ui import Ui_Dialog as iso_dialog
from main_ui import Ui_MainWindow
import uuid as u
import libvirt as lib

connection = None


class PopUpCrearMaquinas(QtGui.QDialog):

    def __init__(self):
        QtGui.QDialog.__init__(self)
        self.ui = iso_dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_3.clicked.connect(self.seleccionar)
        self.ui.pushButton_2.clicked.connect(self.salir)
        self.ui.pushButton.clicked.connect(self.aceptar)

    def seleccionar(self):
        self.ui.lineEdit.setText(QFileDialog.getOpenFileName())


    def generarXML(self, machine_list):
        tree = etree.parse("maquina.xml")
        tree.find('uuid').text = machine_list[3]
        tree.find('memory').text =machine_list[2]
        tree.find('currentMemory').text = machine_list[2]
        tree.find('name').text = machine_list[1]
        for host_ip in tree.xpath("/domain/devices/disk[@device='disk']/source"):
            host_ip.attrib['file'] = machine_list[4]
        for host_ip in tree.xpath("/domain/devices/disk[@device='cdrom']/source"):
            host_ip.attrib['file']=machine_list[0]
        tree.write("%s.xml" % machine_list[1])

    def crear(self, machine_list):
        global connection
        global info
        xml = ""
        archivo="%s.xml" % machine_list[1]
        with open(archivo, "r") as file:
            xml = file.read()
        connection.defineXML(xml)
        for id in connection.listDomainsID():
            dom = connection.lookupByID(id)
            info = dom.info()



    def aceptar(self):
        machine_list = []
        machine_list.append(str(self.ui.lineEdit.text()))
        machine_list.append(str(self.ui.lineEdit_2.text()))
        machine_list.append(str(self.ui.lineEdit_3.text()))
        machine_list.append(str(u.uuid4()))
        machine_list.append(str("/var/lib/libvirt/images/%s.img" % self.ui.lineEdit_2.text()))
        self.generarXML(machine_list)
        cmd="qemu-img create -f qcow2 /var/lib/libvirt/images/%s.img 1g" % machine_list[1]
        os.system(cmd)
        self.crear(machine_list)
        self.accept()

    def salir(self):
        self.reject()


class MainUi(QtGui.QMainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.setWindowTittle("KVM virtual machine manager")
        self.ui.pushButton_8.clicked.connect(self.conectar)
        self.ui.pushButton_7.clicked.connect(self.crearMaquina)




    def conectar(self):
        global connection
        connection = lib.open("qemu:///system")
        self.ui.plainTextEdit.setPlainText("Conectado a " + connection.getHostname())
        item = QListWidgetItem(str("Maquinas apagadas"))
        self.ui.listWidget.addItem(item)
        cont = 1
        for names in connection.listDefinedDomains():
            item=QListWidgetItem(str(names))
            self.ui.listWidget.addItem(item)
            self.dicA[names]=cont
            cont=cont+1
        item=QListWidgetItem(str(""))
        self.ui.listWidget.addItem(item)
        item=QListWidgetItem(str(""))
        self.ui.listWidget.addItem(item)


    def crearMaquina(self):
        self.dialog = PopUpCrearMaquinas()
        self.dialog.exec_()


if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    window = MainUi()
    window.show()
    sys.exit(app.exec_())
