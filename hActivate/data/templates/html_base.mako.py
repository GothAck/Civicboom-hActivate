# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308477354.730814
_template_filename=u'/home/greg/Civicboom-hActivate/hActivate/hactivate/templates/html_base.mako'
_template_uri=u'html_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = ['menu']


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n\n    <head>\n        <link rel="stylesheet" type="text/css" href="/style/style.css" />\n        <script type="text/javascript" src="/javascript/jquery.js"></script>\n        <script type="text/javascript" src="http://maps.google.com/maps/api/js?sensor=true"></script>\n        <title>FreeHoc</title>\n    </head>\n    \n    <body>\n        <div id="wrapper">\n            <div id="title_bar">\n                <img class="logo" src="/logo.png" />\n            </div>\n            <div style="clear: both;"></div>\n            ')
        # SOURCE LINE 16
        __M_writer(escape(next.body()))
        __M_writer(u'\n        </div>\n    </body>\n\n</html>\n\n')
        # SOURCE LINE 26
        __M_writer(u'\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_menu(context):
    context.caller_stack._push_frame()
    try:
        __M_writer = context.writer()
        # SOURCE LINE 22
        __M_writer(u'\n    <div id="menu">\n        \n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


