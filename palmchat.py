# topics include ham radios, politics, art, motorcycles, cars, palm pilots, 
# computers, movies, music, maybe all under topic class, or subclass?

from sys import exit
import time
import random


print ">_Login ID:"
login = raw_input (">_")
print ">_irssi"
time.sleep(2) 

#look for a way to pass this time, maybe with dots?

print ">_/connect irc.oftc.net"
time.sleep(2)
print ">_/join #Palmchat"
time.sleep(3)
print ">_The topic for #Palmchat is:  Pilot_518: Am I happy or sad"
# Change this to a dictionary or something besides a list, for practice
users = ['Mike_W','irq','aaron','pthree','liiwi','Worf','Austin','CosmicRay',
		 'pilot518','tomcatt1','ranc0r','dampeoples']
print ">_%s: Hi" % login
time.sleep(2)
print ">_%s: Hello " % random.choice (users) + "%s" % login
print ">_%s: Hi" % random.choice (users)


# These have to be moved below!! Can't run without first defining them
# Topic class, includes start 'room' as well as any programmed topics
def topic():
	prompt = raw_input(">_%s") % login
	if "ham" in prompt:
		return 'ham'
	if "bush" in prompt:
		return 'bush'
	if "obama" in prompt:
		obama()


def bush():
	print ">_aaron: I blame Bush!"
	print ">_aaron: come to think of it..OBAMA too!"
	print ">_pilot518: None of them top Reagan, amirite?", login

	reply = raw_input(">_%s:") % login
		
	if reply == "yes":
		print ">_pilot518: Mr. Gorbachev, tear down this wall!"
		return 'topic'
	elif reply == "no":
		print ">_aaron: I blame Bush!"
		return 'topic'
	else:
		print ">_aaron: What are you, some sort of Tea party Hack?"
		return 'topic'


def ham():
	print ">_Mike_W: I like radios!"
	print ">_irq: You mean HAM radio, if you going to talk about it, get it right!"
	print ">_Mike_W: ...What do you think", login, "does it matter?"

	reply = raw_input(">_%s:") % login

	if reply == "yes":
		print ">_irq: Of course it matters,", login, "agrees"
		return 'topic'
	elif reply == "no":
		print ">_Mike_W: See,", login, "gets the point, it's time you did!"
		return 'topic'
	else:
		print ">_irq: If you didn't care, why did you ask?"
		return 'topic'


def obama():
	print ">_aaron: oh Obama, don't you lie to me..."
	print ">_pthree: Shut your mouth! I could afford to have two kids under obamacare!"
	print ">_Worf: Canada's medicine has a waiting list"
	return 'topic'



topic()

