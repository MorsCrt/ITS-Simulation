import libsumo
import sumolib

from simulation import Simulation
from ontology_manager import OntologyManager


if __name__ == "__main__":
    ontology_path = "itsTest.rdf"
    java_path = r"C:\Program Files\Common Files\Oracle\Java\javapath\java.exe"
    route_file = r"Sumo\osm.net.xml"
    sumo_config_file = r"Sumo\osm.sumocfg"
    output_path = "its_ontology_with_data.rdf"


    ontology_manager = OntologyManager(ontology_path=ontology_path, java_path=java_path)

    # Read the SUMO network
    net = sumolib.net.readNet(route_file)

    # Start SUMO
    libsumo.start(["sumo", "-c", sumo_config_file])

    # Initialize the simulation with the ontology manager and network
    simulation = Simulation(ontology_manager=ontology_manager, net=net)

    # Run the simulation
    simulation.run(max_steps=2)

    ontology_manager.save_ontology(output_path=output_path)