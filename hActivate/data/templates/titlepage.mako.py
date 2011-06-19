# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308476840.964285
_template_filename='/home/allan/civicboom/hActivate/Civicboom-hActivate/hActivate/hactivate/templates/titlepage.mako'
_template_uri='titlepage.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


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
        url = context.get('url', UNDEFINED)
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\n<h1>FreeHoc</h1>\n\n')
        # SOURCE LINE 5
        if c.logged_in_user:
            # SOURCE LINE 6
            __M_writer(u'<p>Signed in as ')
            __M_writer(escape(c.logged_in_user.username))
            __M_writer(u'</p>\n')
            # SOURCE LINE 7
        else:
            # SOURCE LINE 8
            __M_writer(u'<a href="')
            __M_writer(escape(url(controller='account', action='signin')))
            __M_writer(u'">Signin</a>\n')
            pass
        # SOURCE LINE 10
        __M_writer(u'\n<ul>\n    <li><a href="')
        # SOURCE LINE 12
        __M_writer(escape(url(controller='item', action='view_items')))
        __M_writer(u'">View Items</a></li>\n    <li><a href="')
        # SOURCE LINE 13
        __M_writer(escape(url(controller='item', action='new_item')))
        __M_writer(u'">New Item</a></li>\n</ul>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


