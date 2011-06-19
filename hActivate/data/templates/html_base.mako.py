# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308477790.741705
_template_filename=u'/home/greg/Civicboom-hActivate/hActivate/hactivate/templates/html_base.mako'
_template_uri=u'html_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n\n    <head>\n        <link rel="stylesheet" type="text/css" href="/style/style.css" />\n        <script type="text/javascript" src="/javascript/jquery.js"></script>\n        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>\n        <title>FreeHoc</title>\n    </head>\n    \n    <body>\n\n        <div class="header">\n            \n        </div>\n\n        <div id="wrapper">\n            <div id="title_bar">\n                <a href="')
        # SOURCE LINE 18
        __M_writer(escape(url(controller='misc', action='titlepage')))
        __M_writer(u'"><img class="logo" src="/logo.png" /></a>\n')
        # SOURCE LINE 19
        if c.flash:
            # SOURCE LINE 20
            __M_writer(u'                <p class="flash_message">')
            __M_writer(escape(c.flash))
            __M_writer(u'</p>\n')
            pass
        # SOURCE LINE 22
        if c.logged_in_user:
            # SOURCE LINE 23
            __M_writer(u'                <p>Signed in as ')
            __M_writer(escape(c.logged_in_user.username))
            __M_writer(u' <a href="')
            __M_writer(escape(url(controller='account', action='signout')))
            __M_writer(u'">signout</a></p>\n')
            # SOURCE LINE 24
        else:
            # SOURCE LINE 25
            __M_writer(u'                <p><a href="')
            __M_writer(escape(url(controller='account', action='signin')))
            __M_writer(u'">Signin</a></p>\n')
            pass
        # SOURCE LINE 27
        __M_writer(u'            </div>\n            <div style="clear: both;"></div>\n            <div id="menu">\n                <ul>\n                    <li><a href="')
        # SOURCE LINE 31
        __M_writer(escape(url(controller='misc', action='titlepage')))
        __M_writer(u'">Home</a></li>\n                    <li><a href="')
        # SOURCE LINE 32
        __M_writer(escape(url(controller='item', action='view_items')))
        __M_writer(u'">View Items</a></li>\n                    <li><a href="')
        # SOURCE LINE 33
        __M_writer(escape(url(controller='item', action='new_item')))
        __M_writer(u'">New Item</a></li>\n                    <li><a href="')
        # SOURCE LINE 34
        __M_writer(escape(url(controller='misc', action='test')))
        __M_writer(u'">Test</a></li>\n                </ul>\n            </div>\n            ')
        # SOURCE LINE 37
        __M_writer(escape(next.body()))
        __M_writer(u'\n        </div>\n\n    </body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


