"""The base Controller API

Provides the BaseController class for subclassing.
"""
from pylons.controllers import WSGIController
from pylons.templating import render_mako as render
from pylons import request, tmpl_context as c, session, url
from pylons.controllers.util  import redirect

from decorator import decorator

from hactivate.model.meta import Session

from hactivate.lib.database_get import *

def set_flash(message):
    session['flash'] = message
    session.save()

@decorator
def auth(target, *args, **kwargs):
    if not c.logged_in_user:
        if 'user_id' in request.params:
            c.logged_in_user = get_user(request.params['user_id'])
        else:
            set_flash('please login')
            redirect('/')
            
    result = target(*args, **kwargs) # Execute the wrapped function

    return result


class BaseController(WSGIController):

    def __before__(self):
        # Login from session
        c.logged_in_user = None
        if 'user' in session:
            c.logged_in_user = get_user(session['user'])
            
        # Flash message
        c.flash = None
        if session.has_key('flash'):
            c.flash = session.get('flash')
            del session['flash']
            session.save()

    def __call__(self, environ, start_response):
        """Invoke the Controller"""
        # WSGIController.__call__ dispatches to the Controller method
        # the request is routed to. This routing information is
        # available in environ['pylons.routes_dict']
        try:
            return WSGIController.__call__(self, environ, start_response)
        finally:
            Session.remove()
