from django.conf import settings
from django.forms import *
from django.forms.widgets import flatatt
from django.utils.encoding import smart_unicode
from django.utils.html import escape
from django.utils.simplejson import *
from django.utils.safestring import mark_safe
from django.utils.html import escape, conditional_escape
from django.utils.encoding import StrAndUnicode, force_unicode

class AceArea(Textarea):

    def __init__(self, attrs=None):
        # The 'rows' and 'cols' attributes are required for HTML correctness.
        default_attrs = {'cols': '40', 'rows': '10', 'class':'ace-django-editor'}
        if attrs:
            default_attrs.update(attrs)
        super(Textarea, self).__init__(default_attrs)

    def render(self, name, value, attrs=None):
        if value is None: value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        id = attrs['id']
        
        template = """
        <div class="ace-editor-widget">
            <div id="%s_editor" class="ace_editor ace-django-editor" data-target="%s">%s</div>
            <textarea style="display:none;"%s></textarea>
        </div>
        
        """ %  (id, id, conditional_escape(force_unicode(value)), flatatt(final_attrs))
       
        return mark_safe(template)
       
    #TODO: move ace_start.js inclusion to admin form
    class Media:
        js = ('acejs/ace.js','acejs/theme-twilight.js', 'acejs/mode-css.js', 'acejs/mode-javascript.js',
                'acejs/mode-html.js', 'ace_start.js')
        css = {
             'all': ('acecss/defaultace.css', ),
        }

# Custom Fields
from django.db import models
class AceAreaField(models.TextField):
    description = "Same as the standard TextField field, but with syntax highlighting."
    def formfield(self, **kwargs):
        defaults = {}
        defaults.update(kwargs)
        defaults['widget'] = AceArea()
        return super(AceAreaField, self).formfield(**defaults)
