from django.contrib import admin
from cms.admin.placeholderadmin import PlaceholderAdmin
from models import *


admin.site.register(Fragment)


class FragmentMembershipAdminInline(admin.StackedInline):

    model = FragmentMembership 
    extra = 0


class FragmentCollectionAdmin(admin.ModelAdmin):
    
    model = FragmentCollection
    inlines = [FragmentMembershipAdminInline]
    
admin.site.register(FragmentCollection, FragmentCollectionAdmin)


class FragmentBlockMembershipInline(admin.StackedInline):
    model = FragmentBlockMembership

class FragmentRegionAdmin(admin.ModelAdmin):
    model = FragmentRegion
    inlines = [FragmentBlockMembershipInline]
    
    
admin.site.register(FragmentBlock, PlaceholderAdmin)
admin.site.register(FragmentRegion, FragmentRegionAdmin)