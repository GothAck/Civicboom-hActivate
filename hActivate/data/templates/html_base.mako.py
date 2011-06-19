# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308477259.674692
_template_filename=u'/home/allan/civicboom/hActivate/Civicboom-hActivate/hActivate/hactivate/templates/html_base.mako'
_template_uri=u'html_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['menu']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n\n    <head>\n        <link rel="stylesheet" type="text/css" href="/style/style.css" />\n        <script type="text/javascript" src="/javascript/jquery.js"></script>\n        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>\n        <title>FreeHoc</title>\n    </head>\n    \n    <body>\n\n        <div class="header">\n')
        # SOURCE LINE 13
        if c.flash:
            # SOURCE LINE 14
            __M_writer(u'            <p class="flash_message">')
            __M_writer(escape(c.flash))
            __M_writer(u'</p>\n')
            pass
        # SOURCE LINE 16
        if c.logged_in_user:
            # SOURCE LINE 17
            __M_writer(u'            <p>Signed in as ')
            __M_writer(escape(c.logged_in_user.username))
            __M_writer(u'</p>\n')
            # SOURCE LINE 18
        else:
            # SOURCE LINE 19
            __M_writer(u'            <a href="')
            __M_writer(escape(url(controller='account', action='signin')))
            __M_writer(u'">Signin</a>\n')
            pass
        # SOURCE LINE 21
        __M_writer(u'        </div>\n\n        <div id="wrapper">\n            <div id="title_bar">\n                <h1>FreeHoc</h1>\n            </div>\n            ')
        # SOURCE LINE 27
        __M_writer(escape(next.body()))
        __M_writer(u'\n        </div>\n\n    </body>\n\n</html>\n\n')
        # SOURCE LINE 38
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 34
        __M_writer(u'\n    <div id="menu">\n        \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


