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
    original_title=""

    for movie_results in data["movie_results"]:
        for token in movie_results:
            if token == "title":
                movie_info["title"] = unicodedata.normalize('NFKD',movie_results[token]).encode('ascii','ignore')
            if token == "original_title":
                original_title = movie_info[token]

    if original_title.lower() == movie_info["title"].lower():
        movie_info["title"] = movie_info["title"]+"ITA"

    return movie_info
