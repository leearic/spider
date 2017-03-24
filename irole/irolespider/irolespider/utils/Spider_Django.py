__author__ = 'aric'

import sys,os

from irolespider.settings import path

if path not in sys.path:
    sys.path.append(path)

import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "irole.settings")
django.setup()



from cnirole.models import cosplay8dotcom

class django_sql(object):
    def save_Item(self, item):
        cosplay8 = cosplay8dotcom()
        cosplay8.base_html_url      = item["html_base_url"]
        cosplay8.base_image_url     = item["img_base_url"][0]
        cosplay8.base_image_content = item["img_content"][0].encode("utf-8")
        cosplay8.save()

    def is_crawled(self, html_url):
        try:
            aa = cosplay8dotcom.objects.filter(base_html_url=html_url)
            if len(aa) != 0:
                return False
            else:
                return True;
        except Exception, e:
            return True
