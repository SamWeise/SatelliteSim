import Star as Star
import math

class StarCatalog:
    StarList = []
    lowestMagn = -100.0
    highestMagn = 100.0
    
    def __init__(self):
        return None
        
    def StarCatalog(self):
        return self
    
    def loadCatalog(self, starFile = None):
        print "Loading Catalog\n"
        numStarsAdded = 0
        newList = []
        
        # Exception Test: Is file valid?
        try:
            File = open(starFile, 'r')
        except IOError:
            print "Exception Raised: Invalid File\n Loading Failed"
            raise ValueError("Exception Raised: Invalid File\n Loading Failed")
        
        for line in File:       # For each line in the file, parse line and create new Star object
            inStringList = line.strip('\n').split('\t')
            inID = int(inStringList[0])
            inMagn = float(inStringList[1])
            inRA = float(inStringList[2])
            inDec = float(inStringList[3])
            
            if (inRA > 2 * math.pi):
                inRA -= 2 * math.pi
            newStar = Star.Star(inID, inMagn, inRA, inDec)
                
            # Exception Test: Is Star duplicate?
            try:
                for star in self.StarList:
                    if newStar.getID() == star.getID():
                        raise ValueError
            except ValueError:
                print "Exception Raised: Duplicate Star Found\n Loading Failed"
                raise ValueError
                
            # Add new Star to new List and run Magnitude Tests
            newList.append(newStar)
            numStarsAdded = numStarsAdded + 1
            if newStar.getMagn() > self.highestMagn:
                self.highestMagn = newStar.getMagn()
            elif newStar.getMagn() < self.lowestMagn:
                self.lowestMagn = newStar.getMagn()
            
            # Close File and Concatenate Old List with New List
        File.close()
        self.StarList = self.StarList + newList
        
        print "Loading Completed Successfully"
        return numStarsAdded
    
    def emptyCatalog(self):
        # Move Old List reference to a new empty List
        self.StarList = []
        print "Catalog Cleared Successfully"
        
    def getStarCount(self, lowerMagnitude = -100.0, upperMagnitude = 100.0):
        # Exception Test: Are Parameters Valid?
        try:
            if isinstance(lowerMagnitude, int) and isinstance(upperMagnitude, int):
                pass
            else:
                raise ValueError
        except ValueError:
            return "Exception Raised: Parameters are not valid"
        
        # Exception Test: Is Lower Bound > Upper Bound?
        try:
            if lowerMagnitude > upperMagnitude:
                raise ValueError
        except ValueError:
            return "Exception Raised: Lower Bound cannot be greater than Upper Bound"
        
        # If Lower and/or Upper Bounds not provided, then use max/min as bounds
        if lowerMagnitude == -100.0:
            lowerMagnitude = self.lowestMagn
        if upperMagnitude == 100.0:
            upperMagnitude = self.highestMagn
        
        # Start counting stars in catalog that are between bounds    
        starcount = 0            
        for star in self.StarList:
            if (star.getMagn() > lowerMagnitude) and (star.getMagn() < upperMagnitude):
                starcount = starcount + 1
        
        return starcount
    
    def getMagnitude(self, RACP, DCP, FOV):
        # Exception Test: Are Parameters Valid?
        try:
            if isinstance(RACP, float) and isinstance(DCP, float) and isinstance(FOV, float):
                pass
            else:
                raise ValueError
        except ValueError:
            return "Exception Raised: Parameters are not valid"
        
        # For each star in catalog, if it is located in field of view, then it is a candidate for return
        newList = []
        for star in self.StarList:
            if star.getRA() >= RACP - (FOV/2) and star.getRA() <= RACP + (FOV/2):
                if star.getDec() >= DCP - (FOV/2) and star.getDec() <= DCP - (FOV/2):
                    newList.append(star)
        
        # For each star in new list, identify and return the one with the lowest magnitude
        if newList.__len__() == 0:
            return None
        
        returnStar = newList[0]
        for star in newList:
            if star.getMagn() < returnStar.getMagn():
                returnStar = star
        
        return returnStar
