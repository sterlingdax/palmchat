#! /usr/bin/env python3

# So just the line above doesnt seem to work, have to start using python3 programp.py to start
# New version of Palmchat game

# topic ideas: iphone, ipad, sysadmin, camera gear,
# TV Shows: Mr. Robot, Game of Thrones, narcos

# usernames: aaron, Austin, Cloud_Strife, CosmicRay, dampeoples, irq, liiwi, LonEagle, Mike_W, pilot518, pthree, tomcatt1, Worf

# add random quips from people, just to keep conversation going
# channel topic - Eat your drugs, stay in vegetables and don't do school.

# Syntax for the login:
# print('Comput-0:~ ' + UserName + '$'))

def thedon():
	print('<irq>what the literal fuck?')
	print('<irq>if that situation happened to me, i would hunt down the guy who put a password in 		  it and destroy his family and his next 3 generations of family')
	prompt()
	
	
def change():
	print('<pthree>watch how you speak about Obama! I was able to have TWO children due to 				  Obamacare!')
	print('<pthree>otherwise it would have been too expensive to get them tattooed at such a young 		  age.')
	prompt()
	
	
def phone():
	print('<pthree>my users are confused about these new phones not having a headphone port')
	print("<pthree>I really don't know what to tell them to do, buy adapters?")
	print('<Worf>Amazon has them in the basics line')
	print('<aaron>and here is the aaronzon link!')
	prompt()
	
	
def stream():
	print("<pilot518>now you're talking! Kodi is awesome, I even stay under the radar because I 		  stream, not torrent")
	print("<irq>you do know that you are on this radar? Right?")
	print("<pilot518>what!!? I'm just as bad as those no good torrent thieves!")
	print('<irq>yes, pilot, you are just as evil and terrible as me (you wish!)')
	prompt()


def prompt():
	topic = input('[#palmchat] ')
	topic = topic.lower()
	if "trump" in topic:
		thedon()
	elif "obama" in topic:
		change()
	elif "iphone" in topic:
		phone()
	elif "kodi" in topic:
		stream()
	else:
		prompt()
		







prompt()

	
