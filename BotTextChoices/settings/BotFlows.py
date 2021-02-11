class BotFlows:
	NUMERIC_FLOWS = {
		'1': 'Compras',
		'2': 'Status.meu.pedido',
		'3': 'Trocas.devolucoes.ou.cancelamento',
	}

	PATTERN_MESSAGE_NOT_HANDLED = [
		'Desculpe, não entendi.',
	]
	
	FLOWS = {
		'': {
			'response': [
				'Oi! Eu sou a Ervilha, que bom te ver por aqui!',
				'Digite a opção que mais se encaixa com o seu assunto:\n'\
				'1 - 🛍️ Compras\n'\
				'2 - 🚛 Status do meu pedido\n'\
				'3 - 🔁 Trocas, devoluções ou cancelamento',
			],
			'not_handled': [
				'Poxa, acabei não entendendo... Me envie o número da opção que mais se encaixa'\
				'com a sua solicitação ;)'\
				'1 - 🛍️ Compras\n'\
				'2 - 🚛 Status do meu pedido\n'\
				'3 - 🔁 Trocas, devoluções ou cancelamento',
			],
		},
		'Compras': {
			'response': [
				'Como posso te ajudar nisso?\n'\
				'1 - Regras de compras pelo whatsapp\n'\
				'2 - Buscar lojas próximas\n'\
				'3 - Voltar ao menu inicial',
			],
			'not_handled': [
				'Desculpe, não entendi. O que você quer falar sobre compras?\n'\
				'1 - Regras de compras pelo whatsapp\n'\
				'2 - Buscar lojas próximas\n'\
				'3 - Voltar ao menu inicial',
			],
		},
		'Status.meu.pedido': {
			'response': [
				'Certo!\n'\
					'Gostaria de ressaltar que nossas entregas demoram até 14 dias '\
					'para serem entregues.',
				'Então para que eu possa localizar seu pedido, digite seu CPF.',
			],
			'not_handled': [
				'CPF inválido! Por favor, digite novamente o seu CPF',
			],
		},
		'Trocas.devolucoes.ou.cancelamento': {
			'response': [
				'Como posso te ajudar nisso?\n'\
				'1 - Trocas\n'\
				'2 - Devoluções\n'\
				'3 - Cancelar pedido\n'\
				'4 - Voltar ao menu principal',
			],
			'not_handled': [
				'Desculpe, não entendi muito bem.'\
				'Qual opção mais se encaixa com a sua solicitação?\n'\
					'1 - Trocas\n'\
					'2 - Devoluções\n'\
					'3 - Cancelar pedido\n'\
					'4 - Voltar ao menu principal',
			],
		}
	}