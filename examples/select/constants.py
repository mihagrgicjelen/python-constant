from py_constant import Constant


class AircraftType(Constant):
    GLIDER = 'glider'
    BALOON = 'baloon'
    MILITARY = 'military'
    CARGO_JET = 'cargo_jet'
    PASSENGER_JET = 'passenger_jet'
    ROTORCRAFT = 'rotorcraft'

    _titles = {
        GLIDER: 'Glider',
        BALOON: 'Air baloon',
        MILITARY: 'Military aircraft',
        CARGO_JET: 'Cargo jet',
        PASSENGER_JET: 'Passenger jet',
        ROTORCRAFT: 'Rotorcraft',
    }

    _descriptions = {
        GLIDER: 'Lightweight aircrafts with no propulsion',
        BALOON: 'Big plastic bag like objects, filled with hot air.',
        MILITARY: 'Aircrafts designed to do harm to other people :(',
        CARGO_JET: 'Aircrafts designed to carry as much stuff as possible',
        PASSENGER_JET: 'Aircrafts that carry people. Maybe animals and some stuff too',
        ROTORCRAFT: 'Aircrafts which have (usually) two rotors, keeping them in the air, a.k.a helicopters'
    }
