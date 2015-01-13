from pulsar import provider
import urllib
import sys
import re
import HTMLParser

sys.path.append('resources/utils/')
import resources.utils.settings
from resources.utils.torrent import Torrents
from resources.utils.imdbapi import title_translate


def search(query):
    query = urllib.quote_plus(query)
    resp = provider.GET("https://oldpiratebay.org/search.php",
                        params={"q": query,
                                'Torrent_sort': 'seeders.desc',
                        })

    return extract_magnets(resp.data)


def extract_magnets(data):
    h = HTMLParser.HTMLParser()
    magnets = re.findall(r'magnet:\?[^\'"\s<>\[\]]+', data)
    seeders = re.findall('<td class="seeders-row s[y,n]+">[0-9]+?</td>', data)
    leechers = re.findall('<td class="leechers-row l[y,n]+">[0-9]+?</td>', data)

    torrName = [urllib.unquote_plus(re.findall('dn=(.*?)&', m).pop(0)) for m in magnets]

    TorrentsList = [Torrents.factory(t) for t in torrName]

    for tl, sds,lch,mgn in zip(TorrentsList, seeders, leechers, magnets):
        svalue = re.search('[0-9]+', sds)
        lvalue = re.search('[0-9]+',lch)
        tl.setSeeders(svalue.group())
        tl.setLeechers(lvalue.group())
        tl.setMagnet(mgn)#!!!ATTENTION!!!

    provider.log.info("LIST OF FOUND MAGNET LINKS")

    for tl in TorrentsList:
        if tl.getName().find("Subs") < 0:
            provider.log.info("ADD TORRENT -----> "+tl.getName())
            yield {"uri": tl.getMagnet()}


def search_episode(episode):
    return search("%(title)s S%(season)02dE%(episode)02d 720p" % episode)


def search_movie(movie):
    return search("%(title)s %(year)d ITA" % movie)


provider.register(search, search_movie, search_episode)
