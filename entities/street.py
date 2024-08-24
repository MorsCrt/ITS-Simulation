from dataclasses import dataclass, field
from typing import List
import libsumo
from ontology_manager import OntologyManager

# TODO: Street and Vehicle shares same emissions split with inheritance
@dataclass
class Street:
    id: str
    edge_type: str
    ontology_manager: OntologyManager
    co2_emission: List[float] = field(default_factory=list)
    co_emission: List[float] = field(default_factory=list)
    hc_emission: List[float] = field(default_factory=list)
    pmx_emission: List[float] = field(default_factory=list)
    nox_emission: List[float] = field(default_factory=list)
    fuel_consumption: List[float] = field(default_factory=list)
    electricity_consumption: List[float] = field(default_factory=list)
    street_name: str = ""

    def update_street_data(self):
        try:
            self.co2_emission.append(libsumo.edge.getCO2Emission(self.id))
            self.co_emission.append(libsumo.edge.getCOEmission(self.id))
            self.hc_emission.append(libsumo.edge.getHCEmission(self.id))
            self.pmx_emission.append(libsumo.edge.getPMxEmission(self.id))
            self.nox_emission.append(libsumo.edge.getNOxEmission(self.id))
            self.fuel_consumption.append(libsumo.edge.getFuelConsumption(self.id))
            self.electricity_consumption.append(libsumo.edge.getElectricityConsumption(self.id))
            self.street_name = libsumo.edge.getStreetName(self.id)


            data = {
                'CO2Emission': self.co2_emission[-1],
                'COEmission': self.co_emission[-1],
                'HCEmission': self.hc_emission[-1],
                'PMxEmission': self.pmx_emission[-1],
                'NOxEmission': self.nox_emission[-1],
                'FuelConsumptions': self.fuel_consumption[-1],
                'ElectricityConsumptions': self.electricity_consumption[-1],
                'StreetName': self.street_name
            }
            self.ontology_manager.create_instance(self.edge_type, self.id, data)

        except libsumo.libsumo.TraCIException:
            pass
