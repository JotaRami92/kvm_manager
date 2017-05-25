import libvirt as lib

global connection

def connect(self):
    connection = lib.open("qemu:///system")

def createDomain(self, maquina_dict):
    xml = ""
    with open(maquina_dict.get('Name'), "r") as file:
        xml = file.read()
    connection.defineXML(xml)

def deleteDomain(self, domain):
    virtual_machine = connection.lookupByName("%s", domain)
    virtual_machine.undefine()

def startDomain(self, vm):
    vm.create()

def stopDomain(self, vm):
    vm.destroy()

def listDomains(self, running):
    if running:
        connection.listDomainsID()
    else:
        connection.listDefinedDomains()

def findDomain(self, name):
    virtual_machine = connection.lookupByName("%s" % name)





