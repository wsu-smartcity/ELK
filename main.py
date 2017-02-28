from ftplib import FTP
def grabFile():
	filename = 'SET_B1.txt'

        #changing current directory
        ftp.cwd('/SETTINGS/')
	localfile = open(filename, 'wb')
	ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
	ftp.quit()
	localfile.close()
ftp = FTP('YOURIP')
ftp.login(user='YOURUSER', passwd='YOURPASS')


grabFile()
