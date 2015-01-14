import urllib2
import urllib
import re
import json
import unicodedata

def title_translate(imdbid,year):
    lang = "it"
    json_data = urllib2.urlopen('http://api.themoviedb.org/3/find/%s?api_key=0ede5a89b54f3399dfdbd132b48ebcd6&external_source=imdb_id&language=%s'
                                % (imdbid,lang))
    data = json.load(json_data)
    movie_info  = {"title":"", "year":year}

    for movie_results in data["movie_results"]:
        for token in movie_results:
            if token == "title":
                movie_info["title"] = unicodedata.normalize('NFKD',movie_results[token]).encode('ascii','ignore')

    return movie_info
