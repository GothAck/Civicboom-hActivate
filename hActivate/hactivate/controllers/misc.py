from hactivate.lib.base import *

class MiscController(BaseController):
    """
    """
    def titlepage(self):
        return render("titlepage.mako")
    
    def test(self):
        return render("test.mako")