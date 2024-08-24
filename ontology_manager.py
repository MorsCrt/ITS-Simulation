from owlready2 import get_ontology
import re


# TODO: Add type hints
# TODO: DataProperties can be use append or directly assigned depending on the data type
class OntologyManager:
    def __init__(self, ontology_path: str, java_path: str):
        from owlready2 import JAVA_EXE
        JAVA_EXE = java_path
        self.onto = get_ontology(ontology_path).load()

    def find_class(self, class_name):
        """
        Find and return a class from the ontology by name.
        """
        cls = next((c for c in self.onto.classes() if c.name == class_name), None)
        if cls is None:
            raise ValueError(f"Class {class_name} not found in ontology.")
        return cls
    
    def normalize_class_name(self, class_name: str) -> str:
        """
        Normalize an input string to match the naming convention of ontology classes.

        This function converts an input string with potential variations (e.g., underscores, 
        mixed casing, spaces, or improperly capitalized camel case formats) into a standardized 
        class name that adheres to the camel case convention commonly used in ontologies.

        Parameters:
        - class_name (str): The input string representing the class name to be normalized.

        Returns:
        - str: The normalized class name in camel case, suitable for matching ontology classes.

        Example:
        normalize_class_name("Living_street") -> "LivingStreet"
        normalize_class_name("living_street") -> "LivingStreet"
        normalize_class_name("street") -> "Street"
        normalize_class_name("HIGHWAY_MAJOR") -> "HighwayMajor"
        normalize_class_name("Trafficlights") -> "TrafficLights"
        """
        # Convert to lowercase, split by underscores, spaces, or camel case transitions
        words = re.findall(r'[a-z]+|[A-Z][a-z]*', class_name)

        # Capitalize each word and join them together
        normalized_name = ''.join(word.capitalize() for word in words)

        return normalized_name

    def create_instance(self, class_name, instance_id, data):
        """
        Create an instance of a class in the ontology and populate it with data.
        """
        try:
            cls = self.find_class(self.normalize_class_name(class_name))
        except ValueError as e:
            print(e)
            return None  # Continue processing, but skip instance creation for this class

        with self.onto:
            instance = cls(instance_id)

        for data_prop, value in data.items():
            getattr(instance, data_prop).append(value)

        return instance

   
    def save_ontology(self, output_path: str):
        """
        Save the ontology to the specified path.
        
        :param output_path: The file path to save the ontology.
        """
        self.onto.save(file = output_path, format = "rdfxml")