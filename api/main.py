import falcon
from . import config
from . import mainhandler
from . import symbolhandler
from . import testhandler

configFile = config.findConfigFile(
    [ '../config/pysymproxy.json'
    , './config/pysymproxy.json'
    , './config/default.pysymproxy.json'])

configuration = config.Config(configFile)

symbolroutehandler = symbolhandler.SymbolHandler(configuration)
testrouteHandler = testhandler.TestHandler()
defaultroutehandler = mainhandler.MainHandler(configuration, symbolroutehandler.getStats())

api = falcon.App()
api.add_route('/{file}', defaultroutehandler)
api.add_route('/symbols/{file}/{identifier}/{rawfile}', symbolroutehandler)
api.add_route('/test/{file1}/{file2}/{file3}', testrouteHandler)