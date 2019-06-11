#! /usr/bin/env python
import sys


def set_beacon(channelkey, rrggbb, period_ms=0):
    """Python 2/3 compatible hacky code below!"""
    PYTHON3 = False
    try:
        from urllib.request import urlopen
        from urllib.parse import urlencode, quote_plus
        PYTHON3 = True
    except ImportError:
        from urllib2 import urlopen
        from urllib import urlencode

    url = 'https://api.cilamp.se/v1/' + channelkey
    params = {
        'color': rrggbb,
        'period': period_ms
    }
    if PYTHON3:
        data = urlencode(
            params,
            quote_via=quote_plus
        ).encode('utf-8')
    else:
        data = urlencode(params)
    print("     url:\t{url}".format(url=url))
    print("  params:\t{params}".format(params=params))
    req = urlopen(url, data)
    print("response:\t{response}".format(response=req.read()))


if __name__ == '__main__':
    if len(sys.argv) in [3, 4]:
        channelkey = sys.argv[1]
        color = sys.argv[2]
        period = 0 if len(sys.argv) != 4 else sys.argv[3]
        set_beacon(channelkey, color, period)
    else:
        print("Usage: python bi-beacon.se <channelkey> <hexcolor> [period_ms]")
