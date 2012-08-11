from django.conf import settings


_CMS_FRAGMENTS_REGIONS = []
CMS_FRAGMENTS_REGIONS = getattr(settings, 'CMS_FRAGMENTS_REGIONS', _CMS_FRAGMENTS_REGIONS)
