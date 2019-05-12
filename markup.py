from telegram.ext import InlineQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import telegram
import handlers
import cases
from dict import dict


def game_inline_markup(case):
    if case > 1:
        button_list = [InlineKeyboardButton(dict[case][s], callback_data=str(case) + ' ' + str(s)) for s in
                       range(1, len(dict[case]))]
    elif case == 0:
        button_list = [InlineKeyboardButton(dict[case][1], callback_data='start new game')]
    elif case == 1:
        levels = ['top', 'mid', 'bottom']
        button_list = [InlineKeyboardButton(dict[case][i], callback_data=levels[i - 1]) for i in
                       range(1, len(dict[case]))]

    def build_menu(buttons,
                   n_cols,
                   header_buttons=None,
                   footer_buttons=None):
        menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
        if header_buttons:
            menu.insert(0, header_buttons)
        if footer_buttons:
            menu.append(footer_buttons)
        return menu

    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
    return reply_markup
