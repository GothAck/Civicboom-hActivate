# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308414239.840916
_template_filename='/home/allan/civicboom/hActivate/Civicboom-hActivate/hActivate/hactivate/templates/view_item.mako'
_template_uri='view_item.mako'
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
        c = context.get('c', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'\n\nView single item\n\nwith requests\n\n')
        # SOURCE LINE 7
        if not c.item:
            # SOURCE LINE 8
            __M_writer(u'  No item\n')
            # SOURCE LINE 9
        else:
            # SOURCE LINE 10
            __M_writer(u'  Item: ')
            __M_writer(escape(c.item.id))
            __M_writer(u'\n')
            pass
        return ''
    finally:
        context.caller_stack._pop_frame()

