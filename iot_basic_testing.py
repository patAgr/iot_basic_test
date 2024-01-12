from iot_basic_components import *
from iot_basic_visitors import *

d=Drone(None,sensorsAttached=None,resource=None)
g=Gateway(None,communicationProtocol=None,bandwidth=None)
s=Sensor(None,dataLogType=None)
infrastructure=[d, g, s]

# GNSS Station activation
print('Before method set : ',d.locationMethod)
lvLocSet=locationMethodSetVisitor()
lvLocSet.locationMethodSet(d,'GNSS')

print('After method set : ',d.locationMethod)
print('------------------')

print('Before loc update : ',d.location)
# Object localization update
newLocalization=[(0,0), (0,1), (0,2)]
lv=locationUpdateVisitor()
lv.locationUpdate(d,newLocalization)

print('After loc update : ',d.location)
print('------------------')

print('Before method update : ', d.locationMethod)
# Object localization methods update
newMethod='VisualOdometry'
lvAdd=locationMethodAddVisitor()
lvAdd.locationMethodAdd(d,'VisualOdometry')

print('After method update : ', d.locationMethod)
# Emergency situation : broadcast messages, rescue operation

