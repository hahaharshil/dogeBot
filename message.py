import random

from data import commonGreetings


def getMessage(message):
    if message in commonGreetings.keys():
        msg = commonGreetings[message]
        messages = commonGreetings[message]['data']
        if 'useFunc' in msg:
            return msg['func']()
        index = random.randint(0, len(messages) - 1)
        if len(messages) == 1:
            index = 0
        return messages[index]
    return None
