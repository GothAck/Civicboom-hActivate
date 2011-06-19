from hactivate.lib.base import *

class AccountController(BaseController):
    """
    """
    def signin(self):
        if request.environ['REQUEST_METHOD'] == 'GET':
            return render("signin.mako")
        
        username = request.params.get('username')
        if username:
            if not get_user(username):
                set_flash('failed signin')
            else:
                session['user'] = username
                session.save()
                set_flash('signed in as %s' % username)
        
        return redirect('/')
    
    def signout(self):
        try:
            session['user'] = request.params.get('username')
            session.save()
        except:
            pass
        return redirect('/')