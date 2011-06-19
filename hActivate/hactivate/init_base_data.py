from hactivate.model.declarative_objects import *
from hactivate.model.meta import Session


import logging
log = logging.getLogger(__name__)

def init_base_data():
        log.info("Populating tables with base test data")
        
        u1 = User()
        u1.username      = u"test"
        u1.name          = "TES MONKEY MAN"
        
        u2 = User()
        u2.username      = u"elroid"
        u2.name          = "Elliot Test"
        
        Session.add_all([u1,u2])
        Session.commit()
        
        # -- Items ---
        
        i1 = Item()
        #i1.user_id              = 1
        i1.title                = "Bike Seat"
        i1.description          = "You sit on it"
        i1.item_type            = "item"
        i1.direction_type       = "offer"
        i1.lon                  = 0.0
        i1.lat                  = 0.0
        u1.items.append(i1)
        
        i0 = Item()
        #i0.user_id              = 1
        i0.title                = "Necromicon"
        i0.description          = "Don't read it"
        i0.item_type            = "item"
        i0.direction_type       = "offer"
        i0.lon                  = 1.0
        i0.lat                  = 1.0
        u1.items.append(i0)
        
        # -- Searchs ---
        
        s1 = UserSearch()
        s1.raduis = 1
        s1.lon =  -0.120335
        s1.lat =  51.532255
        s1.keywords = "bike"
        u1.searchs.append(s1)
        
        s1 = UserSearch()
        s1.raduis = 1
        s1.lon =  -0.133188
        s1.lat =  51.539662
        s1.keywords = "ladder"
        u1.searchs.append(s1)
        
        #Session.add_all([i1, i0])
        Session.commit()
