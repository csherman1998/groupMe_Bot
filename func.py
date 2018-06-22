import json
import requests
import string
import random
import time 
import logging
import wikipedia
import time
import os
import datetime


from weather import Weather, Unit

startTime = time.time()
api_key = os.environ.get("api_key")
logging.getLogger("requests").setLevel(logging.WARNING)

def getMsg (amount):
	msglst = []
	
	parameters = {"limit": amount}
	response = requests.get("https://api.groupme.com/v3/groups/22484502/messages?token="+api_key, params=parameters)
		
	data = response.json()
	
	for x in range(0, amount):
		msglst.append(data["response"]["messages"][x]["text"])
		#print msglst[x]
		if msglst[x] is not None and "@bot " in msglst[x].encode("utf-8") :
			processMsg(msglst[x].encode("utf-8"))
		
	return 1

			

def send(str):

	rnd =''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) 
	data = {"message":{"source_guid": rnd , "text": str}}	
	send = requests.post("https://api.groupme.com/v3/groups/22484502/messages?token="+api_key, json=data)

	return 1


def processMsg(strn):
	rnd = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range (5))
	
	#print "here"]
	if "rape" in strn:
		send("live rape")
	if "coin flip" in strn:
		#print "true"
		coinflip()
	elif "insult" in strn:
		insult()
	elif "8ball" in strn:
		ball(random.randint(1,8))
	elif "uptime" in strn:
		 getUptime()
	elif "weather" in strn:	
		weather()
	elif "help" in strn:
		help()
	elif "forecast" in strn:
		if "spring" in strn:
			forecast(spring)
		elif "cstat" in strn:
			forecast("cstat")
	elif "poll" in strn:
		poll()
	elif "wiki" in strn:
		ex = strn.split("wiki",1)[1] 
		#print ex
		wiki(ex)
	elif "rate" in strn:
		
		if "fr" in strn:
			rate(False)
		else: 
			rate(True)

def rate(severity):
	if severity:
		send("" + str(round(random.uniform(1.0,10.0),2)))
	else:
		send("" + str(round(random.uniform(6.0,10.0),2)))
def poll():
	people = ["Nathan","Chris","Ross", "Eric","Sam", "Bri", "Jeremy", "Alejandro", "Nate", "Christian", "Sean","Will", "James", "Trav", "Jackson", "Logan", "CG", "Kas", "Kaeman"]
	send(people[random.randint(1,len(people)-1)])

def wiki(search_string):
		
	try:
		str  = wikipedia.summary(search_string)
		send(str)
	except wikipedia.exceptions.DisambiguationError as e:
		send("ambigious, options : " + e.options)	
	except wikipedia.exceptions.PageError as f:
		send("uh, cringe... " + search_string + " doesn't exist, tf")
	except wikipedia.exceptions.WikipediaException as g:
		send("little fucko boingo")
def help():
	send("options : 'insult' : roast yourself, '8ball' : game, 'uptime' : uptime counter, 'weather' : spring and college station weather , 'coin flip': flip a coin")
def weather():
	weather = Weather(unit=Unit.FAHRENHEIT)
	lookup = weather.lookup(12590027)
	condition = lookup.condition
	

	springLookup = weather.lookup(2497763)
	springCondition = lookup.condition
	
	send("College Station : " + condition.text + " Spring : " + springCondition.text)
	
def forecast(strn):
	weather = Weather(unit=Unit.FAHRENHEIT)
	if strn == "cstat":
		lookup = weather.lookup(12590027)
		forecasts = lookup.forecast
		text = ""
		print len(forecasts)
		for forecast in forecasts:
			text += forecast.text + " "
			text += forecast.date + " " 
    		text += "high: " + forecast.high + " "
    		text += "low : " + forecast.low + " "

    	print(text)
    	send(text)
def ball(ballnum):
	
	message = ""
	if ballnum == 1:
		message = "it is certain"
		
	elif ballnum == 2:
		message = "Outlook is good"
		
	elif ballnum == 3:
		message =  "You may rely on it"
		
	elif ballnum == 4:
		message = "Shut the fuck up retard"
		
	elif ballnum == 5:
		message ="cringe^"
		
	elif ballnum ==6:
		message = "paise on a childd"
		
	elif ballnum ==7:
		message = "My reply is no"
			
	elif ballnum == 8:
		message = "Don't count on it"

	
	send(message) 
	return 1


def insult():
	send("fuck yourself, idiot")

def coinflip():
	coin = random.random()
	if coin < .5:
		send("heads")
	else:
		send("tails")

def getUptime():
    
	time_seconds = time.time() - startTime
	send(str(datetime.timedelta(seconds=time_seconds)))
