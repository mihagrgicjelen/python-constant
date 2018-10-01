# python-constant
General purpose Constant class for Python apps


```python
from py_constant import Constant

class Aircraft():

    def __init__(brand, model, type):
        pass
        ...

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


class AircraftPartCategory(Constant):
    EXTERIOR = 'exterior'
    INTERIOR = 'interior'
    ENGINE = 'engine'
    ELECTRONICS = 'electronics'
    HYDRAULICS = 'hydraulics'


helicopter = Aircraft(
    brand='Sikorsky',
    model='MH-60 Seahawk',
    type=AircraftType.ROTORCRAFT
)

jet = Aircraft(
    brand='Boeing',
    model='777-300',
    type=AircraftType.PASSENGER_JET
)

```


```python

class AircraftCreate(View):

    def post(self, request, *args, **kwargs):

        if request.POST['aircraft_type'] not in AircraftType.get_all():
            raise ValueError('Invalid aircraft type "%s". Should be one of %s' % (
                request.POST['aircraft_type'], AircraftType.get_all()))
        ...            

```


