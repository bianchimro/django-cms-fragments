from django.contrib import admin
from models import *


admin.site.register(Fragment)


class FragmentMembershipAdminInline(admin.StackedInline):

    model = FragmentMembership 
    extra = 0


class FragmentCollectionAdmin(admin.ModelAdmin):
    
    model = FragmentCollection
    inlines = [FragmentMembershipAdminInline]
    
admin.site.register(FragmentCollection, FragmentCollectionAdmin)