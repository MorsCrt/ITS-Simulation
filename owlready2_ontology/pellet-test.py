from owlready2 import *
owlready2.JAVA_EXE = r"C:\Program Files\Common Files\Oracle\Java\javapath\java.exe"

onto = get_ontology("traffic_scene.owl")


with onto:
    class TrafficScenarioElement(Thing):
        pass

    class Infrastructure(TrafficScenarioElement):
        pass

    class TrafficParticipant(TrafficScenarioElement):
        pass

    class Obstacle(TrafficScenarioElement):
        pass

    class Vehicle(TrafficParticipant):
        pass

    class LaneSegment(TrafficScenarioElement):
        pass

    class Intersection(TrafficScenarioElement):
        pass

    class Connector(TrafficScenarioElement):
        pass

    class TrafficLight(Infrastructure):
        pass

    class TrafficRegulation(Thing):
        has_region = ObjectProperty()
        preferred_lane = DataProperty()

    class Region(Thing):
        pass


with onto:
    class has_preferred_lane(ObjectProperty):
        domain = [LaneSegment]
        range = [str]

    class has_traffic_regulations(ObjectProperty):
        domain = [TrafficScenarioElement]
        range = [TrafficRegulation]

    class contains_traffic_light(ObjectProperty):
        domain = [Intersection]
        range = [TrafficLight]

    class contains_traffic_regulating_person(ObjectProperty):
        domain = [Intersection]
        range = [TrafficParticipant]

    class has_conflicting_connector(ObjectProperty):
        domain = [Intersection]
        range = [Connector]

    class has_environment_conditions(ObjectProperty):
        domain = [TrafficScenarioElement]
        range = [DataProperty]

    
    class has_to_give_way(ObjectProperty):
        domain = [Connector]
        range = [Connector]

    class has_to_wait_for_traffic_light(ObjectProperty):
        domain = [Connector]
        range = [TrafficLight]


with onto:
    class maximum_speed(DataProperty):
        domain = [LaneSegment]
        range = [int]

    class color(DataProperty):
        domain = [TrafficLight]
        range = [str]

    class preferred_lane(DataProperty, FunctionalProperty):
        domain = [TrafficRegulation]
        range = [str]


bavaria = Region("Bavaria")


regulation_traffic_light = TrafficRegulation("regulation_traffic_light")


traffic_light_color = "Red"


regulation_traffic_light.color.append(traffic_light_color)


intersection = Intersection("intersection_1")
connector = Connector("connector_1")

intersection.contains_traffic_light.append(regulation_traffic_light)


intersection.has_conflicting_connector.append(connector)


with onto:


    rule_traffic_light_intersection = Imp(namespace=onto)
    rule_traffic_light_intersection.set_as_rule("""
        Intersection(?intersection),
        contains_traffic_light(?intersection, ?traffic_light),
        color(?traffic_light, "Red"),
        has_conflicting_connector(?intersection, ?connector)
        -> 
        has_to_wait_for_traffic_light(?connector, ?traffic_light)
    """)


sync_reasoner_pellet(infer_property_values=True, infer_data_property_values=True)


instances_with_wait_property = list(onto.search(has_to_wait_for_traffic_light = "*"))


for instance in instances_with_wait_property:
    print("Connector:", instance.name, "has to wait for traffic light:", instance.has_to_wait_for_traffic_light)