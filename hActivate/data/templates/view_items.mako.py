# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308476325.993034
_template_filename='/home/greg/Civicboom-hActivate/hActivate/hactivate/templates/view_items.mako'
_template_uri='view_items.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['body']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'html_base.mako', _template_uri)
def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n')
        # SOURCE LINE 2
        import json 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['json'] if __M_key in __M_locals_builtin_stored]))
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        float = context.get('float', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 4
        __M_writer(u'\n    <script type="text/javascript">\n    var itemArray = new Array();\n    var map;\n    \n')
        # SOURCE LINE 9
        for item in c.items:
            # SOURCE LINE 10
            __M_writer(u'        itemArray[')
            __M_writer(escape(item.id))
            __M_writer(u'] = {\n            id: ')
            # SOURCE LINE 11
            __M_writer(escape(item.id))
            __M_writer(u',\n            uid:    ')
            # SOURCE LINE 12
            __M_writer(escape(item.user_id))
            __M_writer(u',\n            status: "')
            # SOURCE LINE 13
            __M_writer(escape(item.status))
            __M_writer(u'",\n            title:  "')
            # SOURCE LINE 14
            __M_writer(escape(item.title))
            __M_writer(u'",\n            description:    "')
            # SOURCE LINE 15
            __M_writer(escape(item.description))
            __M_writer(u'",\n            type:   "')
            # SOURCE LINE 16
            __M_writer(escape(item.item_type))
            __M_writer(u'",\n            direction:  "')
            # SOURCE LINE 17
            __M_writer(escape(item.direction_type))
            __M_writer(u'",\n            lat:    ')
            # SOURCE LINE 18
            __M_writer(escape(float(item.lat)))
            __M_writer(u',\n            lon:    ')
            # SOURCE LINE 19
            __M_writer(escape(float(item.lon)))
            __M_writer(u',\n        };\n')
            pass
        # SOURCE LINE 22
        __M_writer(u'\n    $(document).ready(function() {\n        var latlng = new google.maps.LatLng(0.0, 0.0);\n        \n        var myOpts = {\n            zoom: 8,\n            center: latlng,\n            mapTypeId: google.maps.MapTypeId.ROADMAP, // optons = ROADMAP, SATELLITE, HYBRID, TERRAIN\n        };\n        \n        map = new google.maps.Map(document.getElementById("map_canvas"), myOpts);\n    \n        for (var id in itemArray) {\n            item = itemArray[id];\n            ll = new google.maps.LatLng(item.lat, item.lon);\n            marker = new google.maps.Marker({\n                position: ll,\n                map: map,\n                title: id,\n                draggable: false,\n            });\n            add_listener(marker);\n            marker.setMap(map);\n        }\n        \n        \n    });\n    \n    function add_listener(marker) {\n        google.maps.event.addListener(marker, \'click\', function() {\n            populate_item(marker.title);\n        });\n    }\n    \n    function populate_item(id) {\n        item = itemArray[id];\n        content = "<b>Item ID</b><br />" + item.id +\n                    "<br /><b>User ID</b><br />" + item.uid +\n                    "<br /><b>Status</b><br />" + item.status +\n                    "<br /><b>Title</b><br />" + item.title +\n                    "<br /><b>Description</b><br />" + item.description +\n                    "<br /><b>Type</b><br />" + item.type +\n                    "<br /><b>Direction</b><br />" + item.direction;\n        canvas = $(\'#item_canvas\');\n        canvas.html(content);\n    }\n    </script>\n\n    <div id="menu">\n        <ul>\n            <li><a href="')
        # SOURCE LINE 72
        __M_writer(escape(url(controller='misc', action='titlepage')))
        __M_writer(u'">Home</a></li>\n            <li><a href="')
        # SOURCE LINE 73
        __M_writer(escape(url(controller='misc', action='test')))
        __M_writer(u'">Test</a></li>\n            <li><a href="')
        # SOURCE LINE 74
        __M_writer(escape(url(controller='item', action='view_items')))
        __M_writer(u'">View Items</a></li>\n            <li><a href="')
        # SOURCE LINE 75
        __M_writer(escape(url(controller='misc', action='test')))
        __M_writer(u'">Test</a></li>\n        </ul>\n    </div>\n    <div id="map_canvas"></div>\n    <div id="item_canvas"></div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


