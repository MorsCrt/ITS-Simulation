from owlready2 import Thing, get_ontology

onto = get_ontology("test.owl")

class Infrastructure(Thing):
    namespace = onto    
    pass

class Buildings(Infrastructure):
    namespace = onto
    pass

class Accommodation(Buildings):
    namespace = onto
    pass

class Apartments(Buildings):
    namespace = onto
    pass

class Barracks(Buildings):
    namespace = onto
    pass

class Bungalow(Buildings):
    namespace = onto
    pass

class Cabin(Buildings):
    namespace = onto
    pass

class DetachedHouse(Buildings):
    namespace = onto
    pass

class Dormitory(Buildings):
    namespace = onto
    pass

class Farmhouse(Buildings):
    namespace = onto
    pass

class Ger(Buildings):
    namespace = onto
    pass

class Hotel(Buildings):
    namespace = onto
    pass

class House(Buildings):
    namespace = onto
    pass

class Houseboat(Buildings):
    namespace = onto
    pass

class ResidentialBuilding(Buildings):
    namespace = onto
    pass

class SemiDetachedHouse(Buildings):
    namespace = onto
    pass

class StaticCaravan(Buildings):
    namespace = onto
    pass

class StiltHouse(Buildings):
    namespace = onto
    pass

class Terrace(Buildings):
    namespace = onto
    pass

class TreeHouse(Buildings):
    namespace = onto
    pass

class Trullo(Buildings):
    namespace = onto
    pass


class TrafficLights(Infrastructure):
    namespace = onto
    pass
    
class ParkingArea(Infrastructure):
    namespace = onto
    pass

class ChargingStation(Infrastructure):
    namespace = onto
    pass

class BusStop(Infrastructure):
    namespace = onto
    pass


onto.save(file=r"updated_onto.owl")











