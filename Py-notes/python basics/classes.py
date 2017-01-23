# learnpythonthehardway exercise.

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around that family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Notes
	# think of classes like mini modules except that you are not importing them from outside
	# you declare a class and then instantiate it, i.e create an object for it. 
	# Classes are like blueprints or definitions for creating new mini-modules.
	# Instantiation is how you make one of these mini-modules and import it at the same time. 
	# "Instantiate" just means to create an object from the class.
	# The resulting created mini-module is called an object and you then assign it to a 
	# variable to work with it.
