import sys
from settings import figmaUrl, figmaToken, TELEGRAM_TOKEN
from modules.BotObjects.BotBySets import BotBySets
from modules.FlowExtractor import FlowExtractor

def getFlows(Extractor):
    figmaData = Extractor.getFigmaData()
    Extractor.getPageWithFlows()

    Extractor.getBotDataForEachFlow()
    Extractor.insertBlockValues()
    Extractor.replaceToBeforeFlows()
    return Extractor.flows

Extractor = FlowExtractor(figmaUrl, figmaToken)
flows = getFlows(Extractor)

Bot = BotBySets(TELEGRAM_TOKEN, flows)
Bot.run()