import http.client
import sys
import urllib.parse


def stdin_as_text():
    txt = ""
    for line in sys.stdin:
        txt += line
    return txt


def stdin_as_byte():
    txt = stdin_as_text()
    return txt.encode()


def get(url, key, value):
    params = urllib.parse.urlencode({key: value})
    response = urllib.request.urlopen(url + '?' + params)
    return response.status


def post(url, key, value):
    protocol, address, path = url_to_items(url)

    params = urllib.parse.urlencode({key: value})
    headers = {"Content-type": "application/x-www-form-urlencoded", "Accept": "text/plain"}
    if protocol == 'https':
        conn = http.client.HTTPSConnection(address)
    else:
        conn = http.client.HTTPConnection(address)
    conn.request('POST', path, params, headers)
    response = conn.getresponse()
    conn.close()
    return response.status


def url_to_items(url):
    # split url to get needed items from, assuming there is no, port defined
    s1, s2 = url.split('//')
    protocol = s1[:-1]
    path_start = s2.find('/')
    address = s2[:path_start]
    path = s2[path_start:]
    return protocol, address, path
