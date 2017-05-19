# -*- coding: utf-8 -*-

# Scrapy settings for cos8 project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'irolespider'

SPIDER_MODULES = ['irolespider.spiders']
NEWSPIDER_MODULE = 'irolespider.spiders'

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'cos8 (+http://www.yourdomain.com)'
LOG_LEVEL = 'ERROR'

base_url = "http://www.cosplay8.com/"
path = "/home/aric/PycharmProjects/irole"


DOWNLOADER_MIDDLEWARES = {
    # 'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware' : None,
    #  'irolespider.utils.user_agent.RotateUserAgentMiddleware' :400,

    'irolespider.middleware.splash.SplashMiddleware': 725,

    # 'scrapy.downloadermiddlewares.httpproxy.HttpProxyMiddleware': 110,
    # 'irolespider.utils.proxy_midware.ProxyMiddleware': 100,
}

DEFAULT_ITEM_CLASS = 'irolespider.items.Cos8Item'
IMAGES_MIN_HEIGHT = 50
IMAGES_MIN_WIDTH = 50
IMAGES_STORE = 'images'
DOWNLOAD_TIMEOUT = 1200
ITEM_PIPELINES ={'irolespider.pipelines.Cos8Pipeline': 300, }



SPLASH_ENABLED = True
SPLASH_ENDPOINT = 'http://127.0.0.1:5000/render.html'
SPLASH_WAIT = 2
SPLASH_IMAGES = False
#SPLASH_URL_PASS = (r'example\.com',)
#SPLASH_URL_BLOCK = (r'badexample\.com',)

CONCURRENT_REQUESTS_PER_DOMAIN = 5
CONCURRENT_REQUESTS = 5
RETRY_ENABLED = False