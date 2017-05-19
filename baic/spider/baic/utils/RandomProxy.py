# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
import random

class RadomProxyWebdriver(object):
    @classmethod
    def getdriver(self):
            # 代理服务器地址来自 https://proxy.peuland.com/proxy_list_by_category.htm#
            proxylist  = [
                'http://183.61.236.55:3128',
                'http://122.156.214.154:3129',
                'http://112.226.254.225:8888',
                'http://222.133.31.130:2226',
                'http://123.124.168.107:80',
                'http://121.12.149.18:2226',
                'http://39.80.33.145:81',
                'http://121.40.108.76:80',
                'http://112.64.142.254:81',
            ]

            myproxy = random.choice(proxylist)
            # print  myproxy

            proxy = Proxy(
                {
                    'proxyType': ProxyType.MANUAL,
                    'httpProxy': myproxy,
                    'ftpProxy' : myproxy,
                    'sslProxy' : myproxy,
                    'noProxy' : ''
                }
            )
            self.driver = webdriver.Remote(command_executor='http://127.0.0.1:8080/wd/hub',
                                           desired_capabilities={
                                                "browserName": "chrome",
                                                'takeScreenshot': False,
                                                'javascriptEnabled': True,
                                            },
                                           proxy = proxy
                                           )
            return  self.driver
