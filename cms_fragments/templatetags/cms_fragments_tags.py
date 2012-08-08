from __future__ import absolute_import

from django import template
import cms_fragments.models

register = template.Library()

import cms_fragments.settings as settings


class RegionNode(template.Node):

    def __init__(self, region_name):
        #import cms_fragments
        #print dir(cms_fragments)
        #

        self.region_name = region_name.replace("'", "").replace('"', '')
        

    def render(self, context):
        valid_regions = [x[0] for x in settings.CMS_FRAGMENTS_REGIONS]
        output = ""
        
        if self.region_name not in valid_regions:
            message = "Region %s not declared in settings %s" % (self.region_name, str(settings.CMS_FRAGMENTS_REGIONS))
            raise Exception(message)
        
        try:
            region = cms_fragments.models.FragmentRegion.objects.get(pk = self.region_name)
        except:
            return ""
        blocks = region.fragment_blocks.all()
        for block in blocks:    
            print dir(block.placeholder)
            output += block.placeholder.render(context, None)
            
        return output
            
    

@register.tag
def region(parser, token):
    """{% region "region_name" %}"""
    try:
        # split_contents() knows not to split quoted strings.
        tag_name, region_name = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly one argument" % token.contents.split()[0])
    if not (region_name[0] == region_name[-1] and region_name[0] in ('"', "'")):
        raise template.TemplateSyntaxError("%r tag's argument should be in quotes" % tag_name)
    return RegionNode(region_name)
    