import requests


from config import BRIDGE_URL, Selection_Url, State


def light_is_on(selection):
    """returns true/false whether any light in the inputted group is on"""
    lights_status = requests.get(BRIDGE_URL+selection).json()["state"]["any_on"]
    return lights_status


def light_brightness(selection, direction):
    """gets current light brightness and sets the light to a higher or lower brightness"""
    # adds or subtracts 50 to brightness depending on arrow direction
    if direction == "down": brightness = requests.get(BRIDGE_URL+selection).json()["action"]["bri"] - 50
    elif direction == "up": brightness = requests.get(BRIDGE_URL+selection).json()["action"]["bri"] + 50
    else: print("Error")

    # makes sure brightness is within the allowed range of 1-254 inclusive
    if brightness < 1: brightness = 1
    elif brightness > 254:  brightness = 254
    # calls set light with brightness
    data = '{"bri":'+str(brightness)+'}'
    light_set(selection=selection, data=data)


def light_set(selection, data):
    """sets the chosen light group to the chosen state"""
    r = requests.put(BRIDGE_URL + selection+ 'action', data=data)
    # print("\nSetting {selection} lights to {data}...\n".format(selection=selection, data=data))


def toggle_group(selection):
    """toggles lights in selected group to opposite state"""
    if light_is_on(selection=selection): light_set(selection=selection, data=State.off)
    elif not light_is_on(selection=selection): light_set(selection=selection, data=State.on)
