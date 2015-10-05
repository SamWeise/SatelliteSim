class Star:
    # Inventory Number, Magnitude, Right Ascension, and Declination
    ID = -1
    Magn = -1
    RA = -1
    Dec = -1
    
    # Constructor
    def __init__(self, IDIn, MagnIn, RAIn, DecIn):
        self.ID = IDIn
        self.Magn = float(MagnIn)
        self.RA = float(RAIn)
        self.Dec = float(DecIn)
        
        return None
    
    def getID(self):
        return self.ID
    
    def getMagn(self):
        return self.Magn
    
    def getRA(self):
        return self.RA
    
    def getDec(self):
        return self.Dec
