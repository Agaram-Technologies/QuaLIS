import os
from configparser import ConfigParser

objectRepository=ConfigParser()
objectRepository.read(os.path.dirname(os.path.abspath(__file__))+"\\ObjectRepository\\ElementBaseMaster.ini")

d=objectRepository.get("UnitOfMeasurement", "masterIcon")

#print((os.path.abspath(__file__))+"\\ObjectRepository\\ElementBaseMaster.ini")

