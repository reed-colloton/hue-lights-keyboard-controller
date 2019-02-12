
# hue bridge global constants for api
BRIDGE_USER = 'MK3jG8ecIDzlApeKfFRdCVqZsG5hBY7QG3XDSxjT'
BRIDGE_URL = 'http://192.168.1.94/api{}'.format(BRIDGE_USER)

class State:
    """data inputs for setting state of lights"""
    on = '{"on":true}'
    off = '{"on":false}'
    high = '{"on":true, "bri":254}'
    low  = '{"on":true, "bri":10}'
    relax = '{"hue": 7688,"sat": 199,"effect": "none","xy": [0.5014,0.4153],"ct": 447,"alert": "none","colormode": "ct"}'
    read = '{"hue":8595,"sat":121,"effect":"none","xy":[0.4452,0.4068],"ct":346,"alert":"none","colormode":"ct"}'
    concentrate = '{"hue":39392,"sat":13,"effect":"none","xy":[0.3691,0.3719],"ct":233,"alert":"none","colormode":"ct"}'


class Selection_Url:
    desk = '/groups/2/'
    bedroom = '/groups/1/'
    every = '/groups/0/'
