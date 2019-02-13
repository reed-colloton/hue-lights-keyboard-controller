import pynput


from lights_controller import toggle_group, light_set, light_brightness
from config import Selection_Url, State


# starting default
selection = Selection_Url.desk


def key_pressed(key):
    print(str(key))
    """responds to calls from the listener with the defined action"""

    # coverts pynput object to string
    try:
        # if alphanumeric key
       keycode = str(key.char).replace('Key.','') # deletes from beginning of string FYI
    except AttributeError:
        # if modifyer/special key
        keycode = str(key).replace('Key.','')

    global selection

    # toggle on/off current group
    if keycode == "enter":
        toggle_group(selection=selection)

    # sets group
    elif keycode == "insert": selection = Selection_Url.bedroom
    elif keycode == "delete": selection = Selection_Url.desk
    elif keycode == "tab": selection = Selection_Url.every

    # brightness control
    elif keycode == "+": light_brightness(selection=selection, direction="down") # plus and minus are flipped b/c on keypad they are 
    elif keycode == "-": light_brightness(selection=selection, direction="up")

    # set light state/scene/hue
    elif keycode == "3" or keycode == "page_down": light_set(selection=selection, data=State.relax)
    elif keycode == "2" or keycode == "down": light_set(selection=selection, data=State.read)
    elif keycode == "1" or keycode == "end": light_set(selection=selection, data=State.concentrate)


def main_listener():
    """"pynput keyboard listener- calls function key_pressed with keycode when key is pressed"""
    print("\nStarting rpi-lights keyboard listener...")
    try:
        with pynput.keyboard.Listener(on_press=key_pressed) as listener:
            listener.join()
    except KeyboardInterrupt:
        # so it doesn't show ugly errors when it quits
        print("\n\nSHUTDOWN WITH CTRL-C\n")
