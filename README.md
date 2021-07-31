dogeBot is a open source and barebone discord bot which allows anyone to use it however.

Anyone can add this to there discord servers and make it the way they want.

HOW TO USE:
  Before you clone:
  
     1) Register a discord bot at Discord developers portal (https://discord.com/developer).
     You can have a look at this video by Engineer man on how to register a discord app (https://www.youtube.com/watch?v=UX-aMm6EHVo)

     2) To you all the features:

        We have features like Spotify and reddit APIs and to use it you gave to register there apps as well, instructions of which are given below:
          1) Spotify: You will have to register you app (https://developer.spotify.com/dashboard/) and save all the details.
          2) Reddit: You will have to register you app (https://www.reddit.com/prefs/apps) and save all the details.



  Now that you have registered all the APIs and have all the detail.

  Something to be noted here is all the token that you have saved should now be kept private as they allow direct access to the accounts.

  YOU CAN NOW CLONE IT.
  To do that you need to write (git clone https://github.com/hahaharshil/dogeBot) in your terminal.

  After you clone:
  
    1) Now you need to install all the pip packages in you in the host computer, instructions of which are given below:

      1) cd in the dogeBot folder. ($cd dogeBot)

      2) Install all the packages using pip. ($ pip install -r requirement.txt)

    2) Now you have to put in all the saved details in the respective files, instructions of which are given below:
      1) Go to classMain.py, Fill in the discord client token under line #35
      2) Go to redditAPI.py, Fill in all the details under line #8
      3) Go to musicAPI.py, Fill in all the derails under line #8


  Now your bot is ready to run.

  To run the bot just run the classMain.py in the shell.


COMMANDS:

      1) Static messages: staticMessages.py has all the messages that the bot will reply to.
      2)Reddit messages: If you write (doge show memes) it will.
      3)IMDB ratings messages: Write (doge movie <movie name>) then it will give you rating and some derails of the movies.
      4)Spotify message: Write (doge music latest) and it will give you names of some latest Spotify music. If you write (doge playlist) it will give you a playlist suggestion.


UNDERSTANDING THE FILES:

    1) classMain.py is a main file which finally send the messages.
    2) message.py is a file responsible for all the message and response give by the bot.
    3) staticMessages.py is a file responsible for all the hard coded messages.
    4)redditAPI.py is a file which is responsible for responses related to reddit. This can be edited the way you desire and functions can be edited, but for now we have r/meme by default, because why not :P.
    5)musicAPI.py is a file responsible for all the responses related to Spotify and can be edited as you want it.
    6)moviesAPI.py is responsible for responses related to IMDB.


AND YES IT'S NOT Dogebot, IT'S dogeBot.
