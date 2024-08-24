from owlready2 import Thing, get_ontology

onto = get_ontology(r"updated_onto.owl").load()

class Network(Thing):
    namespace = onto
    pass


class Edge(Network):
    namespace = onto
    pass

class Way(Edge):
    namespace = onto
    pass


class Aerialway(Way):
    namespace = onto
    pass

class CableCar(Aerialway):
    namespace = onto
    pass

class Gondola(Aerialway):
    namespace = onto
    pass

class MixedLift(Aerialway):
    namespace = onto
    pass

class ChairLift(Aerialway):
    namespace = onto
    pass

class DragLift(Aerialway):
    namespace = onto
    pass

class TBar(Aerialway):
    namespace = onto
    pass

class JBar(Aerialway):
    namespace = onto
    pass

class Platter(Aerialway):
    namespace = onto
    pass

class RopeTow(Aerialway):
    namespace = onto
    pass

class MagicCarpet(Aerialway):
    namespace = onto
    pass

class ZipLine(Aerialway):
    namespace = onto
    pass

class GoodsAerialway(Aerialway):
    namespace = onto
    pass

class Pylon(Aerialway):
    namespace = onto
    pass

class Station(Aerialway):
    namespace = onto
    pass

















class Aeroway(Way):
    namespace = onto
    pass 

class Aerodrome(Aeroway):
    namespace = onto
    pass

class AircraftCrossing(Aeroway):
    namespace = onto
    pass

class Apron(Aeroway):
    namespace = onto
    pass

class Gate(Aeroway):
    namespace = onto
    pass

class Hangar(Aeroway):
    namespace = onto
    pass

class Helipad(Aeroway):
    namespace = onto
    pass

class Heliport(Aeroway):
    namespace = onto
    pass

class NavigationAid(Aeroway):
    namespace = onto
    pass

class Runway(Aeroway):
    namespace = onto
    pass

class Spaceport(Aeroway):
    namespace = onto
    pass

class Taxiway(Aeroway):
    namespace = onto
    pass

class Terminal(Aeroway):
    namespace = onto
    pass

class Windsock(Aeroway):
    namespace = onto
    pass





class Highway(Way):
    namespace = onto
    pass 

class Motorway(Highway):
    namespace = onto
    pass

class Trunk(Highway):
    namespace = onto
    pass

class Primary(Highway):
    namespace = onto
    pass

class Secondary(Highway):
    namespace = onto
    pass

class Tertiary(Highway):
    namespace = onto
    pass

class Unclassified(Highway):
    namespace = onto
    pass

class Residential(Highway):
    namespace = onto
    pass

class MotorwayLink(Highway):
    namespace = onto
    pass

class TrunkLink(Highway):
    namespace = onto
    pass

class PrimaryLink(Highway):
    namespace = onto
    pass

class SecondaryLink(Highway):
    namespace = onto
    pass

class TertiaryLink(Highway):
    namespace = onto
    pass

class LivingStreet(Highway):
    namespace = onto
    pass

class Service(Highway):
    namespace = onto
    pass

class Pedestrian(Highway):
    namespace = onto
    pass

class Track(Highway):
    namespace = onto
    pass

class BusGuideway(Highway):
    namespace = onto
    pass

class Escape(Highway):
    namespace = onto
    pass

class Raceway(Highway):
    namespace = onto
    pass

class UnknownRoadType(Highway):
    namespace = onto
    pass

class Busway(Highway):
    namespace = onto
    pass

class Footway(Highway):
    namespace = onto
    pass

class Bridleway(Highway):
    namespace = onto
    pass

class Steps(Highway):
    namespace = onto
    pass

class Corridor(Highway):
    namespace = onto
    pass

class Path(Highway):
    namespace = onto
    pass

class ViaFerrata(Highway):
    namespace = onto
    pass

class Cycleway(Highway):
    namespace = onto
    pass








class Railway(Way):
    namespace = onto
    pass 

class Abandoned(Railway):
    namespace = onto
    pass

class Construction(Railway):
    namespace = onto
    pass

class Disused(Railway):
    namespace = onto
    pass

class Funicular(Railway):
    namespace = onto
    pass

class Light(Railway):
    namespace = onto
    pass

class Miniature(Railway):
    namespace = onto
    pass

class Monorail(Railway):
    namespace = onto
    pass

class NarrowGauge(Railway):
    namespace = onto
    pass

class Preserved(Railway):
    namespace = onto
    pass

class FullSize(Railway):
    namespace = onto
    pass

class Subway(Railway):
    namespace = onto
    pass

class Tram(Railway):
    namespace = onto
    pass





class Waterway(Way):
    namespace = onto    
    pass

class River(Waterway):
    namespace = onto
    pass

class Riverbank(Waterway):
    namespace = onto
    pass

class Stream(Waterway):
    namespace = onto
    pass

class TidalChannel(Waterway):
    namespace = onto
    pass

class Canal(Waterway):
    namespace = onto
    pass

class Drain(Waterway):
    namespace = onto
    pass

class Ditch(Waterway):
    namespace = onto
    pass

class PressurisedWaterway(Waterway):
    namespace = onto
    pass

class Fairway(Waterway):
    namespace = onto
    pass







class Lane(Edge):
    namespace = onto
    pass

class Emissions(Edge):
    namespace = onto
    pass


class Pollution(Emissions):
    namespace = onto
    pass



class Noise(Emissions):
    namespace = onto
    pass

class Consumption(Edge):
    namespace = onto
    pass



def create_edge_instance(edge):
    instances = []
    edge_type = str(edge.getType()).split(".")[1].capitalize()
    #tram word both in edges and vehicles, so dynamic object creation have some problems with that.
    if "tram" in edge_type:
        pass
    try:
        if "|" in edge_type:
            #Parsing cycleway and unclassifed for cycleway.lane|highway.unclassified
            first_edge_type = str(str(edge.getType()).split("|")[0]).split(".")[0].capitalize()
            second_edge_type = str(str(edge.getType()).split("|")[1]).split(".")[1].capitalize()
            first_edge_class = globals()[first_edge_type]
            second_edge_class = globals()[second_edge_type]

            instances.append(first_edge_class(edge.getID()))
            instances.append(second_edge_class(edge.getID()))

        elif edge_type in globals():
                
                edge_class = globals()[edge_type]
                instances.append(edge_class(edge.getID()))

        elif edge_type not in globals():
            pass
    except ValueError:
        pass

    return instances



onto.save(file=r"updated_onto.owl")
