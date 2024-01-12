class Component:
    def acceptVisitor(self, visitor):
        return visitor.visit(self)
    def __init__(self, location):
        self.location = location
        self.locationMethod = [None]
        self.sodaSystemMetrics=None

class Drone(Component):
    def __init__(self, location, sensorsAttached,resource):
        super().__init__(location)
        self.sensorsAttached = sensorsAttached
        self.resource = resource
    
    def acceptVisitor(self, visitor):
        return visitor.visitDrone(self)

class Sensor(Component):

    def acceptVisitor(self, visitor):
        return visitor.visitSensor(self)
    def __init__(self, location, dataLogType):
        super().__init__(location)
        self.dataLogType = dataLogType


class Gateway(Component):
    def __init__(self, location, communicationProtocol,bandwidth):
        super().__init__(location)
        self.communicationProtocol = communicationProtocol
        self.bandwidth = bandwidth

    def acceptVisitor(self, visitor):
        return visitor.visitGateway(self)

class SodaInternMetrics:
    def __init__(self, effectiveness, operability, availability):
        self.effectiveness = effectiveness
        self.operability = operability
        self.availability = availability
    
class ResourceManager:
    def __init__(self,type,level,levelHistory,location):
        self.type=type
        self.level=level
        self.levelHistory=levelHistory
        self.location=location