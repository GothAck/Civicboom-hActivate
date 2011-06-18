from civicboom.model.declarative_objects  import *

from civicboom.model.meta import Session


def get_user(user):
    if isinstance(user, User):
        return user
    try:
        return Session.query(User).filter_by(username=user).one()
    except NoResultFound:
        pass
    return None


def get_item(item):
    if isinstance(user, Item):
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
