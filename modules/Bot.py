from abc import ABC
import telebot

class Bot(ABC):
	def __init__(self, TELEGRAM_TOKEN):
		self.bot = telebot.TeleBot(TELEGRAM_TOKEN, parse_mode='HTML')

	def run(self):
		@self.bot.message_handler(func=lambda m: True)
		def processTextAndReply(message):
			self.processTextAndReply(message)


		@self.bot.message_handler(content_types=[
			"audio", "document", "photo", "sticker", "video", "video_note", "voice",
			"location", "contact", "new_chat_members", "left_chat_member", "new_chat_title",
			"new_chat_photo", "delete_chat_photo", "group_chat_created", "supergroup_chat_created",
			"channel_chat_created", "migrate_to_chat_id", "migrate_from_chat_id", "pinned_message"
		])
		def isNotText(message):
			self.bot.reply_to(message, "Poxa... eu só consigo entender quando você digita algo")

		self.bot.polling()

	def processTextAndReply(self, message):
		chatId = message.chat.id
		response = "A simple bot"
		self.bot.send_message(chatId, botResponse)

