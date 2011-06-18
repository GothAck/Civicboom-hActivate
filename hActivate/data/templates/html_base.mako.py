# -*- encoding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1308407787.34994
_template_filename=u'/home/allan/civicboom/hActivate/Civicboom-hActivate/hActivate/hactivate/templates/html_base.mako'
_template_uri=u'html_base.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        next = context.get('next', UNDEFINED)
        __M_writer = context.writer()
        # SOURCE LINE 1
        __M_writer(u'<html>\n\n    <head>\n        <title>FreeHoc</title>\n    </head>\n    \n    <body>\n        ')
        # SOURCE LINE 8
        __M_writer(escape(next.body()))
        __M_writer(u'\n    </body>\n\n</html>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


