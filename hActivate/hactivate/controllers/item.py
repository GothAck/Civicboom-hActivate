from hactivate.lib.base import *

from hactivate.model.declarative_objects import *

from hactivate.lib.misc    import dict_overlay
from hactivate.lib.helpers import distance

from hactivate.lib.comms import notify

import hactivate.lib.push_to_services

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

    @auth
    def new_item(self):
        # Render input form if needed
        if not request.params:
            return render('new_item.mako')
        
        params = dict(request.params)
        
        # Create new item
        item = Item()
        item.user = c.logged_in_user
        dict_overlay(item, params)
        
        # insert into db
        Session.add(item)
        Session.commit()
        
        # Push top external services
        if c.logged_in_user.username != 'elroid':
            hactivate.lib.push_to_services.freeminder(item)
        
        # trigger all search table to match
        #   send alerts to users contacts in search
        for search in get_searchs():
            print search.keywords
            keywords = search.keywords.split(',')
            for keyword in keywords:
                #print "searching for keyword %s in %s" % ( keyword , item.description )
                if keyword in item.description:
                    #print "distance from %s to %s" % ( search.lon , item.lon )
                    d = distance(search, item)
                    print d, search.radius
                    if d < search.radius:
                        # search.user.notify('')
                        print "alert %s to %s" % (search.user.username, item.title)
                        notify(search.user, "New item found: %s" % (item.title))
        
        return redirect(url(controller='item', action='view_item', id=item.id))
    
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
        get_item(item_id)
        if item.user != c.logged_in_user:
            set_flash('you are not the item owner')
        else:
            # set status to closed
            item.status = 'closed'
            #Session.delete()
            Session.commit()
            set_flash('item deleted')
        return redirect('/')

    @auth
    def new_search(self):
        if not request.params:
            return render('new_search.mako')
        
        params = dict(request.params)
        if 'radius' not in params:
            params['radius'] = '0.01'
        # Delete black lon lats so it defaults to user location is missing
        if 'lon' in params and not params.get('lon'):
            del params['lon']
        if 'lat' in params and not params.get('lat'):
            del params['lat']
        
        search = UserSearch()
        dict_overlay(search, params)
        c.logged_in_user.searchs.append(search)
        
        Session.commit()
        
        set_flash('added search %s' % search.keywords)
        return redirect(url(controller='item', action='view_user', id=c.logged_in_user.username))