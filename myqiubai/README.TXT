1 环境要求：
    安装python2.7
    安装 PIP
    安装 SCRAPY
    安装 Django
2 部署步骤：
    修改django数据库连接地址：
        'NAME': 'qiushibaike', # MySQL 数据库名字
        'USER': 'root',        # MySQL 数据库用户名
        'PASSWORD': '123456',  # MySQL 数据库密码
    python  manage.py  syncdb
    python  manage.py  makemigrations
    python  manage.py  migrate
3 爬取数据：
    scrapy  crawl qiubai  # 爬取糗事百科数据
4 运行django：
    ## 运行糗事百科Demo
    python  manage.py  runserver 0.0.0.0:80
    or
    Apache的方式运行，配置文件在 conf 下. apache需要安装mod_wsgi 模块.



    #############################################    警告    #############################################

    这个已经不能用了..

