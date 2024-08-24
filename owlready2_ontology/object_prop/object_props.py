from traffic_objects.traffic_objects import *
from network.network import *
from owlready2 import ObjectProperty,get_ontology



onto = get_ontology(r"updated_onto.owl").load()


class hasVehicleType(ObjectProperty):
    namespace = onto
    domain = [Vehicle]
    range = [Veh,Bus,Truck,Tram,Bike]

class hasWayType(ObjectProperty):
    namespace = onto
    domain = [Way]
    range = [Aerialway,Waterway,Railway,Highway,Aeroway]

class hasEmission(ObjectProperty):
    namespace = onto
    domain = [Highway, Motorway, Trunk, Primary, Secondary, Tertiary, Unclassified, Residential, MotorwayLink, TrunkLink, PrimaryLink, SecondaryLink, TertiaryLink, LivingStreet, Service, Pedestrian, Track, BusGuideway, Escape, Raceway, UnknownRoadType, Busway, Footway, Bridleway, Steps, Corridor, Path, ViaFerrata, Cycleway]
    range = [Pollution]


class hasLane(ObjectProperty):
    namespace = onto
    domain = [Edge]
    range = [Lane]

    
class inTheWay(ObjectProperty):
    namespace = onto
    domain = [Pollution]
    range = [Highway, Motorway, Trunk, Primary, Secondary, Tertiary, Unclassified, Residential, MotorwayLink, TrunkLink, PrimaryLink, SecondaryLink, TertiaryLink, LivingStreet, Service, Pedestrian, Track, BusGuideway, Escape, Raceway, UnknownRoadType, Busway, Footway, Bridleway, Steps, Corridor, Path, ViaFerrata, Cycleway]
    inverse_property = hasEmission



onto.save(file=r"updated_onto.owl")
