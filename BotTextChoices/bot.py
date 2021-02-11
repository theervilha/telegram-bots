import sys
sys.path.append('../')
from modules.BotObjects.BotTextChoices import BotTextChoices
from telegramToken import TELEGRAM_TOKEN

Bot = BotTextChoices(TELEGRAM_TOKEN)
Bot.run()
