import random

from data import commonGreetings


def getMessage(message):
    if message in commonGreetings.keys():
        messages = commonGreetings[message]['data']
        index = random.randint(0, len(messages) - 1)
        if len(messages) == 1:
            index = 0
        print(messages[index])
        return messages[index]
    return None
