import time
from func import getMsg, pstMsg

while(1):
	getMsg(1)
	time.sleep(2)

str = input("How many messages to load?");

getMsg(str)


inp = raw_input("send a message ");
pstMsg(inp)


