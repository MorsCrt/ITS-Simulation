from dataclasses import dataclass, field
import libsumo
import sumolib
from ontology_manager import OntologyManager

@dataclass
class Buildings:
    net: sumolib.net.Net
    id: str
    building_type : str
    ontology_manager: OntologyManager
    x: float= field(default_factory=float)
    y: float= field(default_factory=float)
    lon: float= field(default_factory=float)
    lat: float= field(default_factory=float)

    def update_building_data(self):
        self.x, self.y = libsumo.poi.getPosition(self.id)
        self.lon, self.lat = self.net.convertXY2LonLat(self.x, self.y)

        data = {
            'XLocationInSUMO' :  self.x,
            'YLocationInSUMO' : self.y,
            'LonLocation' : self.lon,
            'LatLocation' : self.lat
            }
        self.ontology_manager.create_instance(self.building_type, self.id, data)
