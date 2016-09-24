# Newwwwwwwwww #Palmchatttttttt
# An, ahem, adventure game in the spirit of Zork, Adventure
# But those games are both tedious and boring, so I decided
# To make a game that was even more tedious and more boring
# By basing it off of my favorite people slash IRC channel
# This, plus a lot of idle time, is exactly what happens

import time
import sys

print("\n" * 80)
UserName = input('Login ID: ')
print('\n' * 80)
time.sleep(1)
print('Comput-0:~ ' + UserName + '$ irssi', end = "")
for i in range (3):
	print('.', end = "")
	time.sleep(1)
print('\n')
print('Welcome to Palmchat')
print("Topic: Eat your drugs, stay in vegetables and don't do school.")

# topic ideas: sysadmin, camera gear,
# TV Shows: Game of Thrones, narcos
# Use the prompt instead of the built in prompt, in possible?
# to make it look like actually using irssi

users = ['aaron', 'Austin', 'Cloud_Strife','CosmicRay', 'dampeoples', 'irq', 'liiwi', 'LonEagle', 		'Mike_W', 'pilot518', 'pthree', 'tomcatt1', 'Worf']


# add random quips from people, just to keep conversation going


def thedon():
	print('<irq>what the literal fuck?')
	print('<irq>if that situation happened to me, i would hunt down the guy who put a password in 		  it and destroy his family and his next 3 generations of family')
	print('<dampeoples>But, but we were talking about Donald Trump?')
	print("<irq>I was too, what's your point?")
	print("<dampeoples>oh... nothing!")
	prompt()
	
	
def pro():
	print("<irq>just what the fuck is so 'pro' about a Retina iPad with a keyboard for a cover?")
	print('<dampeoples>I must be a rookie, I got a Retina iPad Mini and a BT keyboard...')
	print("<irq>that's my point, it's the same thing")
	prompt()
	
	
def change():
	print('<pthree>watch how you speak about Obama! I was able to have TWO children due to 			Obamacare!')
	print('<pthree>otherwise it would have been too expensive to get them tattooed at such a young 	age.')
	print('pilot518>yah social medicine!')
	prompt()
	
	
# Put an actual link here, not sure how to do that in code!
def phone():
	print('<pthree>my users are confused about these new phones not having a headphone port')
	print("<pthree>I really don't know what to tell them to do, buy adapters?")
	print('<Worf>Amazon has them in the basics line')
	print('<aaron>and here is the aaronzon link!')
	prompt()
	
	
def mr():
	print('<pilot518>started watching this show recently')
	print('<dampeoples>yeah me too, I wonder how many people got confused downloading the show     	with the names')
	print('Worf>you mean besides you?')
	print('<dampeoples>...(yes, me)')
	print('<everyone else!> lol!')
	prompt()
	
	
def stream():
	print("<pilot518>now you're talking! Kodi is awesome, I even stay under the radar because I 		  stream, not torrent")
	print("<irq>you do know that you are on this radar? Right?")
	print("<pilot518>what!!? I'm just as bad as those no good torrent thieves!")
	print('<irq>yes, pilot, you are just as evil and terrible as me (you wish!)')
	prompt()
	
	
def code():
	print("<aaron>I think I'm going to write a book about programming in Django and I'm going to 		 call it 'Django Unchained'")
	print('<everyone else>...')
	print('<dampeoples>somethign something smartass-like')
	print("<aaron>good one dampeoples. Don't you have some direct mail pieces to mangle?")
	prompt()


def eye():
	print("<irq>they should call this phone the iPhone 6ss")
	prompt()


def noti():
	print("<tomcatt1>i am not a bot")
	print("<tomcatt1>i I do occasionally come in here and read back to see what's going on")
	prompt()


def food():
	print("<dampeoples>I really need to go get something more appealing than this to eat 😞")
	print("<dampeoples>Boston Market Salisbury Stake TV dinner")
	print("<irq>Stake lol")
	print("<irq>sort of like Cheez")
	print("<irq>perhaps i shall have a Cheez Stake")
	prompt()
	
	
def string():
	print("<LonEagle>Kang broke a mandolin string")
	print(">CosmicRay>yeah, at the Mishawaka Amphitheater")
	print("<Austin>October 6, 1996, i think?")
	prompt()
	
	
def joshua():
	print("<joshua>do you want to play a game")
	game = input('[#palmchat] ')
	game = game.lower()
	if game == 'yes':
		print("<joshua>Love to. How about Global Thermonuclear War.")
	elif game == 'no':
		print("<joshua>The only winning move is not to play")
	else:
		print("<joshua>You have a golden opportunity to talk to a War Games icon and you fuck it up, way to go!")
		prompt()
		
def infocom():
	print("<pthree>You are standing in an open field west of a white house, with a boarded front door. There is a small mailbox here.")
	print("<dampeoples>See! I told you pthree was a robot!")
	print("<aaron>and I thought it was tomcatt!")
	print("<pthree>You were both eaten by a Grue. Game Over Bitches.")
	prompt()
	
	
def freaky():
	print("<dampeoples>I forgot my fucking pants again!")
	print("<dampeoples>I just have two options...")
	print("<Cloud_Strife>also, while dp is here, anyone notice his only options are rubber and leather?")
	print("dampeoples smacks Cloud_Strife with a large trout")
	prompt()

	
# The <Worf> strikethrough looks funny on the f, is it just because of the casing, or should I find another person to be Colonel	
def monty():
	print("[Console] wget http://www.fish-slapping-dance.mov")
	print("<Cosmic_Ray>Ah yeah, classic, that's a good one!")
	print("<irq>That's one of my favorite Monty Python Sketches, when the guy whips out that large fish, I fell out of my chair!")
	print("\u0336".join('<Worf>') + "\u0336""<Colonel>Right! Stop That! It's far too silly!")
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
	elif "ipad" in topic:
		pro()
	elif "robot" in topic:
		mr()
	elif "program" in topic:
		code()
	elif "iphone" in topic:
		eye()
	elif "lurk" in topic:
		noti()
	elif "eat" in topic:
		food()
	elif "game" in topic:
		joshua()
	elif "cheese" in topic:
		string()
	elif "zork" in topic:
		infocom()
	elif "pants" in topic:
		freaky()
	elif "trout" in topic:
		monty()
	elif "quit" in topic:
		sys.exit('Goodby!')
	else:
		print("<pthree>ever since the string cheese incident, we don't speak of that here")
		prompt()
		
prompt()

	
