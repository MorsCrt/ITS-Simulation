from dataclasses import dataclass, field
from typing import Dict
import libsumo
import sumolib
from entities.vehicle import Vehicle
from entities.traffic_light import TrafficLight
from entities.parking_area import ParkingArea
from entities.street import Street
from ontology_manager import OntologyManager
from entities.buildings import Buildings
from entities.person import Person

@dataclass
class Simulation:
    ontology_manager: OntologyManager
    net: sumolib.net.Net
    vehicles: Dict[str, Vehicle] = field(default_factory=dict)
    traffic_lights: Dict[str, TrafficLight] = field(default_factory=dict)
    parking_areas: Dict[str, ParkingArea] = field(default_factory=dict)
    streets: Dict[str, Street] = field(default_factory=dict)
    buildings: Dict[str, Buildings] = field(default_factory=dict)
    person:  Dict[str, Person] = field(default_factory=dict)
    step: int = 0


    def run(self, max_steps=2):
        while self.step < max_steps:
            libsumo.simulationStep()
            self.update_streets()
            self.update_vehicles()
            self.update_parking_areas()
            self.update_traffic_lights()
            self.update_persons()
            self.update_buildings()
            self.step += 1
    
    # TODO: Instance creation method for this should be redefine after emergency vehicles, and different fuel type vehicles
    def update_vehicles(self):
        vehicle_ids = libsumo.vehicle.getLoadedIDList()
        for vehicle_id in vehicle_ids:
            if vehicle_id not in self.vehicles:
                self.vehicles[vehicle_id] = Vehicle(vehicle_id, self.ontology_manager)
            vehicle_instance = self.vehicles[vehicle_id]
            vehicle_instance.update_vehicle_data()
            if vehicle_instance.is_moving():
                print(vehicle_id)

    def update_traffic_lights(self):
        traffic_light_ids = libsumo.trafficlight.getIDList()
        for traffic_light_id in traffic_light_ids:
            if traffic_light_id not in self.traffic_lights:
                self.traffic_lights[traffic_light_id] = TrafficLight(traffic_light_id, self.ontology_manager)
            traffic_light_instance = self.traffic_lights[traffic_light_id]
            traffic_light_instance.update_traffic_light_data()

    def update_parking_areas(self):
        parking_area_ids = libsumo.parkingarea.getIDList()
        for parking_id in parking_area_ids:
            if parking_id not in self.parking_areas:
                self.parking_areas[parking_id] = ParkingArea(parking_id, self.ontology_manager)
            parking_instance = self.parking_areas[parking_id]
            parking_instance.update_parking_data()


    def update_buildings(self):
        poi_ids = libsumo.poi.getIDList()
        for poi_id in poi_ids:
            building_type = libsumo.poi.getType(poi_id).split(".")[-1]
            if poi_id not in self.buildings:
                self.buildings[poi_id] = Buildings(id=poi_id, 
                                                   net=self.net,
                                                    building_type=building_type,
                                                    ontology_manager = self.ontology_manager)
            building_instance = self.buildings[poi_id]
            building_instance.update_building_data()
    
    def update_persons(self):
        person_ids = libsumo.person.getIDList()
        for person_id in person_ids:
            if person_id not in self.person:
                self.person[person_id] = Person(id=person_id, 
                                                    ontology_manager = self.ontology_manager)
            person_instance = self.person[person_id]
            person_instance.update_person_data()

    # TODO: Some data can be belong to two different street like highway.motorway | highway.cycleway
    def update_streets(self):
        # TODO: Change Entity-IRI options in Protege for #
        # TODO: link, tram, cycle also belong to vehicles
        edges = [edge for edge in self.net.getEdges()
                 if "#" not in edge.getID() and not any(keyword in str(edge.getType()) for keyword in ["link", "tram", "cycle"])]
        for edge in edges:
            edge_id = edge.getID()
            # Example edge_type 'highway.footway'
            edge_type = edge.getType().split(".")[-1]

            self.streets[edge_id] = Street(id=edge_id,edge_type=edge_type,ontology_manager=self.ontology_manager)
            street_instance = self.streets[edge_id]

            street_instance.update_street_data()