import random


commonGreetings = {
    'doge hello': {'showAll': False, 'data': ['helloooo!!', 'nice to see you', 'hey! how are you today?']},
    'doge help': {'showAll': True, 'data': ['Under development']},
    'doge What is your name': {'showAll': False, 'data': ['dogeBot']},
    'doge do you love me?': {'showAll': False, 'data': ['yes of Couse I love you !', 'you are so sweet I love you !',
                                                   'What what I do without you']},
    'doge what is your favorite song?': {'showAll': True, 'data': ['Under development']},
    'doge tell me a joke': {'showAll': False, 'data': ['Under development']},
    'doge where are you from?': {'showAll': False,
                            'data': ['I was born on the moon where are you from?\n A very lame joke']},
    'doge send me a playlist': {'showAll': False, 'data': ['Under development']},
    'doge how much do you earn?': {'showAll': False, 'data': ['jitna aapki beti ek mahine mein udati hai']},
    'doge tell me a fact': {'showAll': False, 'data': ['Under development']},
    'doge is illuminati real?': {'showAll': False, 'data': ['Yes!']},
    'doge send me a cursed photo': {'showAll': False, 'data': ['Under development']},
    'doge what is your favorite tv show?': {'showAll': False,
                                       'data': ['I dont mind watching anything. Just want good company.']},
    'doge am I a joke to you?': {'showAll': False, 'data': ['I mean you"re a joke to everyone']},
    'doge who do you work for?': {'showAll': False,
                             'data': ['idk never heard of you', 'you"re some cool brat: ', 'A mistake! I see.']},
    'doge let\'s have fun': {'showAll': False,
                        'data': ['I am busy', "Let's go to mc Donald's", 'You tell me a joke', 'Like?']},
    'doge You are so annoying': {'showAll': False, 'data': ['I know ']},
    'doge what is the time?': {'showAll': False, 'data': ['Developing ']},
}

def getMessage(message):
    if message in commonGreetings.keys():
        msg = commonGreetings[message]
        messages = commonGreetings[message]['data']
        index = random.randint(0, len(messages) - 1)
        if len(messages) == 1:
            index = 0
        return messages[index]
    return None
