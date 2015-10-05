class Environment:
    
    simclock = 0
    rotationalPeriod = -1
    def __init__(self):
        self.simclock = 0
        self.rotationalPeriod = -1
        return None
    
    def Environment(self):
        return self
    
    def getTime(self):
        return self.simclock
    
    def incrementTime(self, muSecsIn = -1):
        if (not(isinstance(muSecsIn, int))):
            raise ValueError('Environment.incrementTime: invalid args')
        if (muSecsIn < 0):
            raise ValueError('Environment.incrementTime: invalid range')
        self.simclock += muSecsIn
        return self.simclock
    
    def getRotationalPeriod(self):
        if (self.rotationalPeriod < 0):
            raise ValueError ('Environment.getRotationalPeriod: has not been set')
        return self.rotationalPeriod
    
    def setRotationalPeriod(self, muSecsIn = -1):
        if (not(isinstance(muSecsIn, int))):
            raise ValueError('Environment.setRotationalPeriod: invalid args')
        if (muSecsIn < 1000000):
            raise ValueError('Environment.setRotationalPeriod: invalid range')
        self.rotationalPeriod = muSecsIn
        return self.rotationalPeriod
