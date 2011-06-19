from hactivate.model.meta import Base

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Unicode, UnicodeText, String
from sqlalchemy import Enum, Integer, DateTime, Boolean, Float
#from geoalchemy import GeometryColumn, Point, GeometryDDL
from sqlalchemy import and_, or_, func
from sqlalchemy.orm import relationship, backref
#from sqlalchemy.schema import DDL



_item_types         = Enum("item", "knowledge", "service", name="item_types")
_item_statuss       = Enum("open", "closed",              name="contact_statuss")
_direction_types    = Enum("offer", "wanted",             name="direction_types")
_contact_types      = Enum("twitter", "email", "sms",     name="contact_types")
_contact_directions = Enum("in","out",                    name="contact_direction_types")


class Item(Base):
    """
    """
    __tablename__   = "item"

    id          = Column(Integer(),        primary_key=True)
    user_id     = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
    
    status      = Column(_item_statuss ,  nullable=False, default="open" )
    
    title       = Column(Unicode(250),     nullable=False, default=u"Untitled")
    description = Column(Unicode(250),     nullable=False, default=u"")
    
    item_type      = Column(_item_types     ,  nullable=False, default="item" )
    direction_type = Column(_direction_types,  nullable=False, default="offer")

    lon = Column(Float(),nullable=False, default=0) #? nullable?
    lat = Column(Float(),nullable=False, default=0)

    requests = relationship("ItemRequest"  , backref=backref('item'), cascade="all,delete-orphan")

class ItemRequest(Base):
    __tablename__   = "item_request"
    # Composite key
    item_id     = Column(Integer(),     ForeignKey('item.id'),  nullable=False, primary_key=True)
    user_id     = Column(Integer(),     ForeignKey('user.id'),  nullable=False, primary_key=True)
    # will have fields item and user from backrefs



class User(Base):
    __tablename__   = "user"
    id              = Column(Integer(),      primary_key=True)
    username        = Column(String(32), nullable=False, unique=True, index=True)
    name            = Column(Unicode(250),   nullable=False, default=u"")
    join_date       = Column(DateTime(),     nullable=False, default=func.now())
    
    home_lon  = Column(Float())
    home_lat  = Column(Float())
    home_text = Column(Unicode(250),   nullable=False, default=u"") # Created from reverse geocode
    
    #feedback_score = Column(Integer(), nullable=False, default=0, doc="Controlled by trigger") # TODO!!! # AllanC - short term can create a @property to fake this by actually pulling all fedback records and processing

    searchs  = relationship("UserSearch"          , backref=backref('user'), cascade="all,delete-orphan")
    contacts = relationship("UserContact"         , backref=backref('user'), cascade="all,delete-orphan")
    feedback = relationship("UserFeedback"        , backref=backref('user'), cascade="all,delete-orphan")

    requests = relationship("ItemRequest"         , backref=backref('user'), cascade="all,delete-orphan")
    items    = relationship("Item"                , backref=backref('user'), cascade="all,delete-orphan")

    @property
    def feedback_score(self):
        return 0
    
    def notify(self):
        from hactivate.lib.comms import notify
        notify(self)

class UserSearch(Base):
    __tablename__   = "user_search"
    id              = Column(Integer(),      primary_key=True)
    user_id         = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
    
    radius          = Column(Float(),nullable=False, default=0)
    lon             = Column(Float()) # optional
    lat             = Column(Float()) # optional - will use home_### if no location given
    
    keywords        = Column(Unicode(50),     nullable=False, default=u"") # comma serparated list of search words

    

class UserContact(Base):
    __tablename__   = "user_contact"
    id              = Column(Integer(),      primary_key=True)
    user_id         = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
    contact_type    = Column(_contact_types,  nullable=False)
    data            = Column(Unicode(250),    nullable=False)
    #data_id         = Column(Unicode(250),    nullable=True,        index=True)
    contact_direction_type = Column(_contact_directions,  nullable=False) # in or out


class UserFeedback(Base):
    __tablename__   = "user_feedback"
    id              = Column(Integer(),      primary_key=True) # Composite key????
    item_id         = Column(Integer(),     ForeignKey('item.id'),  nullable=False, index=True)
    user_id         = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
   
    rating          = Column(Integer()   , nullable=False, default=0)
    comment         = Column(Unicode(250), nullable=False, default=u"")
