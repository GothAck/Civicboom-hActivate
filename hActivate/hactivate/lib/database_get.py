from hactivate.model.declarative_objects  import *

from hactivate.model.meta import Session

from sqlalchemy.orm.exc import NoResultFound

def get_user(user):
    if isinstance(user, User):
        return user
    try:
        return Session.query(User).filter_by(username=user).one()
    except NoResultFound:
        pass
    return None


def get_item(item):
    if isinstance(item, Item):
        return item
    try:
        return Session.query(Item).filter_by(id=item).one()
    except NoResultFound:
        pass
    return None


def get_items():
    try:
        return Session.query(Item).all()
    except NoResultFound:
        pass
    return []