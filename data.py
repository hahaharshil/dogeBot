from redditAPI import redditMemes, cursedImages
from spotify import featured_playlists,latest_albums

commonGreetings = {
    'hello': {'showAll': False, 'data': ['helloooo!!', 'nice to see you', 'hey! how are you today? ']},
    'help': {'showAll': True, 'data': ['Under development']},
    'What is your name': {'showAll': False, 'data': ['dogeBot']},
    'do you love me?': {'showAll': False, 'data': ['yes of Couse I love you !', 'you are so sweet I love you !',
                                                   'What what I do without you']},
    'what is your favorite song?': {'showAll': True, 'data': ['Under development']},
    'tell me a joke': {'showAll': False, 'data': ['Under development']},
    'where are you from?': {'showAll': False,
                            'data': ['I was born on the moon where are you from?\n A very lame joke']},
    'send me a playlist': {'showAll': False, 'data': ['Under development']},
    'how much do you earn?': {'showAll': False, 'data': ['jitna aapki beti ek mahine mein udati hai']},
    'tell me a fact': {'showAll': False, 'data': ['Under development']},
    'Is illuminati real?': {'showAll': False, 'data': ['Yes!']},
    'send me a cursed photo': {'showAll': False, 'data': ['Under development']},
    'what is your favorite tv show?': {'showAll': False,
                                       'data': ['I dont mind watching anything. Just want good company.']},
    'Am I a joke to you?': {'showAll': False, 'data': ['I mean you"re a joke to everyone']},
    'who do you work for?': {'showAll': False,
                             'data': ['idk never heard of you', 'you"re some cool brat: ', 'A mistake! I see.']},
    'let\'s have fun': {'showAll': False,
                       'data': ['I am busy', "Let's go to mc Donald's", 'You tell me a joke', 'Like?']},
    'You are so annoying': {'showAll': False, 'data': ['I know ']},
    'what is the time?': {'showAll': False, 'data': ['Developing ']},
    'dogeBot': {'showAll': False, 'data': ['Developing ']},
    'memes': {'showAll': False, 'useFunc': True, 'func': redditMemes,'param' : 'new', 'data': ['Developing ']},
    'cursed memes': {'showAll': False, 'useFunc': True, 'func': cursedImages, 'param': 'new', 'data': ['Developing ']},
    'albums': {'showAll': False, 'useFunc': True, 'func': latest_albums, 'param': 'new', 'data': ['Developing ']},
    'playlists': {'showAll': False, 'useFunc': True, 'func': featured_playlists, 'param': 'new', 'data': ['Developing ']},
}
sampleData = [
    {'intent': 'happy', 'responses': []}
]
