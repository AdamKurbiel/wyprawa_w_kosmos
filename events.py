import random

EVENTS = [
    {
        "Name" : "Deszcz meteorytów",
        "Desc" : "Lorem ipsum"
    },
    {
        "Name" : "Wiatr słoneczny",
        "Desc" : "Lorem ipsum"
    }
]

def announce_event(event):
    print("\n===WYDARZENIE:===")
    print(event['Name'].upper())
    print(event['Desc'])
    print("=================\n")


def pick_event():
    random_event = EVENTS[random.randint(0,len(EVENTS)-1)]
    announce_event(random_event)
    return random_event

pick_event()