from typing import List, Any, Union
from media import file_ids_base, file_ids_endings

dict = [['Start game', 'Start'], [
    'Совсем скоро каждого студента Вышки ждут волшебные недели — период летней сессии. Основываясь на собственном опыте, мы создали симулятор сессии. Необходимо выбрать одного из трех персонажей и пытаться дойти до конца. Тебя ждут подготовка к экзаменам, нарушения регламента ВШЭ, добрые лекторы и умные одногруппники. Удачи!',
    'Топ рейтинга', 'Тот бюджетник со стипендией',
    'А 3,49 округляется наверх?'],
        ['Экзамен на носу, а препод не прислал материалы для подготовки. Твои действия:',
         'Напишу преподу на почту', 'Пну старосту',
         'Буду ботать все начиная с первой лекции', 'Забью и не буду ничего учить',
         'Поставлю преподу в СОПе 1'],

        [
            'Грядет устный экзамен. Препод прислал 100+ билетов для подготовки. Как ты поступишь?',
            'Начну писать билеты заранее',
            'Разделю написание билетов с друзьями',
            'Буду ждать, пока билеты напишут друзья',
            'Буду надеяться выехать на своих знаниях'],

        [
            'Утром тебя ждет экзамен, ты уже отложил ботку в сторону и лежишь в перед сном скроллишь ленту. Всплывает сообщение от одногруппника «спишь?».',
            'Проигнорирую - я закончил ботать сегодня!',
            'Скажу, что ничего не учил', 'Объясню билет'],

        ['Препод за пару дней до экзамена меняет формулу не тебе на руку',
         'Схожу в учебный офис', 'Нажму выразительную кнопку', 'Смирюсь'],

        [
            'Умный друг может рассказать тебе все билеты к экзамену перед самим экзаменом, а сейчас вышла новая серия любимого сериала.',
            'Конечно, серия!', 'Сегодня поботаю, а посмотрю завтра'],

        ['Прямо перед экзаменом ты понял, что ничего не знаешь.',
         'Куплю справку', 'Буду надеяться списать у друга',
         'Буду надеяться на божью помощь', 'Найду, у кого скатать шпору',
         'Приму ускорители', 'Я не могу совсем ничего не знать'],

        [
            'Друг, который не очень хорошо списывает и частенько попадается на этом, просит у тебя скатать на экзамене. Что решишь?',
            'Дам списать', 'Не дам списать'],

        [
            'В другом городе проходит событие, которого ты ждал несколько лет. Можно пропустить экзамен и поехать, но сдавать потом придется лектору один на один.',
            'Такое событие нельзя пропустить, поеду!',
            'Ни за что не сдам лектору лично, не еду!'],

        [
            'Сидишь на экзамене и вдруг звонит твой телефон. Это HR компании, в которую ты мечтал попасть стажером очень давно и уже прошел пару собеседований. Они которые готовы позвать тебя на финальное собеседование.',
            'Отвечу и получу 0 за экз. Оно того стоит', 'Не отвечу',
            'Не беру телефон на экзамены!'],

        ['Устный экзамен. Кому пойдешь сдавать?',
         'Лектору', 'Своему семинаристу ', 'Ассистенту',
         'Буду сидеть до последнего, судьба решит'],

        ['Выбери свою манеру сдачи устного экзамена.',
         'Шутишь и затираешь золотые цитаты препода',
         'Льёшь много воды объемно и долго', 'Коротко и по делу'],

        ['Ну что, списываем?',
         'Классические шпоры', 'Телефон', 'Умные часы', 'Выйти в туалет и спросить друга',
         'Не списываю!'],

        [
            'Экзамены закончились, начались апелляции. Приходишь на апелляцию и видишь, что тебе поставили балл за номер, который ты не решал.',
            'Уйду, пока не заметили, и порадуюсь', 'Скажу честно, что завысили',
            'Буду пытаться отбить и за другие номера',
            'Допишу номер и скажу, что не увидели',
            'Что такое апелляция? Я уже еду отдыхать'],

        ['Узнал про изичный отбор на хорошую стажировку.',
         'Кину инфу в групповой чат - альтруист',
         'Скажу ближайшим однокурсникам',
         'Не скажу никому и никто не узнает']
        ]

endings_based_on_scores = ['Что ты ждал со своей-то кармой? Вселенная зла на тебя. Отчислен.',
                           'С твоей кармой тебе уже можно на небеса.',
                           'Настроение 10 эмо-девочек из 10.',
                           'Вселенная не любит таких счатливых людей, на тебя упала сосулька. Летом.',
                           'Зачем нужен универ, когда свободного времени больше чем часов в сутках? Уехал в кругосветное путешествие.',
                           'Рекорд человека без сна составляет 19 суток и это не твой рекорд.']

bonus_ending = {1: '''СОП подкрался из-за угла\n\nТы забыл пройти СОП и это вывело тебя из эмоционального равновесия.''',

                2: '''Умер от болевого шока\n\nУчил, учил. Выучил 100 билетов, а достался 101ый.''',

                3: '''Умер от проклятия\n\nКто же знал, что твой одногруппник мастер проклятий?..''',

                5: '''Ушел в запой\n\nПеред просмотром серии ты увидел спойлер и дальше было невозможно жить.''',

                6: '''Нелегальная медицина это опасно\n\nПроверенная клиника оказалась шаражкой, как и твое новое место обучения.''',

                7: '''Город просыпается без тебя\n\n Ты был не осторожен и не дал списать главе Мафии Дубков.''',

                8: '''Умер от зависти\n\nНа экзамене лектор раздавал халявные оценки и ты не смог это пережить."''',

                13: '''Умер от угрызений совести''',

                61: '''Умер от своей лжи\n\nТы же топ рейтинга! Что-то ты точно знаешь, а может даже и больше.'''}

good_ending = ['Что мы говорим богу пересдач? Не сегодня!',
               'Скатился... Или переоценил свой уровень! Попробуй еще раз.',
               'Собеседование на комиссию пройдено.']


def get_ending(game, bonus_flag):
    if bonus_flag:
        if game.level == 'top' and game.case == 7:
            return bonus_ending[61]
        if game.case - 1 in bonus_ending:
            return bonus_ending[game.case - 1]
    if game.case > 1:
        if game.score >= 4:
            return good_ending[0]
        if game.score < 4:
            return good_ending[2]
    return endings_based_on_scores[(game.case + 1) * (-1) - 1]


def handle_ending(game):
    end = 1
    if game.karma < -100:
        game.case = -2
    elif game.karma > 100:
        game.case = -3
    elif game.mood < -100:
        game.case = -4
    elif game.mood > 100:
        game.case = -5
    elif game.free_time > 100:
        game.case = -6
    elif game.free_time < -100:
        game.case = -7
    else:
        end = 0
    return end

# def update_write(game):
