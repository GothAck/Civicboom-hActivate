from hactivate.lib.base import *

class ItemController(BaseController):
    """
    """
    
    def create_item(self):
        # insert into DB
        # trigger all search table to match
        #   send alerts to users contacts in search
        pass
    
    def delete_item(self, item_id):
        # set status to closed
        pass
    
    def request(self, item_id):
        # im interested in item
        # send deatils top item owner
        pass
    
    def acknollege_request(self, item_id, user_id):
        # Swap contact details with item owner and requestee
        pass
    
    def feedback(self, item_id, user_id, rating, comment, status): # open/close
        # store feedback
        # close item if needed
        pass