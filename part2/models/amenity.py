# models/amenity.py
from basse_model import BaseModel
from place import amenity

class Amenity(BaseModel):
    def __init__(self, wifi, parking, garage, picine, climatisation):
        super().__init__()
        self.wifi = wifi
        self.parking = parking
        self.garage = garage
        self.picine = picine
        self.climatisation = climatisation
    
    @property
    # verifie qui a bien la wifie
    def wifi(self):
        return self.__wifi
    @wifi.setter
    def wifi(self, value):
        if not isinstance(value, bool):
            raise TypeError("doit avoir la wifie")
        self.__wifi = value
    
    @property
    # verifie qui a bien le parking
    def parking(self):
        return self.__parking
    @parking.setter
    def parking(self, value):
        if not isinstance(value, bool):
            raise TypeError("doit avoir le parking")
        self.__parking = value
    
    @property
    # verifie qui a bien le garage
    def garage(self):
        return self.__garage
    @garage.setter
    def garage(self, value):
        if not isinstance(value, bool):
            raise TypeError("doit avoir le garage")
        self.__garage = value
    
    @property
    # verifie qui a bien la picine
    def picine(self):
        return self.__picine
    @picine.setter
    def picine(self, value):
        if not isinstance(value, bool):
            raise TypeError("doit avoir la picine")
        self.__picine = value
    
    @property
    # verifie qui a bien la climatisation
    def climatisation(self):
        return self.__climatisation
    @climatisation.setter
    def climatisation(self, value):
        if not isinstance(value, bool):
            raise TypeError("doit avoir la climatisation")
        self.__climatisation = value