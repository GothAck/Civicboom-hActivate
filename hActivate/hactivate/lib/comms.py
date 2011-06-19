'''
Created on 19 Jun 2011

@author: greg
'''

from hactivate.lib.oauth import sendSMS

from hactivate.model.declarative_objects  import *

from hactivate.model.meta import Session

from sqlalchemy.orm.exc import NoResultFound

def notify(user, text):
    contacts = Session.query(UserContact).filter(UserContact.user_id==user.id).all()
    for contact in contacts:
        if contact.contact_type == 'sms':
            sendSMS(contact.data, text)
    pass