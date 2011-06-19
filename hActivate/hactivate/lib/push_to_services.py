import json, httplib


def freeminder(item):
    #http://www.free-minder.org/rest/offer
    
    if not item:
        return False
    
    body = json.dumps({
        'sender'       : item.user.username ,
        'groupID'      : 'FreeHoc'          ,
        'location_name': 'not implemented'  ,
        'location_lat' : str(item.lat)      ,
        'location_lon' : str(item.lon)      ,
        'title'        : item.title         ,
        'message'      : item.description   ,
        'item_id'      : str(item.id)       ,
    })
    
    print body
    
    connection = httplib.HTTPConnection("www.free-minder.org")
    headers = {'Content-Type': 'application/json'}
    connection.request("POST", "http://www.free-minder.org/rest/offer" ,headers=headers, body=body)
    
    resp = connection.getresponse()
    data = resp.read()
    
    print data, resp.status, resp.reason
    return resp.status==201