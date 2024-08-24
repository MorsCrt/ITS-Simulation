from dataclasses import dataclass, field
from typing import List
import libsumo
from ontology_manager import OntologyManager

@dataclass
class TrafficLight:
    id: str
    ontology_manager: OntologyManager
    color_state: List[str] = field(default_factory=list)

    def update_traffic_light_data(self):
        if "#" not in self.id:  # Skip problematic IDs
            self.color_state.append(str(libsumo.trafficlight.getRedYellowGreenState(self.id)))
            
            data = {
                'ColorState': self.color_state[-1]
            }
            self.ontology_manager.create_instance("TrafficLights", self.id, data)
