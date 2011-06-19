import math

def distance(x1,y1,x2,y2):
    x_diff = math.fabs(x1-x2)
    y_diff = math.fabs(y1-y2)
    
    return math.sqrt(math.pow(x_diff,2) + math.pow(y_diff,2))
    
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
    