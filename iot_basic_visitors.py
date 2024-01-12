class Visitor:
    def visit(self, component):
        pass
    def visitSensor(self, sensor):
        return sensor
    def visitDrone(self, drone):
        return drone
    def visitGateway(self, gateway):
        return gateway


class EmergencyVisitor(Visitor):
    def visit(self, component):
        pass

    def broadcastEmergencyData(self):
        pass
    def sendMessage(self,message, sender, receiver):
        pass

    def performRescueOperation(self, drone):
        # for drones only
        pass

    def communicateEmergencyInfo(self, info):
        pass

    

class LocationVisitor(Visitor):
    pass

class locationMethodSetVisitor(LocationVisitor):
    def locationMethodSet(self,component,method):
        component.acceptVisitor(self).locationMethod[0]=method
        pass

class locationUpdateVisitor(LocationVisitor):

    def locationUpdate(self, component,newLocation):
        component.acceptVisitor(self).location=newLocation
        pass
    

class locationMethodAddVisitor(LocationVisitor):
    def locationMethodAdd(self,component,method):
        component.acceptVisitor(self).locationMethod.append(method)
        pass