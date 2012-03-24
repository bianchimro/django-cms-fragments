from cms.models.pluginmodel import CMSPlugin
from django.db import models
from django.core.exceptions import ValidationError
import editarea

class Fragment(models.Model):
    
    fragment_type = models.CharField(max_length=10, choices=(('js', 'javascript'), ('css', 'css'),('html', 'HTML fragment')))
    file = models.FileField(null=True, blank=True, upload_to="cms_fragments");
    direct_url = models.URLField(null=True, blank=True)
    inline_code = editarea.EditAreaField(null=True, blank=True)
    
    def clean(self):
        # Don't allow all direct_url, file and inline_code to be empty
        if not self.file and not self.direct_url and not self.inline_code:
            raise ValidationError('You must provide an uploaded file or an url')
    
    def __unicode__(self):
        if self.file:
            return u'%s: %s' % (self.fragment_type, self.file.url)
        if self.direct_url:
            return u'%s: %s' % (self.fragment_type, self.direct_url)
        if self.inline_code:
            return u'%s: %s' % (self.fragment_type, "(inline code)")
        return "none"

    
class FragmentCollection(models.Model):
    name = models.CharField(max_length=100)
    fragments = models.ManyToManyField(Fragment, through='FragmentMembership')
    
    def __unicode__(self):
        return u'%s' % (self.name)


class FragmentMembership(models.Model):
    fragment = models.ForeignKey(Fragment)
    fragment_collection = models.ForeignKey(FragmentCollection)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ('order',)

class FragmentPluginModel(CMSPlugin):
    fragment = models.ForeignKey(Fragment)
    

class FragmentCollectionPluginModel(CMSPlugin):
    fragment_collection = models.ForeignKey(FragmentCollection)