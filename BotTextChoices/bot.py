import sys
sys.path.append('../')
from modules.BotObjects.BotTextChoices import BotTextChoices
from telegramToken import TELEGRAM_TOKEN
from BotFlows import BotFlows

Bot = BotTextChoices(TELEGRAM_TOKEN, BotFlows)
Bot.run()
