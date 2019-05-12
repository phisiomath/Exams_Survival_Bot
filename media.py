import telegram

file_ids_base = ['CgADAgADRAMAAuIKwEqlXGF7fFHeygI',
                 'CgADAgADRQMAAuIKwErL72A1QqV1XQI',
                 'CgADAgADRgMAAuIKwEozpW6MM0y3OQI',
                 'CgADAgADRwMAAuIKwEpjKeqEoBnWrgI',
                 'CgADAgADSAMAAuIKwEocUbTMDLoS8gI',
                 'CgADAgADSQMAAuIKwEqxIA6oddQQfQI',
                 'CgADAgADSgMAAuIKwEohF6RU4h1yzwI',
                 'CgADAgADSwMAAuIKwEo9FqLPjSxXcgI',
                 'CgADAgADTAMAAuIKwEpdmugo7fLJ8QI',
                 'CgADAgADTQMAAuIKwEqo9L1ZjuPlBAI',
                 'CgADAgADTgMAAuIKwEo7giibehNdmgI',
                 'CgADAgADTwMAAuIKwEp9SqqQljr-ogI',
                 'CgADAgADUAMAAuIKwEoaJx2ICtU6vAI',
                 'CgADAgADUQMAAuIKwErGnS__mOzsMAI',
                 'BQADAgADUgMAAuIKwEpktniKpnKzUwI'
                 ]

file_ids_endings = []

def create_media_1(text, gif):
    return telegram.Animation(file_id=gif, caption=text, width=100, height=100, duration=100)

def create_media_2(gif, text):
    return telegram.InputMediaAnimation(media=gif, caption=text)

