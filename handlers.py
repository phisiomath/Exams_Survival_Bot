import telegram.ext
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler, InlineQueryHandler
from bot_body import dispatcher, updater
import message_snippets
import json
import markup
from dict import dict, get_ending, handle_ending
from game_script import Game, print_parametres
from telegram.ext.dispatcher import run_async
import random
import media


# import inlines


def start(context, update):
    if update.message:
        context.send_animation(chat_id=update.message.chat_id,
                               animation=media.create_media_1(dict[0][0], media.file_ids_base[0]),
                               reply_markup=markup.game_inline_markup(0))


def help(context, update):
    if update.message:
        context.send_message(chat_id=update.message.chat_id,
                             text=message_snippets.help_message)


def plain_message(context, update):
    if update.channel_post:
        fd = open('media_id.txt', 'a+')
        fd.write(str(update.channel_post.document.file_id) + '\n')
        fd.close()


def start_game(context, update):
    if update.callback_query.data == 'start new game':
        context.editMessageMedia(message_id=update.callback_query.message.message_id,
                                 chat_id=update.callback_query.message.chat.id,
                                 media=media.create_media_2(
                                     media.file_ids_base[1], dict[1][0]),
                                 reply_markup=markup.game_inline_markup(1), parse_mode=telegram.ParseMode.HTML)
    else:
        choose_level(context, update)


def choose_level(context, update):
    if update.callback_query.data in {'top', 'mid', 'bottom'}:
        dispatcher.chat_data[update.callback_query.message.chat.id] = Game(update.callback_query.data)
        game = dispatcher.chat_data[update.callback_query.message.chat.id]
        context.editMessageMedia(message_id=update.callback_query.message.message_id,
                                 chat_id=update.callback_query.message.chat.id,
                                 media=media.create_media_2(media.file_ids_base[3],
                                                            dict[2][0] + '\n\n\n' + print_parametres(game)),
                                 reply_markup=markup.game_inline_markup(2), parse_mode=telegram.ParseMode.HTML)
    else:
        button_press(context, update)


def button_press(context, update):
    print(2)
    game = dispatcher.chat_data[update.callback_query.message.chat.id]
    upd = game.get_parameters_change(update.callback_query.data).split()
    fd = open('updlog.txt', 'a+')
    fd.write(str(upd) + '\n')
    fd.close()
    tmp = list(map(float, upd))
    print(tmp)
    bonus_flag = 0
    if tmp[0] == -101.0:
        bonus_flag = 1
    a, b, c, d = tmp
    end = 0
    if game.score <= 0:
        game.score = 0
    elif game.score >= 10:
        game.score = 10
    if bonus_flag == 0:
        game.karma += a
        game.score += b
        game.free_time += c
        game.mood += d
        end = handle_ending(game)
    else:
        end = 1
    if end or game.case == len(dict) - 1:
        context.editMessageMedia(message_id=update.callback_query.message.message_id,
                                 chat_id=update.callback_query.message.chat.id,
                                 media=media.create_media_2('CgADAgADWgMAAuIKwErA1ZWtsUxoIQI', get_ending(game,
                                                                                                          bonus_flag,
                                                                                                          ) + '\n\n\n' + print_parametres(
                                     game)),
                                 reply_markup=markup.game_inline_markup(0), parse_mode=telegram.ParseMode.HTML)
        game.case = -1
    elif len(dict) - 1 > game.case > 0:
        context.editMessageMedia(message_id=update.callback_query.message.message_id,
                                 chat_id=update.callback_query.message.chat.id,
                                 media=media.create_media_2(media.file_ids_base[game.case],
                                                            dict[game.case + 1][0] + '\n\n\n' + print_parametres(
                                                                game)),
                                 reply_markup=markup.game_inline_markup(game.case + 1),
                                 parse_mode=telegram.ParseMode.HTML)
        game.case += 1


start_handler = CommandHandler('start', start)
help_handler = CommandHandler('help', help)
plain_handler = MessageHandler(Filters.all, plain_message)
callback_handler = CallbackQueryHandler(start_game)
