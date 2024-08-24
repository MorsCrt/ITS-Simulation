from dataclasses import dataclass, field
from typing import List
import libsumo
from ontology_manager import OntologyManager

@dataclass
class Person:
    id: str
    ontology_manager: OntologyManager
    person_vehicle: List[str] = field(default_factory=list)

    def update_person_data(self):
        self.person_vehicle.append(libsumo.person.getVehicle(self.id))
        
        data = {
            'PersonVehicle': self.person_vehicle[-1]
        }
        self.ontology_manager.create_instance("Pedestrian", self.id, data)
