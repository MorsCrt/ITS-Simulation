import os

from infrastructure.infrastructure import *
from traffic_objects.traffic_objects import *
from network.network import *

from owlready2 import * 

onto = get_ontology(r"updated_onto.owl").load()


class Length(DataProperty):
    namespace = onto
    domain = [Vehicle]
    range = [float]

    
class Width(DataProperty):
    namespace = onto
    domain = [Vehicle]
    range = [float]
class Height(DataProperty):
    namespace = onto
    domain = [Vehicle]
    range = [float]
class Speed(DataProperty):
    namespace = onto
    domain = [Vehicle]
    range = [float]


class Type(DataProperty):
    namespace = onto
    domain = [Edge]
    range = [str]


class ParkingAreaVehicleCount(DataProperty):
    namespace = onto
    domain = [ParkingArea]
    range=  [int]

class BusStopVehicleCount(DataProperty):
    namespace = onto
    domain = [BusStop]
    range=  [int]

class VehicleCount(DataProperty):
    namespace = onto
    domain = [ChargingStation]
    range=  [int]



class ColorState(DataProperty):
    namespace = onto
    domain = [TrafficLights]
    range = [str]


class CO2Emission(DataProperty):
    namespace = onto
    domain = [Edge]
    range = [float]

class COEmission(DataProperty):
    namespace = onto
    domain = [Edge]
    range = [float]

class HCEmission(DataProperty):
    namespace = onto
    domain = [Edge]
    range = [float]


class HCEmission(DataProperty):
    namespace = onto
    domain = [Edge]
    range = [float]

class PMxEmission(DataProperty):
    namespace = onto
    domain = [Edge]
    range = [float]

class NOxEmission(DataProperty):
    namespace = onto
    domain = [Edge]
    range = [float]

onto.save(file=r"updated_onto.owl")
