from hactivate.lib.base import *

class AccountController(BaseController):
    """
    """
    def signin(self):
        if request.environ['REQUEST_METHOD'] == 'GET':
            return render("signin.mako")
        
        #perform signin        
        return "signing in as %s" % request.params['username']
        #redirect to ???
    
    def signout(self):
        # clear session
        pass