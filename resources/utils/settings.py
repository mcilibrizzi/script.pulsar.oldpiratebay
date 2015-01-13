import xbmcaddon
import xbmc
class Settings:
    def __init__():
        self.settings = xbmcaddon.Addon()

        if(self.settings.getSettings('480p')=='true'):
            self.qulityPref["480p"] = bool(0)
        else:
            self.quelityPref["480p"] = bool(1)

        if(self.settings.getSettings('720p')=='true'):
            self.qulityPref["720p"] = bool(0)
        else:
            self.quelityPref["720p"] = bool(1)

        if(self.settings.getSettings('1080p')=='true'):
            self.qulityPref["1080p"] = bool(0)
        else:
            self.quelityPref["1080p"] = bool(1)
