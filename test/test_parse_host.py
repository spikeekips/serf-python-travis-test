import serf
import urllib
import string
import urlparse


AVAILABLE_HOST_URI_QUERY_KEYS = set([
        'AuthKey',
    ], )


def teste_1 () :
    h = 'http://192.168.100.1:7374/?AuthKey=this-is-token'
    _parsed = urlparse.urlparse(h, )

    assert _parsed.scheme == 'http'
    assert _parsed.netloc == '192.168.100.1:7374'
    assert _parsed.path == '/'
    assert _parsed.params == ''
    assert _parsed.query == 'AuthKey=this-is-token'
    assert _parsed.fragment == ''

    _host = map(
            lambda x : None if x in ('', -1, ) else x,
            urllib.splitnport(_parsed.netloc, defport=7373, ),
        )
    assert _host == ['192.168.100.1', 7374]

    assert _parsed.query == 'AuthKey=this-is-token'

    if _parsed.query :
        _queries = dict(map(
                urllib.splitvalue,
                filter(string.strip, _parsed.query.split('&'), ),
            ), )

        assert _queries.keys() == ['AuthKey', ]

def teste_2 () :
    h = 'http://192.168.100.1:7374/?AuthKey=this-is-token'
    _parsed = urlparse.urlsplit(h, )

    assert _parsed.scheme == 'http'
    assert _parsed.netloc == '192.168.100.1:7374'
    assert _parsed.path == '/'
    assert _parsed.query == 'AuthKey=this-is-token'
    assert _parsed.fragment == ''

    _host = map(
            lambda x : None if x in ('', -1, ) else x,
            urllib.splitnport(_parsed.netloc, defport=7373, ),
        )
    assert _host == ['192.168.100.1', 7374]

    assert _parsed.query == 'AuthKey=this-is-token'

    if _parsed.query :
        _queries = dict(map(
                urllib.splitvalue,
                filter(string.strip, _parsed.query.split('&'), ),
            ), )

        assert _queries.keys() == ['AuthKey', ]


def teste_3 () :
    h = 'http://192.168.100.1:7374/index.html?AuthKey=this-is-token'
    _parsed = urlparse.urlsplit(h, )

    assert _parsed.scheme == 'http'
    assert _parsed.netloc == '192.168.100.1:7374'
    assert _parsed.path == '/index.html'
    assert _parsed.query == 'AuthKey=this-is-token'
    assert _parsed.fragment == ''

    _host = map(
            lambda x : None if x in ('', -1, ) else x,
            urllib.splitnport(_parsed.netloc, defport=7373, ),
        )
    assert _host == ['192.168.100.1', 7374]

    assert _parsed.query == 'AuthKey=this-is-token'

    if _parsed.query :
        _queries = dict(map(
                urllib.splitvalue,
                filter(string.strip, _parsed.query.split('&'), ),
            ), )

        assert _queries.keys() == ['AuthKey', ]


