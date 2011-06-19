import math

def distance(x1,y1,x2,y2):
    x_diff = math.fabs(x1-x2)
    y_diff = math.fabs(y1-y2)
    
    return math.sqrt(math.pow(x_diff,2) + math.pow(y_diff,2))