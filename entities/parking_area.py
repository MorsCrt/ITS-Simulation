from dataclasses import dataclass, field
from typing import List
import libsumo
from ontology_manager import OntologyManager

@dataclass
class ParkingArea:
    id: str
    ontology_manager: OntologyManager
    vehicle_count: List[int] = field(default_factory=list)

    def update_parking_data(self):
        self.vehicle_count.append(libsumo.parkingarea.getVehicleCount(self.id))
        
        data = {
            'VehicleCount': self.vehicle_count[-1]
        }
        self.ontology_manager.create_instance("ParkingArea", self.id, data)
