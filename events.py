import random
from utils import separator

EVENTS = [
    {
        "Name" : "Deszcz meteorytów",
        "Desc" : "W twój statek uderzają meteoryty!\n│(-15 integralności.)",
        "ShipDebuff" : {"integrity" : -15}
    },
    {
        "Name" : "Wiatr słoneczny",
        "Desc" : "Twój statek wpadł w wiatr słoneczny!\n│(+20 energii.)",
        "ShipDebuff" : {"energy" : 20}
    }
]

def announce_event(event):
    print(separator())
    print(f"├WYDARZENIE: {event['Name'].upper()}")
    print(f"├{event['Desc']}")
    print(separator())


def pick_event(vehicle):
    random_event = EVENTS[random.randint(0,len(EVENTS)-1)]

    debuff = random_event.get('ShipDebuff', {})

    for stat, value in debuff.items():
        current = getattr(vehicle, stat, 0)
        setattr(vehicle, stat, current + value)


    return random_event