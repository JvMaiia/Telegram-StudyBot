import telebot
bot = telebot.TeleBot("YOUR TOKEN BOT")
@bot.message_handler(commands=['materias'])
def send_materias(message):
	bot.reply_to(message, "Até o exato momento temos suporte para as seguintes matérias: /Quimica, /Fisica, /Biologia, /Matematica, /Historia, /Geografia, /Artes")
@bot.message_handler(commands=['Quimica']) #adiciona o comando ao bot
def send_quimica(message): #define a função que irá ser acionada com o comando do bot acima
	quimfile = open('quimica.txt', 'r')
	mess = quimfile.read()
	bot.reply_to(message, mess)
	quimfile.close()
@bot.message_handler(commands=['Fisica'])
def send_fisica(message):
	fisfile = open('fisica.txt', 'r')
	fiss = fisfile.read()
	bot.reply_to(message, fiss)
	fisfile.close()
@bot.message_handler(commands=['Biologia'])
def send_biologia(message):
	biofile = open('biologia.txt', 'r')
	bioo = biofile.read()
	bot.reply_to(message, bioo)
	biofile.close()
@bot.message_handler(commands=['Matematica'])
def send_matematica(message):
	matfile = open('matematica.txt', 'r')
	matt = matfile.read()
	bot.reply_to(message, matt)
	matfile.close()
@bot.message_handler(commands=['Historia'])
def send_historia(message):
	histfile = open('historia.txt', 'r')
	histt = histfile.read()
	bot.reply_to(message, histt)
	histfile.close()
@bot.message_handler(commands=['Geografia'])
def send_geografia(message):
	geofile = open('geografia.txt', 'r')
	geoo = geofile.read()
	bot.reply_to(message, geoo)
	geofile.close()
@bot.message_handler(commands=['Artes'])
def send_artes(message):
	artfile = open('artes.txt', 'r')
	artt = artfile.read()
	bot.reply_to(message, artt)
	artfile.close()
bot.polling()