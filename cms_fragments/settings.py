from django.conf import settings


_CMS_FRAGMENTS_REGIONS = [('region_1', 'A region'), ]
CMS_FRAGMENTS_REGIONS = getattr(settings, 'CMS_FRAGMENTS_REGIONS', _CMS_FRAGMENTS_REGIONS)
