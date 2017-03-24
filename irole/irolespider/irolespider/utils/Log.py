__author__ = 'aric'
import syslog
class Mylog():
    def log(self, loginfo):
        syslog.openlog(ident="irole",logoption=syslog.LOG_PID, facility=syslog.LOG_LOCAL1)
        syslog.syslog(loginfo)