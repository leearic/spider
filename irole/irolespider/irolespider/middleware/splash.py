import re

from scrapy import signals
# from scrapy.http import Request
from scrapy.exceptions import NotConfigured
import w3lib.url

_matches = lambda url, regexs: any((r.search(url) for r in regexs))

class SplashMiddleware(object):

    url = 'http://localhost:8050/render.html'
    wait = 2
    url_pass = ()
    url_block = ()

    _settings = [
        'endpoint',
        'wait',
        'images',
        'js',
        'filters',
        'viewport',
    ]

    def __init__(self, crawler):
        self.crwlr_settings = crawler.settings
        self.crwlr_stats = crawler.stats

    @classmethod
    def from_crawler(cls, crawler):
        if not crawler.settings.getbool('SPLASH_ENABLED'):
            raise NotConfigured
        o = cls(crawler)
        crawler.signals.connect(o.open_spider, signal=signals.spider_opened)
        return o

    def open_spider(self, spider):
        for k in self._settings:
            setattr(self, k, self._get_setting_value(spider,
                self.crwlr_settings, k))
        # check URL filters
        url_pass = self._get_setting_value(spider, self.crwlr_settings, 'url_pass')
        if url_pass:
            self.url_pass = [re.compile(x) for x in url_pass]
        url_block = self._get_setting_value(spider, self.crwlr_settings, 'url_block')
        if url_block:
            self.url_block = [re.compile(x) for x in url_block]

    def _get_setting_value(self, spider, settings, k):
        o = getattr(self, k, None)
        s = settings.get('SPLASH_' + k.upper(), o)
        return getattr(spider, 'splash_' + k, s)

    def _needs_wrapping(self, request):
        # already wrapped
        if request.meta.get("splashed_url", False):
            return False

        # force wrap or not
        use_splash = request.meta.get("use_splash", None)
        if use_splash is not None:
            return use_splash == True

        # check URL regexes
        if not self.url_pass and not self.url_block:
            return False
        if self.url_pass and not _matches(request.url, self.url_pass):
            return False
        if self.url_block and _matches(request.url, self.url_block):
            return False

        return True

    def process_request(self, request, spider):
        if self._needs_wrapping(request):
            self.crwlr_stats.inc_value('splash/wrapped', spider=spider)
            return self._wrap_url(request)

    def process_response(self, request, response, spider):
        if request.meta.get('splashed_url', False):
            self.crwlr_stats.inc_value('splash/unwrapped', spider=spider)
            return self._unwrap_url(request, response)
        else:
            return response

    def _wrap_url(self, request):
        wrapped = w3lib.url.add_or_replace_parameter(self.endpoint, 'url', request.url)

        # pass options
        wrapped = w3lib.url.add_or_replace_parameter(wrapped, 'wait', self.wait)
        if self.viewport:
            wrapped = w3lib.url.add_or_replace_parameter(wrapped, 'viewport', self.viewport)
        wrapped = w3lib.url.add_or_replace_parameter(wrapped, 'images', 1 if self.images else 0)
        if self.js:
            wrapped = w3lib.url.add_or_replace_parameter(wrapped, 'js', self.js)
        if self.filters:
            wrapped = w3lib.url.add_or_replace_parameter(wrapped, 'filters', self.filters)

        return request.replace(url=wrapped, meta={"splashed_url": request.url})

    def _unwrap_url(self, request, response):
        unwrapped = w3lib.url.url_query_parameter(request.url, 'url')
        response = response.replace(url=unwrapped)
        return response
