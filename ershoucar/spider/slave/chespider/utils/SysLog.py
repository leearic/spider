# -*- coding: utf-8 -*-
import syslog

class SpiderLog(object):


    @classmethod
    def _formatlog(self, msg):
        msgs = ''
        for i in msg:
            if isinstance(msg, list):
                msgs = msgs + i + "|"
            else:
                msgs = msgs + i+":"+msg[i][0] + "|"
        return msgs.encode('utf8')

    @classmethod
    def log(cls, name, msg):
        syslog.openlog(name)
        syslog.syslog(cls._formatlog(msg))

    @classmethod
    def err(cls, name, msg):
        syslog.openlog(name)
        syslog.syslog("err" + cls._formatlog(msg))