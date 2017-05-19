爬取百度糯米相关数据
1 环境需求:
    ubuntu 14.04(非必须)
    python 2.7.6
    django 1.9.6
    scrapy 1.1.0
    MySQL
    Redis
    scrapy-redis: 0.6.0

spider目录：
    爬虫程序：
    fang:  最简单的爬虫Demo.
    fang_with_headlessBrowser: 需要搭建无头浏览器，selenium.
                               教程传送门： www.jianshu.com/p/stRYfg
    fang_with_redis: 使用了scrapy-redis
    Redis_Spider_distribute: 这个分两部分
        server：将商品的URL放到redis里
        Client: 从Redis里去取url.

        url约定： 'ZONE,URL'，例如： '鞍山,http://www.anjuke.com/a/b/cc...'

frontend 目录：
    python django框架 主要是要用Django来操作数据库.

Testing：
    step 1. 在frontend目录中,先使用django创建数据表.
            cd frontend/soufang
            python manage.py  makemigrations  webapp
            python manage.py  migrate

    step 2. 在spider目录中,使用爬虫程序.
            cd fang
            scrapy crawl a
            重要说明： 在Redis_Spider_distribute 目录里，Server就是server，Client就是client，没有a爬虫了

未完成：
      1. 项目没有后台. 懒得做了 主要是想把精力放在 爬虫 上



说明： 本人想在成都(@中国)找个爬虫相关的工作，有介绍的联系我呀
      leearic@126.com

