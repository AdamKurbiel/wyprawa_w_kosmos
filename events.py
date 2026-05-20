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
    },
    {
        "Name": "Grawitacyjna anomalia",
        "Desc": "Twój statek zostaje wciągnięty w zaburzenie grawitacyjne!\n│(-10 energii, przesunięcie losowe).",
        "ShipDebuff": {"energy": -10},
        "ExtraEffect": "teleport"
    },
    {
        "Name": "Odkrycie złomu kosmicznego",
        "Desc": "Znajdujesz dryfujący złom, który wzmacnia kadłub!\n│(+10 integralności).",
        "ShipDebuff": {"integrity": 10}
    }
]

def announce_event(event):
    print(separator())
    print(f"├WYDARZENIE: {event['Name'].upper()}")
    print(f"├{event['Desc']}")
    print(separator())


def pick_event(vehicle, world):
    random_event = EVENTS[random.randint(0,len(EVENTS)-1)]

    debuff = random_event.get('ShipDebuff', {})

    for stat, value in debuff.items():
        current = getattr(vehicle, stat, 0)
        setattr(vehicle, stat, current + value)
    
    if random_event.get("ExtraEffect") == "teleport":
        dx =  random.randint(-10,10)
        dy = random.randint(-10,10)

        vehicle.x += dx
        vehicle.y += dy

        vehicle.x = max(-world.size, min(world.size, vehicle.x)) 
        vehicle.y = max(-world.size, min(world.size, vehicle.y))


    return random_event