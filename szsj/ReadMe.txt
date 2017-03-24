1. 环境说明
    本环境在xubuntu 16.04 64Bit 下完成.
    python 2
    scrapy
    django
    mysql
    Chrome浏览器

2. 部署
    需要安装 scrapy:  pip install scrapy
    需要安装 Django:  pip install django
    如果木有mysqldb库,则需要另外安装:    apt-get install python-mysqldb


3. 文件夹说明:
    Brower-Driver:      是chrome浏览器的驱动, chromedriver放到 /usr/bin 下 并且给执行权限
    HeadlessBrowser:    是无头浏览器,这个项目没有用到,忽略
    dj_sz:              Django项目, 主要用django来完成数据库的操作.
    sp_sz:              爬虫项目,爬取数据

4. 爬虫说明:
    到sp_sz 目录下,执行 scrapy list 会获取到几个爬虫.
     a. unit:        到深圳政府网站爬取公司列表
     b. unitinfo:    获取到了列表后,到企查查去查公司详细信息
     c. IDC:         爬取IDC相关数据



5. 其他:
    企查查上的源码tag里有中文字符,  所以目前没有爬非首页内容.

    没有按照标准来, 直接一个for 循环搞定. 中间设置了标志,如果中断,被ban等情况发生, 可以从ban的位置继续爬下去





