爬取百度糯米相关数据
1 环境需求:
    ubuntu 14.04(非必须)
    python 2.7.6
    django 1.8.4
    scrapy 1.0.3

spider   目录：
    爬虫主要程序, 现在已经能够爬取一些数据,但是有一些数据要做js解析,关于JS解析的暂时还没做

spider_with_splash 目录：
    爬虫的主要程序，现在已经能够使用splash+scrapyjs 解析js，爬取全站程序都会从splash过一次.
    但是还没做获取一些js数据，比如获取店铺地址.

frontend 目录：
    python django框架,之所有用这个主要是想用django的ORM,操作数据库比较方便.后期会加上前端展示

Testing：
    step 1. 在frontend目录中,先使用django创建数据表.
            cd frontend/nuomi
            python manage.py  syncdb
            python manage.py  migrate
    step 2. 在spider目录中,使用爬虫程序.
            cd spider
            scrapy crawl nuomi

项目演示地址: www.irole.cn
未完成：
      1. 项目没有后台. 懒得做了 主要是想把精力放在 爬虫 上
      2. 服务器做得不太好, 没做404,500 错误什么的,开启了 django的Debug模式
      3. 其他待优化项