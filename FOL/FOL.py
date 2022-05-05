data = {
    'SRK': {
        'Hits': 45,
        'Flops': 18,
        'Awards': 20,
        'Fans': 35,
        'NetWorth': 600
    },
    'Amitabh Bacchan': {
        'Hits': 50,
        'Flops': 5,
        'Awards': 19,
        'Fans': 42,
        'NetWorth': 400
    },
    'Amir Khan': {
        'Hits': 39,
        'Flops': 6,
        'Awards': 16,
        'Fans': 30,
        'NetWorth': 500
    },
    'Ranbir Kapoor': {
        'Hits': 30,
        'Flops': 20,
        'Awards': 15,
        'Fans': 40,
        'NetWorth': 320
    },
    'ideal': {
        'Hits': 40,
        'Flops': 8,
        'Awards': 15,
        'Fans': 40,
        'NetWorth': 350
    },
}


def hits(hits):
    return hits > data['ideal']['Hits']


def flops(flops):
    return flops < data['ideal']['Flops']


def popularity(awards, fans):
    return awards > data['ideal']['Awards'] and fans > data['ideal']['Fans']


def networth(networth):
    return networth > data['ideal']['NetWorth']


def isBestActor(actor):
    if hits(data[actor]['Hits']) and flops(data[actor]['Flops']) and popularity(data[actor]['Awards'],
                                                                                data[actor]['Fans']) and networth(
            data[actor]['NetWorth']):
        return True

    return False


def getBestActor():
    for i in data:
        if i == 'ideal':
            continue
        if isBestActor(i):
            print(i, " is the greatest actor. ")


getBestActor()
