import serf
import urllib
import string
import urlparse


AVAILABLE_HOST_URI_QUERY_KEYS = set([
        'AuthKey',
    ], )


def _parse_host (h, ) :
    if not h.startswith('serf://') :
        h = 'serf://%s' % h

    _parsed = urlparse.urlparse(h, )
    _host = map(
            lambda x : None if x in ('', -1, ) else x,
            urllib.splitnport(_parsed.netloc, defport=7373, ),
        )

    if not _host[0] and not _host[1] :
        raise None

    if not _host[0] :
        _host[0] = serf.constant.DEFAULT_HOST

    if not _host[1] :
        _host[1] = serf.constant.DEFAULT_PORT

    _queries = dict()
    if _parsed.query :
        _queries = dict(map(
                urllib.splitvalue,
                filter(string.strip, _parsed.query.split('&'), ),
            ), )
        if set(_queries.keys()) != AVAILABLE_HOST_URI_QUERY_KEYS :
            return None

    _host.append(_queries, )

    return _host


def test_0 () :
    _host = 'serf://192.168.100.1:7374'
    assert _parse_host(_host, ) == ['192.168.100.1', 7374, {}]

    _host = 'serf://192.168.100.1:7374?AuthKey=this-is-token'
    assert _parse_host(_host, ) == ['192.168.100.1', 7374, {'AuthKey': 'this-is-token'}]


def teste_1 () :
    h = 'serf://192.168.100.1:7374/?AuthKey=this-is-token'
    if not h.startswith('serf://') :
        h = 'serf://%s' % h

    _parsed = urlparse.urlparse(h, )

    assert _parsed.scheme == 'serf'
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
    h = 'serf://192.168.100.1:7374/?AuthKey=this-is-token'
    if not h.startswith('serf://') :
        h = 'serf://%s' % h

    _parsed = urlparse.urlsplit(h, )

    assert _parsed.scheme == 'serf'
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
    h = 'serf://192.168.100.1:7374/index.html?AuthKey=this-is-token'
    if not h.startswith('serf://') :
        h = 'serf://%s' % h

    _parsed = urlparse.urlsplit(h, )

    assert _parsed.scheme == 'serf'
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


