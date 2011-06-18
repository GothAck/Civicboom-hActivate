# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308411744.991882
_template_filename='/home/allan/civicboom/hActivate/Civicboom-hActivate/hActivate/hactivate/templates/titlepage.mako'
_template_uri='titlepage.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<h1>FreeHoc</h1>\n\n<ul>\n    <li><a href="')
        # SOURCE LINE 4
        __M_writer(escape(url(controller='item', action='view_items')))
        __M_writer(u'">View Items</a></li>\n    <li><a href="')
        # SOURCE LINE 5
        __M_writer(escape(url(controller='misc', action='test')))
        __M_writer(u'">Test</a></li>\n</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


