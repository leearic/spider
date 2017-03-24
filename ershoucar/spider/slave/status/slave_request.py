import json
import urllib

def  slave_status():
    url = 'http://127.0.0.1/monster/'
    data = {}
    data['ip'] = '192.168.1.1'
    data['scraped'] = 29
    data['images'] = 29
    data['exception'] = 0
    data['error'] = 0
    data['site'] = 'renrenche.com'
    data['traffic_up'] = '26.9'
    data['traffic_down'] = '59.9'
    try:
        postdata = json.dumps(data)
        resp = urllib.urlopen(url, postdata)

        res = resp.read()
        return res

    except Exception, e:
        return 'error'


if __name__ == '__main__':

    print slave_status()


