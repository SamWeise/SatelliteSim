import StarCatalog
import Environment as env
import math

class StarSensor:
    CONST_MUSECPERDAY = 86400000000
    
    fov = -1
    sc = None
    
    envIn = None
    
    def __init__(self, fovIn = -1):
        if (not(isinstance(fovIn,float))):
            raise ValueError('StarSensor.__init__: invalid args')
        if (fovIn < 0.0 or fovIn > math.pi/4):
            raise ValueError('StarSensor.__init__: invalid fov')
        self.fov = fovIn
        self.sc = StarCatalog.StarCatalog()
        return None
    
    def StarSensor(self):
        return self
    
    def initializeSensor(self, starFileIn = ''):
        if (not(isinstance(starFileIn, str))):
            raise ValueError('StarSensor.initializeSensor: invalid args')
        if (starFileIn == ''):
            raise ValueError('StarSensor.initializeSensor: invalid args')
        return self.sc.loadCatalog(starFileIn)
    
    def configure(self, envIn = None):
        if (envIn == None):
            raise ValueError('StarSensor.configure: invalid args')
        self.envIn = envIn
        return True
    
    def serviceRequest(self):
        if (self.envIn == None):
            return None
        
        RADSat = self.getSensorPosition()
        raSat = RADSat[0] % 1.0 * 2 * math.pi
        DSat = RADSat[1] % 1.0 * 2 * math.pi
        
        magnReturn = self.sc.getMagnitude(raSat + math.pi/2, DSat, self.fov)
        if (magnReturn == None):
            return None
       
        magnReturn = int(magnReturn * 10)
        magnReturn = self.toHex(magnReturn, 16)[2:].zfill(4)
        
        self.envIn.incrementTime(40)
        return magnReturn
    
    def getSensorPosition(self):
        if (self.envIn == None):
            return None
        return [float(self.envIn.getTime()) / self.CONST_MUSECPERDAY,
                float(self.envIn.getTime()) / self.envIn.getRotationalPeriod()]
    
    def toHex(self, num, nbits):
        return hex((num + (1 << nbits)) % (1 << nbits))
