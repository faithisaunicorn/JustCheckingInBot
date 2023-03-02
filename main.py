from telegram import *
from requests import *
from asyncio import *
import os
import telebot

from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

bot = telebot.TeleBot(os.environ['BOT_TOKEN'], parse_mode="HTML")

############################### Bot ############################################
def start(update, context):
  update.message.reply_text(main_menu_message(),
                            reply_markup=main_menu_keyboard())

def main_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=main_menu_message(),
                        reply_markup=main_menu_keyboard())

def first_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=first_menu_message(),
                        reply_markup=first_menu_keyboard())

def second_menu(update,context):
  query = update.callback_query
  query.answer()
  query.edit_message_text(
                        text=second_menu_message(),
                        reply_markup=second_menu_keyboard())

# and so on for every callback_data option
def first_submenu(bot, update):
  pass

def second_submenu(bot, update):
  pass

############################ Keyboards #########################################
def main_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Option 1', callback_data='m1')],
              [InlineKeyboardButton('Option 2', callback_data='m2')],
              [InlineKeyboardButton('Option 3', callback_data='m3')]]
  return InlineKeyboardMarkup(keyboard)

def first_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 1-1', callback_data='m1_1')],
              [InlineKeyboardButton('Submenu 1-2', callback_data='m1_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

def second_menu_keyboard():
  keyboard = [[InlineKeyboardButton('Submenu 2-1', callback_data='m2_1')],
              [InlineKeyboardButton('Submenu 2-2', callback_data='m2_2')],
              [InlineKeyboardButton('Main menu', callback_data='main')]]
  return InlineKeyboardMarkup(keyboard)

############################# Messages #########################################
def main_menu_message():
  return 'Choose the option in main menu:'

def first_menu_message():
  return 'Choose the submenu in first menu:'

def second_menu_message():
  return 'Choose the submenu in second menu:'

############################# Handlers #########################################
updater = Updater(os.environ['BOT_TOKEN'], use_context=True)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CallbackQueryHandler(main_menu, pattern='main'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_menu, pattern='m1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_menu, pattern='m2'))
updater.dispatcher.add_handler(CallbackQueryHandler(first_submenu,
                                                    pattern='m1_1'))
updater.dispatcher.add_handler(CallbackQueryHandler(second_submenu,
                                                    pattern='m2_1'))

### STATIC COMMANDS ###
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, '''Hello and welcome to the Just Checking In Bot!''')

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, '''
    🚦Getting Started 🚦
- Create a new group with whoever you want to check in on/use this bot with
- Add @JustCheckingInBot to the group
- You’ll be individually guided through a quick set-up, then you’re good to go!
    ''')

@bot.message_handler(commands=['feedback'])
def feedback(message):
    bot.reply_to(message, "If you have any feedback/suggestions/bugs found, DM me directly on Telegram @faithisaunicorn :) Thanks a million!")

@bot.message_handler(commands=['about'])
def about(message):
    bot.reply_to(message, '''
@JustCheckingInBot was designed to help you check in regularly on your SO/friends/family and remind them that someone cares. If you’re too busy, tired, or forgot to message them, our daily reminders will help you out. All it takes is a few seconds.

This is a one-woman coding project by @faithisaunicorn, so do pardon the lack of features for now. If you'd like to collab or help me add new features, just let me know! :P
''')

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    if message.chat.type == "private":
        bot.reply_to(message, "Hello there! Would you like to add this bot to a group?")
    elif message.chat.type == "group":
        bot.reply_to(message, "Ello!")

### FUNCTIONAL COMMANDS ###

@bot.message_handler(commands=['settings'])
def edit_settings(message):
    bot.reply_to(message, "XX")

@bot.message_handler(commands=['checkin'])
def check_in_page(message):
    pass
    # “Are you using this bot with your partner/significant other or friend?”
    # if partner:
    # user = input(“Enter your name: “)
    # name = input(“Enter your partner’s name/nickname: “)
    # elif friend:
    # user = input(“Enter your name: “)
    # name = input(“Enter your friend’s name/nickname: “)





###NO OTHER CODE BELOW THIS LINE
updater.start_polling()