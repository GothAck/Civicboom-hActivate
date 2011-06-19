import math

R = 6371

def distance(lon1,lat1,lon2,lat2):
    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)
    
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    a = ( math.sin(dlat/2) * math.sin(dlat/2) ) +\
        math.cos(lat1) * math.cos(lat2) *\
        ( math.sin(dlon/2) * math.sin(dlon/2) )
    c = math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = R * c
    return d
    
def dict_overlay(o, params):
    for (key,value) in params.iteritems():
        # Convert types if needed
        if hasattr(0,key):
            if isinstance(getattr(o,key), float):
                value = float(value)
            if isinstance(getattr(o,key), int):
                value = int(value)
            try:
                setattr(o, key, value)
            except:
                pass # if we cant set it, sod it
    