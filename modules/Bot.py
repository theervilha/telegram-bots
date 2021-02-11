from datetime import datetime
import os
import pandas as pd
from abc import ABC
import telebot

class Bot(ABC):
	def __init__(self, TELEGRAM_TOKEN, BotFlows):
		self.bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')
		self.data = pd.DataFrame()
		self.BotFlows = BotFlows

	def run(self):
		@self.bot.message_handler(func=lambda m: True)
		def processTextAndReply(message):
			self.message = message
			self.processTextAndReply()


		@self.bot.message_handler(content_types=[
			"audio", "document", "photo", "sticker", "video", "video_note", "voice",
			"location", "contact", "new_chat_members", "left_chat_member", "new_chat_title",
			"new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created",
			"channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message"
		])
		def isNotText(message):
			self.bot.reply_to(message, "Poxa... eu só consigo entender quando você digita algo")

		self.bot.polling()

	def processTextAndReply(self):
		self.getData()

		self.botResponses = "A simple bot"
		self.bot.send_message(self.chatId, self.botResponses)

		self.storeData()
		if int(self.datetime.hour) % 6 == 0:
			self.saveData()

	def getData(self):
		self.chatId = self.message.chat.id
		self.datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

	def storeData(self):
		self.data = self.data.append({
			'user_message': self.message.text,
			'bot_response': self.botResponses,
			'datetime': self.datetime,
		}, ignore_index=True)

	def saveData(self, path='reports'):
		if not os.path.exists(path):
			os.makedirs(path)

		date = datetime.now().strftime("%Y-%m-%d")
		self.data.to_csv(f'{path}/report - {date}.csv', index=False, encoding='utf-8')