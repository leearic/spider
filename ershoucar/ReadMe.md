这个repo 主要是 二手车Demo.　　</br>

计划：　　　</br>
    前  端：计划使用最基础的框架呈现出来.　　　</br>
    使用分布式爬虫，并能够解析js，最好能够解析ajax　　　</br>
    后　端：使用django-admin　管理修改查询数据,　使用 django-admin实现爬虫功能管理　　　</br>
    状态端：配置zabbix　使用zabbix来对爬虫实现动态监控　　　</br>
    日　志：对前端访问和后端爬虫爬取数据均会记录log,以便在后期对数据做一些分析和管理　　　</br>
    前端和后端以json接口方式实现数据通信　　　</br>


说明：　　　</br>
    这个 repo 仅仅是用来学习,并不做商业用途.　　　</br>
    爬虫能够正常运行　　　</br>
    前端正常运行　　　</br>
　</br>

访问：　</br>
    前端：　www.irole.cn　　部署在openshift上　</br>
    接口：　www.irole.cn/monster/page/*  *代表页数　</br>
           www.irole.cn/monster/detail/*  *代表汽车ＩＤ　</br>
　</br>
进度：　　　</br>
    日志：0%　　　</br>
    前端：95% 非json　　　</br>
    后端：90% 接口已经做好,还差爬虫功能管理　　　</br>
    状态端: 0％，需要先做日志　　　</br>

　　　</br>
安装：　　　</br>
    需要配置 redis  服务器(spider目录必须，非分布式不必)　　　</br>
    需要配置 splash 服务器(必须，不然不能解析js，报错)　　　</br>
    需要爬虫引擎 scrapy 和 web框架 django　　　</br>
    需要数据库MySQL(必须，不然不能存入数据)　　　</br>
    如果需要看状态,需要安装zabbix　　　</br>
　</br>

逻辑设计：　　　</br>
    ![sheji](https://github.com/leearic/ershoucar/blob/master/jiegou.jpg)　　　</br>


联系：　　　</br>
    email ： leearic@126.com　　　</br>
    QQ    ： leearic@126.com　　　</br>
    WeChat： leearic　　　</br>



