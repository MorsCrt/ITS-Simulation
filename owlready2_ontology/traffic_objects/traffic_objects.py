from owlready2 import Thing,get_ontology

import re

onto = get_ontology(r"updated_onto.owl").load()

class TrafficObjects(Thing):
    namespace = onto
    pass
class Vehicle(TrafficObjects):
    namespace = onto
    pass
class Veh(Vehicle):
    namespace = onto
    pass
class Truck(Vehicle):
    namespace = onto
    pass
class Bus(Vehicle):
    namespace = onto
    pass
class Tram(Vehicle):
    namespace = onto
    pass    
class Bike(Vehicle):
    namespace = onto
    pass


def create_vehicle_instance(vehicle_id):
    vehicle_type = re.split(r'\d+', vehicle_id)[0].capitalize()
    if vehicle_type in globals():
        vehicle_class = globals()[vehicle_type]
        return vehicle_class(vehicle_id)
    else:
        raise ValueError(f"No class found for vehicle type: {vehicle_type}")


onto.save(file=r"updated_onto.owl")
