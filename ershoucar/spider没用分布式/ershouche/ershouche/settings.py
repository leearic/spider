# -*- coding: utf-8 -*-

# Scrapy settings for ershouche project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ershouche'
LOG_LEVEL = 'ERROR'
SPIDER_MODULES = ['ershouche.spiders']
NEWSPIDER_MODULE = 'ershouche.spiders'

BaseUrl = 'http://www.renrenche.com/'
path = "/home/dev136/PycharmProjects/ershoucar/frontend"

# 增加splash支持
DOWNLOADER_MIDDLEWARES = {
    # 浏览器头信息
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
    # 'baidunuomi.utils.User_Agent.RotateUserAgentMiddleware' :400,
    # 使用splash
    'scrapyjs.SplashMiddleware': 725,
    # scrapy使用代理服务器 非splash的代理
#    'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
#    'baidunuomi.utils.User_Proxy.ProxyMiddleware': 100,
}

DEFAULT_ITEM_CLASS = {'erchouche.items.CarItem': 300}

IMAGES_MIN_HEIGHT = 50
IMAGES_MIN_WIDTH = 50
IMAGES_STORE = 'images'
DOWNLOAD_TIMEOUT = 1200
ITEM_PIPELINES ={'ershouche.pipelines.ErshouchePipeline': 300}

DUPEFILTER_CLASS = 'scrapyjs.SplashAwareDupeFilter'
SPLASH_URL = 'http://192.168.1.134:8000/'



# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ershouche (+http://www.yourdomain.com)'

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS=32

# Configure a delay for requests for the same website (default: 0)
# See http://scrapy.readthedocs.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY=3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN=16
#CONCURRENT_REQUESTS_PER_IP=16

# Disable cookies (enabled by default)
#COOKIES_ENABLED=False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED=False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ershouche.middlewares.MyCustomSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ershouche.middlewares.MyCustomDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See http://scrapy.readthedocs.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    'ershouche.pipelines.SomePipeline': 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See http://doc.scrapy.org/en/latest/topics/autothrottle.html
# NOTE: AutoThrottle will honour the standard settings for concurrency and delay
#AUTOTHROTTLE_ENABLED=True
# The initial download delay
#AUTOTHROTTLE_START_DELAY=5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY=60
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG=False

# Enable and configure HTTP caching (disabled by default)
# See http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED=True
#HTTPCACHE_EXPIRATION_SECS=0
#HTTPCACHE_DIR='httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES=[]
#HTTPCACHE_STORAGE='scrapy.extensions.httpcache.FilesystemCacheStorage'
