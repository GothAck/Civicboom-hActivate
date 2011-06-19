from hactivate.lib.base import *

class ItemController(BaseController):
    """
    """

    def view_items(self):
        c.items = get_items()
        return render('view_items.mako')
        
    def view_item(self, id):
        c.item = get_item(id)
        return render('view_item.mako')
        
    def view_user(self, id):
        c.user = get_user(id)
        return render('view_user.mako')

    # ----------------------------------------------------------

    def new_item(self):
        # Render input form if needed
        if not request.params:
            return render('new_item.mako')
        
        # Default params
        if 'user_id' not in request.params:
            request.params['user_id'] = c.logged_in_user.id
        
        # Create new item
        item = Item()
        for (key,value) in request.params.iteritems():
            # Convert types if needed
            if isinstance(getattr(item,key), float):
                value = float(value)
            if isinstance(getattr(item,key), int):
                value = int(value)
            setattr(item, key, value)
        # insert into db
        Session.add(item)
        Session.commit()
        
        # trigger all search table to match
        #   send alerts to users contacts in search
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
    
    def user_msg(user_id, message):
        pass
        # send message to user
    
    # ----------------------------------------------------------

    def delete_item(self, item_id):
        # set status to closed
        pass

    def new_search(self):
        pass
    