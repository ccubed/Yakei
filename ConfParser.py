# Parse Yakei Config Files
from os import path

class ConfMissingError(Exception):
    def __init__(self):
        self.value = "Yakei.conf not found"
    def __str__(self):
        return repr(self.value)

class ConfBadlyFormed(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class YakeiConfig:
    def __init__(self):
        self.data = {}
        self.currentDomain = ''
        self.currentService = ''
        self.currentServices = {}
        self.isService = False
        self.isDomain = False
        if os.path.isfile("Yakei.conf"):
            self.ReadConfig()
        else:
            raise ConfMissingError()

    def ReadConfig(self):
        conf = open('Yakei.conf','r')
        for index, line in enumerate(conf.readlines()):
            if not line.startswith('*'):
                if 'Domain' in line.strip():
                    if line.strip().startswith('<') and self.isDomain:
                        raise ConfBadlyFormed("Missing closing tag for Domain Directive. Line {0}.".format(index))
                    elif line.strip().startswith('</') and self.isDomain:
                        self.isDomain = False
                    else:
                        self.isDomain = True
                        self.currentDomain = line.strip().split(" ")[1].rstrip('>')
                        self.data[self.currentDomain] = {}
                elif 'Service' in line.strip():
                    if line.strip().startswith("<") and self.isService:
                        raise ConfBadlyFormed("Missing closing tag for Service Directive. Line {0}.".format(index))
                    elif not self.isDomain:
                        raise ConfBadlyFormed("Service Directive without matching Domain Directive. Line {0}".format(index))
                    elif line.strip.startswith("</") and self.isService:
                        self.isService = False
                        self.data[self.currentDomain][self.currentService] = self.currentServices
                    else:
                        self.isService = True
                        self.currentService = line.strip().split(" ")[1].rstrip('>')
                        self.currentServices = {}
                elif '=' in line.strip():
                    which = line.strip().split('=')[0].lower()
                    value = line.strip().split('=')[1].lower()
                    if which not in ['type', 'poll', 'load', 'notification', 'endpoint', 'altlocation', 'datatype', 'expected', 'name']:
                        raise ConfBadlyFormed("Bad type. Got type {0} on line {1}".format(which, index))
                    elif not self.isDomain or not self.isService:
                        raise ConfBadlyformed("Got a setting value outside a Domain or Service Directive. Line {0}.".format(index))
                    else:
                        self.currentServices[which] = value

    def GetDomains(self):
        return 'List of Domains'

    def GetServices(self, which):
        return 'List of Services for a Domain'
