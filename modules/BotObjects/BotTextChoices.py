from modules.Bot import Bot

class BotTextChoices(Bot):
	def processTextAndReply(self):
		self.getData()

		self.botResponses = "oi"
		self.bot.send_message(self.chatId, self.botResponses)

		self.storeData()
		if int(self.datetime.hour) % 6 == 0:
			self.saveData()
