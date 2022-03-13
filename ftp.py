'''
a simple ftp program which performs basic functions
- listing
- changing directories
- downloading files
- uploading files
- showing current working directory
--------------------------
Website : https://v1llur1.ml
Twitter : https://twitter.com/v1llur1
GitHub : https://github.com/v1llur1
---------------------------
'''

from ftplib import FTP
import getpass

def banner():
	print("                                    █" )
	print("                                  ▄█" )
	print("            █                   ▓█▌" )
	print("             █▓▄▄▄▓▓▓██████▓▓▄▄▓█" )
	print("              ████▀           ▓███▓ " )
	print("            ▓█▓██▌            ██▌▀███▄" )
	print("           █▌   ██            █▌   ▀███" )
	print("         ▓█▀     ██          █▌    ▐ ▓██▄" )
	print("        ▓█▀       █▌        █▌     ▐  ▓██▄" )
	print("        ██        ▀█       ██         ▐███" )
	print("       ▐██         █▌     ▓█           ███" )
	print("        ██▌        ██     █▌          ▐███" )
	print("        ▐██▌        █▓   ██           ▓██▌" )
	print("          ███       ██  ██▀          ▓██" )
	print("           ▀██▓      ██▐██         ▄███" )
	print("             ████▄   ████        ▄███▀" )
	print("                ▀██▓▄████▌   ▄▓████▀▀" )
	print("                 ▓▀███████████▓▀▀   " )
	print("                     ███▀" )
	print("                      ██" )
	print("                                      " )
	print("              ░  S H Λ M S I ９ ░" )
	print("                                                    " )
	print("         https://www.twitter.com/v1llur1" )
	print("")

def ask():
	d_ = input('domain@ftp > ')
	u_ = input('username@ftp > ')
	p_ = getpass.getpass(prompt = 'password@ftp > ')
	return d_,u_,p_

def getfile(choice):
	filename = choice[4::]
	localfile = open(filename, 'wb')
	session.retrbinary('RETR ' + filename, localfile.write, 1024)

	localfile.close()

def pushfile(choice):
	filename = choice[5::]
	session.storbinary('STOR ' + filename, open(filename, 'rb'))
'''
session init
'''
banner()

domain,user,passwd = ask()
session = FTP(domain)
# def try_except():
# 	try:
# 		session.login(user = user, passwd = passwd)
# 	except:
# 		print('[!] Access Denied')
# 	domain,user,passwd = ask()
# 	session = FTP(domain)
session.login(user = user, passwd = passwd)	

session.getwelcome()
pwd = session.pwd()

choice = input(user + '@ftp' + pwd + ' > ')

while choice != 'exit':
	print(user + '@ftp' + pwd + ' > ')
	if 'cd' in choice:
		print(user + '@ftp > current dir changed to ' + choice[3::])
		session.cwd(choice[3::])
		pwd = session.pwd()
		choice = input(user + '@ftp' + pwd + ' > ')
	elif 'pwd' in choice:
		pwd = session.pwd()
		choice = input(user + '@ftp' + pwd + ' > ')
	elif 'exit' in choice:
		break
	elif 'ls' in choice:
		pwd = session.pwd()
		session.retrlines('LIST')
		choice = input(user + '@ftp' + pwd + ' > ')	
	elif 'get' in choice:
		pwd = session.pwd()
		getfile(choice)
		choice = input(user + '@ftp' + pwd + ' > ')
	elif 'push' in choice:
		pwd = session.pwd()
		pushfile(choice)
		choice = input(user + '@ftp' + pwd + ' > ')
	else:
		continue