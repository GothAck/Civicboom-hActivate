from hactivate.lib.base import *

class TestController(BaseController):
    """
    """
    def test(self):
        return render("test.mako")