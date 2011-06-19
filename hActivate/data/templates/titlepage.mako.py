# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308476330.098053
_template_filename='/home/greg/Civicboom-hActivate/hActivate/hactivate/templates/titlepage.mako'
_template_uri='titlepage.mako'
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
        __M_writer(u'\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_body(context):
    context.caller_stack._push_frame()
    try:
        url = context.get('url', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 3
        __M_writer(u'\n    <div id="menu">\n        <ul>\n            <li><a href="')
        # SOURCE LINE 6
        __M_writer(escape(url(controller='misc', action='titlepage')))
        __M_writer(u'">Home</a></li>\n            <li><a href="')
        # SOURCE LINE 7
        __M_writer(escape(url(controller='misc', action='test')))
        __M_writer(u'">Test</a></li>\n            <li><a href="')
        # SOURCE LINE 8
        __M_writer(escape(url(controller='item', action='view_items')))
        __M_writer(u'">View Items</a></li>\n            <li><a href="')
        # SOURCE LINE 9
        __M_writer(escape(url(controller='misc', action='test')))
        __M_writer(u'">Test</a></li>\n        </ul>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


