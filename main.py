import os 
import requests
import json
from pystyle import Colors, Colorate, Center, Write
import random
import threading
from win10toast import ToastNotifier
import string

proxies = []
proxyneed = False
created = 0
tries = 0
for proxie in open('data/proxies.txt'):
	proxies.append(proxie)


if os.name == 'nt':
    toast_noti = ToastNotifier()


class AeroUtils:

	def trigger_notification(title, desc):
		toast_noti.show_toast(f'{title}', desc, duration=3, threaded=True)
       

	def clear():
		os.system("cls")

	def title(t):
		os.system(f'title '+t)

	def print(type_, text):
		if type_ == "success":
			print(Colorate.Color(Colors.green, " "*4+"[+] "+text, True))
		if type_ == "error":
			print(Colorate.Color(Colors.red, " "*4+"[!] "+text, True))
		if type_ == "normal":
			print(Colorate.Horizontal(Colors.blue_to_purple, " "*4+text, 1))


	def randomNumber(min_, max_):
		return random.randint(min_, max_)

	def randomInsult():
		return requests.get('https://insult.mattbas.org/api/insult.txt').text

	def randomString(n):
		return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(n))


class DiscordThread:

	def create(token, channel_id, name):
		global created
		global tries
		try:
			try:
				current_proxy = random.choice(proxies)
			except:
				pass
			header = {"content-type": "application/json", "Authorization": token}
			if proxyneed == True:
				r = requests.post(f"https://canary.discord.com/api/v9/channels/{channel_id}/threads", headers=header, json={"name": name, "type": 11, "auto_archive_duration": 60}, proxies=current_proxy)
			else:
				r = requests.post(f"https://canary.discord.com/api/v9/channels/{channel_id}/threads", headers=header, json={"name": name, "type": 11, "auto_archive_duration": 60})
			r_id = r.json()['id']
			if proxyneed == True:
				AeroUtils.print("success", f"Thread Created ! ({r_id}) [{current_proxy}]")
				created = created + 1
			else:
				AeroUtils.print("success", f"Thread Created ! ({r_id})")
				created = created + 1
		except:
			tries = tries + 1
		AeroUtils.title(f'Aero • Started • {created} Threads Created • {tries} Try')







banner = """


    :::     :::::::::: :::::::::   ::::::::  
  :+: :+:   :+:        :+:    :+: :+:    :+: 
 +:+   +:+  +:+        +:+    +:+ +:+    +:+ 
+#++:++#++: +#++:++#   +#++:++#:  +#+    +:+ 
+#+     +#+ +#+        +#+    +#+ +#+    +#+ 
#+#     #+# #+#        #+#    #+# #+#    #+# 
###     ### ########## ###    ###  ########  


"""


menu = """

+══════════════════════════════+
|	 [1] Thread Creator          |
|  [2] Soon                    |
|  [3] Soon                    |
|  [4] Soon          	         |		     
+══════════════════════════════+

"""

def floodthread(token, channel_id, name):
	global created
	while True:
		if name.lower() == "insult":
			DiscordThread.create(token, channel_id, AeroUtils.randomInsult())
		if name.lower() == "numbers":
			DiscordThread.create(token, channel_id, AeroUtils.randomNumber(0, 1000))
		if name.lower() == "string":
			DiscordThread.create(token, channel_id, AeroUtils.randomString(16))
		else:
			DiscordThread.create(token, channel_id, name)

def main():
	global created
	created = 0
	AeroUtils.clear()
	AeroUtils.title(f'Aero • Main Menu • {len(proxies)} Proxies Loaded')
	AeroUtils.print("normal", Center.XCenter(banner))
	AeroUtils.print("normal", "\n"+Center.XCenter(menu))
	choice = Write.Input("\n"*3+" "*16+'[?] >> ', Colors.blue_to_purple, interval=0.0025)

	if choice == "1":
		token = Write.Input("\n"*2+" "*16+'[?] Token >> ', Colors.blue_to_purple, interval=0.0025)
		channel_id = Write.Input(" "*16+'[?] Channel ID >> ', Colors.blue_to_purple, interval=0.0025)
		name = Write.Input(" "*16+'[?] Name Type (custom/insult/numbers/string) >> ', Colors.blue_to_purple, interval=0.0025)
		if name.lower() == "custom":
			name = Write.Input(" "*16+'[?] Name >> ', Colors.blue_to_purple, interval=0.0025)
		proxy = Write.Input(" "*16+'[?] Proxy (y/n) >> ', Colors.blue_to_purple, interval=0.0025)
		if proxy.lower() == "y":
			proxyneed = True
		else:
			proxyneed = False
		AeroUtils.clear()
		for i in range(100):
			x = threading.Thread(target=floodthread, args=(token, channel_id, name,))
			x.start()
		AeroUtils.trigger_notification('Successfully', 'Started creating threads !')






main()