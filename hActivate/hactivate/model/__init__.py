"""The application's model objects"""
from hactivate.model.meta import Session, Base

from hactivate.model.declarative_objects import *

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)
