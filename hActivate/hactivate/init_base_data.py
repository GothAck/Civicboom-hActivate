from hactivate.model.declarative_objects import *
from hactivate.model.meta import Session


import logging
log = logging.getLogger(__name__)

def init_base_data():
        log.info("Populating tables with base test data")
        
        u1 = User()
        u1.username      = u"test"
        u1.name          = "TES MONKEY MAN"

        Session.add_all([u1])
        Session.commit()
