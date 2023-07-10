import configparser

config = configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class readConfig():
    @staticmethod
    def getApplicationURL():
        url = config.get('common info', 'googleURL')
        return url
