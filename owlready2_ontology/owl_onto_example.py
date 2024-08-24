from owlready2 import *


"""
Example for OwlReady2 ontology structure
"""


onto = get_ontology("test.owl")

class Environment(Thing): namespace = onto
     
class Infrastructure(Environment): namespace = onto  

class TrafficObjects(Environment): namespace = onto
    

class Buildings(Infrastructure): namespace = onto

class TrafficInfrastructure(Infrastructure): namespace = onto

class Vehicle(TrafficObjects): namespace = onto
    
class FuelVehicles(Vehicle): namespace = onto
    
class FuelVeh(FuelVehicles): namespace = onto
    
class FuelTruck(FuelVehicles): namespace = onto
    
class FuelBus(FuelVehicles): namespace = onto
    
class ElectricVehicles(Vehicle): namespace = onto

class HumanPoweredVehicles(Vehicle): namespace = onto

class Length(DataProperty):
    namespace = onto
    range = [float]

    
class Width(DataProperty):
    namespace = onto
    range = [float]
class Height(DataProperty):
    namespace = onto
    range = [float]
    
class Speed(DataProperty):
    namespace = onto
    domain = [Vehicle]
    range = [float]

class hasVehicleType(ObjectProperty):
    namespace = onto
    domain = [Vehicle]
    range = [ElectricVehicles,HumanPoweredVehicles,FuelVehicles]
