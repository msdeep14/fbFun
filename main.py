import fbchat
from fbchat import Client
from fbchat.models import *
from getpass import getpass


email = str(raw_input("email: "))
# client = fbchat.Client(username, getpass())

client = Client(email, getpass())#, session_cookies=session_cookies)

# session_cookies = client.getSession()
# client.setSession(session_cookies)

friend = str(raw_input("friend name: "))
users = client.searchForUsers(friend)
uid = 0
name = 'temp'
if len(users) is not 0:
	print users[0]
	uid = format(users[0].uid)
	name = format(users[0].name)
else:
	print "invalid user\nexiting..."


val = input("enter 1 to send message ")
if val == 1 and uid is not 0:
	msg = str(raw_input("message: "))
	# set lval to the number of times the message has to be sent
	lval = 50
	for i in range(lval):
		print "sending message"
		# comment the section if you don't want to send emoji or image
		client.sendMessage(msg, thread_id = uid, thread_type = ThreadType.USER)
		client.sendLocalImage('/home/mandeep/1.jpg', message='caption', thread_id=uid, thread_type=ThreadType.USER)
		# it vl send default emoji, you can also set as per your choice
		# client.sendEmoji(emoji=None, size=EmojiSize.LARGE, thread_id=uid, thread_type=ThreadType.USER)
else:
	print "exiting..."

# if you want to get all messages in chat(limit = 10, means it will fetch last 10 messages)
messages = client.fetchThreadMessages(thread_id=uid, limit=10)
messages.reverse()

# save it to text file
lst = []
for message in messages:
	s = message.text
	s = str(s.encode('utf-8'))
	lst.append(s)

filename = name+'.txt'
myfile = open(filename,'w+')
for s in lst:
	s = s+"\n";
	myfile.write(s)
myfile.close()


# client.sendMessage('Hello', thread_id='<user id>', thread_type=ThreadType.USER)
# own_id = client.uid

client.logout()

# def main():
	

# if __name__ == "__main__":
#      main()
