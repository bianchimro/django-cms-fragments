from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from django.utils.translation import ugettext_lazy as _

from models import FragmentCollectionPluginModel

class FragmentCollectionPlugin(CMSPluginBase):
    model = FragmentCollectionPluginModel
    name = _("Fragment Collection Plugin")
    render_template = "fragment_collection_plugin.html"

    def render(self, context, instance, placeholder):
    
        html_fragments = instance.fragment_collection.fragments.filter(fragment_type='html').all()
        html_content = ''
        
        for html_fragment in html_fragments:
            if html_fragment.file:
                f = html_fragment.file.open()
                html_content += f.read()
                f.close()
            
            if html_fragment.inline_code:
                html_content += html_fragment.inline_code
            
        context['html_content'] = html_content

        js_sources = []
        js_fragments = instance.fragment_collection.fragments.filter(fragment_type='js').order_by('fragmentmembership__order').all()
        
        for js_fragment in js_fragments:
            if js_fragment.direct_url:
                js_sources.append((js_fragment.direct_url, 'src'))
            elif js_fragment.file:
                js_sources.append((js_fragment.file.url, 'src'))
            
            if js_fragment.inline_code:
                js_sources.append((js_fragment.inline_code, 'inline'))

        context['js_sources'] = js_sources
        
        css_sources = []
        css_inlines = []
        css_fragments = instance.fragment_collection.fragments.filter(fragment_type='css').order_by('fragmentmembership__order').all()
        
        for css_fragment in css_fragments:
            if css_fragment.direct_url:
                css_sources.append((css_fragment.direct_url, 'src'))
            elif css_fragment.file:
                css_sources.append((css_fragment.file.url, 'src'))

            if css_fragment.inline_code:
                css_sources.append((css_fragment.inline_code, 'inline'))
            
        context['css_sources'] = css_sources
        context['instance'] = instance
        
        return context

#registering the plugin
plugin_pool.register_plugin(FragmentCollectionPlugin)