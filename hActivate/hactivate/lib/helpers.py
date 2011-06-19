"""Helper functions

Consists of functions to typically be used within templates, but also
available to Controllers. This module is available to templates as 'h'.
"""
# Import helpers as desired, or define your own, ie:
#from webhelpers.html.tags import checkbox, password

from hactivate.lib.misc import distance as _distance

def distance(a,b):
    def get_lon_lat(o):
        try:
            return (getattr(o,lon), getattr(o,lat))
        except:
            # bit of a hack, if no lon/lat - look for user parent to get lon lat from
            try:
                return get_lon_lat(getattr(o,user))
            except:
                return (0,0)
    a = get_lon_lat(a)
    b = get_lon_lat(b)
    return _distance(a[0],a[1],b[0],b[1])