from ConfParser import *

def BuildStatusList(services):
    serviceDict = {}
    for item in services:
        serviceDict[item] = 0
    return serviceDict
    
