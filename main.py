from info import info, sort_project_info, age_count
import telebot
token = "6742110064:AAE6qm2tDDQ9LG0B0nKiceorXXwOE-2FPJE" # YOUR TOKEN
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! \n"
                          "Я бот-визитка St1nBot, созданный для проекта Яндекс Практикума.\n"
                          "Если хочешь увидеть, что я умею, напиши /help")


@bot.message_handler(commands=["help"])
def send_help(message):
    bot.reply_to(message, "Вот список доступных команд:\n"
                          "/start - приветствие\n"
                          "/help - список команд\n"
                          "/info - основная информация о создателе\n"
                          "/projects - информация о проектах")


@bot.message_handler(commands=["info"])
def send_info(message):
    bot.reply_to(message, f"Меня зовут {info['name']}, мне {age_count(info['age'])}.\n"
                          f"Я люблю {info['hobbies']} и увлекаюсь {info['interests']}.\n"
                          f"Создатель бота - {info['author']}.\n"
                          f"Проекты: {info['projects'][1]}, {info['projects'][2]}, {info['projects'][3]}.\n"
                          "Все изображения сгенерированы с помощью сайта fusion brain.")


@bot.message_handler(commands=['projects'])
def send_welcome(message):
    bot.reply_to(message, sort_project_info())


@bot.message_handler(content_types=['text'])
def repeat_message(message):
    bot.send_message(message.chat.id, "Напиши команду /start, чтобы начать или "
                                      "команду /help, чтобы получить список доступных команд.")


bot.polling()