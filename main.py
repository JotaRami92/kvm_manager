from PyQt4 import QtGui
from lxml import etree
from conexiones_ui import Ui_Dialog
from crearmaquinas_ui import Ui_Dialog1
from mainwindow_ui import Ui_MainWindow
import uuid as u
import comandos as comandos


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

    def generarxml(self, maquina_dict):
        domain = etree.Element("domain", type="kvm")
        name = etree.SubElement(domain, "name").text = "%s" % maquina_dict.get('Name')
        cpu = etree.SubElement(domain, "cpu")
        topology = etree.SubElement(cpu, "topology", cores="4", sockets="1", threads="4")
        uuid = etree.SubElement(domain, "uuid").text = "%s" % u.uuid4()
        memory = etree.SubElement(domain, "memory", unit="MB").text = "%s" % maquina_dict.get('RAM')
        currentMemory = etree.SubElement(domain, "currentMemory", unit="MB").text = "%s" % maquina_dict.get('RAM')
        vcpu = etree.SubElement(domain, "vcpu", placement="static").text = "%s" % maquina_dict.get('vcpus')
        os = etree.SubElement(domain, "os")
        type = etree.SubElement(os, "type").text = "%s" % maquina_dict.get('os-type')
        boot = etree.SubElement(os, "boot", dev="hd")
        features = etree.SubElement(domain, "features")
        acpi= etree.SubElement(features, "acpi")
        apic= etree.SubElement(features, "apic")
        pae= etree.SubElement(features, "pae")
        clock = etree.SubElement(domain, "clock", offset="utc")
        on_poweroff = etree.SubElement(domain, "on_poweroff").text = "destroy"
        on_reboot = etree.SubElement(domain, "on_reboot").text = "restart"
        on_crash = etree.SubElement(domain, "on_crash").text = "restart"
        devices = etree.SubElement(domain, "devices")
        emulator = etree.SubElement(devices, "emulator").text = "/usr/libexec/qemu-kvm"
        disk = etree.SubElement(devices, "disk", device="disk", type="file")
        driver = etree.SubElement(disk, "driver", cache="none", name="qemu", type="raw")
        source = etree.SubElement(disk, "source", file="%s" % maquina_dict.get('disk path'))
        target = etree.SubElement(disk, "target", dev="hda")
        address = etree.SubElement(disk, "address", bus="0", controller="0", target="0", type="drive", unit="0")
        cdrom = etree.SubElement(devices, "disk", device="cdrom", type="file")
        source2 = etree.SubElement(cdrom, "source", file="%s" % maquina_dict.get('cdrom'))
        driver2 = etree.SubElement(cdrom, "driver", name="qemu", type="raw")
        target2 = etree.SubElement(cdrom, "target", bus="ide", dev="hdc")
        readonly = etree.SubElement(cdrom, "readonly")
        address2 = etree.SubElement(cdrom, "address", bus="1", controller="0", target="0", type="drive", unit="0")
        interface = etree.SubElement(devices, "interface", type="network")
        source_nw = etree.SubElement(interface, "source", network="%s" % maquina_dict.get('network'))
        graphics = etree.SubElement(devices, "graphics", port="-1", type="vnc")
        tree = etree.ElementTree(domain)
        tree.write('%s.xml' % maquina_dict.get('Name'), pretty_print=True, xml_declaration=True, encoding="utf-8")

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
        self.generarxml(maquina_dict)
        comandos.createDomain(maquina_dict)
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
