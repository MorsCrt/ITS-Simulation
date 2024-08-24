from dataclasses import dataclass, field
from typing import List
import libsumo
from ontology_manager import OntologyManager

@dataclass
class Vehicle:
    id: str
    ontology_manager: OntologyManager
    person_capacitiy: int = 0
    co2_emission: List[float] = field(default_factory=list)
    speed: List[float] = field(default_factory=list)
    acceleration: List[float] = field(default_factory=list)
    length: List[float] = field(default_factory=list)
    width: List[float] = field(default_factory=list)
    height: List[float] = field(default_factory=list)
    fuel_consumption: List[float] = field(default_factory=list)
    electricity_consumption: List[float] = field(default_factory=list)

    def update_vehicle_data(self):
        self.co2_emission.append(float(libsumo.vehicle.getCO2Emission(self.id)))
        self.speed.append(float(libsumo.vehicle.getSpeed(self.id)))
        self.acceleration.append(float(libsumo.vehicle.getAcceleration(self.id)))
        self.length.append(float(libsumo.vehicle.getLength(self.id)))
        self.width.append(float(libsumo.vehicle.getWidth(self.id)))
        self.height.append(float(libsumo.vehicle.getHeight(self.id)))
        self.fuel_consumption.append(float(libsumo.vehicle.getFuelConsumption(self.id)))
        self.electricity_consumption.append(float(libsumo.vehicle.getElectricityConsumption(self.id)))
        self.person_capacitiy.append(float(libsumo.vehicle.getPersonCapacity(self.id)))

        data = {
            'CO2Emission': self.co2_emission[-1],
            'VehicleSpeed': self.speed[-1],
            'VehicleAcceleration': self.acceleration[-1],
            'FuelConsumptions': self.fuel_consumption[-1],
            'ElectricityConsumptions': self.electricity_consumption[-1],
            'Length': self.length[-1],
            'Width': self.width[-1],
            'Height': self.height[-1],
            'PersonCapacity': self.person_capacitiy
        }
        self.ontology_manager.create_instance("Vehicle", self.id, data)

    def is_moving(self):
        return self.speed[-1] > 0 if self.speed else False