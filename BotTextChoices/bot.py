import sys
sys.path.append('../')
from modules.BotObjects.BotTextChoices import BotTextChoices
from settings.telegramToken import TELEGRAM_TOKEN
from settings.BotFlows import BotFlows

Bot = BotTextChoices(TELEGRAM_TOKEN, BotFlows)
Bot.run()
