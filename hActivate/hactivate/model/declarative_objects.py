from hactivate.model.meta import Base

from sqlalchemy import Column, ForeignKey
from sqlalchemy import Unicode, UnicodeText, String
from sqlalchemy import Enum, Integer, DateTime, Boolean, Float
#from geoalchemy import GeometryColumn, Point, GeometryDDL
from sqlalchemy import and_, or_, func
from sqlalchemy.orm import relationship, backref
#from sqlalchemy.schema import DDL


# ENUM Example _content_type = Enum("comment", "draft", "article", "assignment", "syndicate", name="content_type")

_item_types      = Enum("item", "knwolege", "service", name="item_types")
_direction_types = Enum("offer", "wanted", name="direction_types")
_contact_types   = Enum("twitter", "email", "sms", name="contact_types")
_contact_directions = Enum("in","out", name="contact_direction_types")


class Item(Base):
    """
    """
    __tablename__   = "item"

    id          = Column(Integer(),        primary_key=True)
    user_id     = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
    
    title       = Column(Unicode(250),     nullable=False, default=u"Untitled")
    description = Column(Unicode(250),     nullable=False, default=u"")
    
    item_type      = Column(_item_types     ,  nullable=False, default="item" )
    direction_type = Column(_direction_types,  nullable=False, default="offer")

    lon = Column(Float(),nullable=False, default=0) #? nullable?
    lat = Column(Float(),nullable=False, default=0)


class User(Base):
    __tablename__   = "user"
    id              = Column(Integer(),      primary_key=True)
    username        = Column(String(32), nullable=False, unique=True, index=True)
    name            = Column(Unicode(250),   nullable=False, default=u"")
    join_date       = Column(DateTime(),     nullable=False, default=func.now())
    
    home_lon  = Column(Float())
    home_lat  = Column(Float())
    home_text = Column(Unicode(250),   nullable=False, default=u"") # Created from reverse geocode


class UserSearch(Base):
    __tablename__   = "user_search"
    id              = Column(Integer(),      primary_key=True)
    user_id         = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
    
    raduis          = Column(Float(),nullable=False, default=0)
    lon             = Column(Float()) # optional
    lat             = Column(Float()) # optional - will use home_### if no location given
    
    keywords        = Column(Unicode(50),     nullable=False, default=u"") # comma serparated list of search words


class UserContact(Base):
    __tablename__   = "user_contact"
    id              = Column(Integer(),      primary_key=True)
    user_id         = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
    contact_type    = Column(_contact_types,  nullable=False)
    data            = Column(Unicode(250),    nullable=False)
    contact_direction_type = Column(_contact_directions,  nullable=False) # in or out


class UserFeedback(Base):
    __tablename__   = "user_feedback"
    id              = Column(Integer(),      primary_key=True)
    item_id         = Column(Integer(),     ForeignKey('item.id'),  nullable=False, index=True)
    user_id         = Column(Integer(),     ForeignKey('user.id'),  nullable=False, index=True)
    
    rating          = Column(Integer()   , nullable=False, default=0)
    comment         = Column(Unicode(250), nullable=False, default=u"")
