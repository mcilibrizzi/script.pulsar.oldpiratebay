import urllib2
import urllib
import re
import json

def title_translate(imdbid):
    lang = "it-ch"
    json_data = urllib2.urlopen('http://www.myapifilms.com/imdb?idIMDB=%s&format=JSON&aka=1&business=0&seasons=0&seasonYear=0&technical=0&lang=%s&actors=N&biography=0&trailer=0&uniqueName=0&filmography=0&bornDied=0&starSign=0&actorActress=0&actorTrivia=0&movieTrivia=0&awards=0'
                                % (imdbid,lang))
    data = json.load(json_data)
    movie_info  = {"title":"", "year":data["year"]}

    for country in data["akas"]:
        if country["country"]=="Italy":
            movie_info["title"] = country["title"]

    return movie_info
