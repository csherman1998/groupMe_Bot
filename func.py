import json
import requests
import string
import random
def getMsg (amount):
	msglst = []
	
	parameters = {"limit": amount}
	response = requests.get("https://api.groupme.com/v3/groups/22484502/messages?token=WJsih8cDTO2WELx3OywvV3j49HrWoqB8xWLmf1DA", params=parameters)
		
	data = response.json()
	
	for x in range(0, amount):
		msglst.append(data["response"]["messages"][x]["name"] + " -  " +  data["response"]["messages"][x]["text"] + "  likes : " + `len(data["response"]["messages"][x]["favorited_by"])`)
		
		if "@bot " in msglst[x].encode("utf-8"):
	
			processMsg(msglst[x].encode("utf-8"))
		#else:
			
			#print (msglst[x].encode("utf-8"))
	return 1


def pstMsg(str):
	rnd =''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) 
	data = {"message":{"source_guid": rnd , "text": str}}	
	send = requests.post("https://api.groupme.com/v3/groups/22484502/messages?token=WJsih8cDTO2WELx3OywvV3j49HrWoqB8xWLmf1DA", json=data)

	print send
	return 1


def processMsg(str):
	rnd = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range (5))
	
	#print "here"
	if "coin flip" in str:
		#print "true"
		coinflip(rnd)
	if "insult" in str:
		insult(rnd)
	if "8ball" in str:
		ball(rnd)
def ball(rnd):
	ballnum = random.randint(1,8)
	if ballnum == 1:
		data = {"message":{"source_guid": rnd, "text" : "it is certain"}}	
		send = requests.post("https://api.groupme.com/v3/groups/22484502/messages?token=WJsih8cDTO2WELx3OywvV3j49HrWoqB8xWLmf1DA", json=data)
		
def insult(rnd):
	data = {"message":{"source_guid": rnd, "text" : "fuck yourself, idiot"}}	
	send = requests.post("https://api.groupme.com/v3/groups/22484502/messages?token=WJsih8cDTO2WELx3OywvV3j49HrWoqB8xWLmf1DA", json=data)
	
def coinflip(rnd):
	coin = random.random()
	if coin < .5:
		#print "heads"
		data = {"message":{"source_guid": rnd, "text" : "heads"}}	

		send = requests.post("https://api.groupme.com/v3/groups/22484502/messages?token=WJsih8cDTO2WELx3OywvV3j49HrWoqB8xWLmf1DA", json=data)

	else:
		data = {"message":{"source_guid": rnd, "text" : "tails"}}
		send = requests.post("https://api.groupme.com/v3/groups/22484502/messages?token=WJsih8cDTO2WELx3OywvV3j49HrWoqB8xWLmf1DA", json=data)
		#print "tails"
