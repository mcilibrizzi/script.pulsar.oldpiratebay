class Torrent:
    def __init__(self,name):
        self.name = name
        self.seeders = 0
        self.leechers = 0
        self.magnet = ""

    def setSeeders(self,seedValue):
        self.seeders = seedValue

    def setLeechers(self,leechValue):
        self.leechers = leechValue

    def setMagnet(self,magnet):
        self.magnet = magnet

    def getSeeders(self):
        return  self.seeders

    def getLeechers(self):
        return self.leechers

    def getName(self):
        return self.name

    def getMagnet(self):
        return self.magnet



class Torrents:

    def factory(name):
        return Torrent(name)

    factory = staticmethod(factory)