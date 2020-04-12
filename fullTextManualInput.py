
'''
Kendra Lepage
Send full text with number input
/double cheeked up/

'''
import os

from subprocess import Popen, PIPE
def send_Message():
    getFile=input(str("Enter file name: ")) #get file name
    infile=open(getFile, 'r') #open file
    number=input(str("Enter phone number: "))#get phone number
    words=infile.read()#set message
    #start applescript
    scpt = '''on run {targetBuddyPhone, targetMessage}
            tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy targetBuddyPhone of targetService
            send targetMessage to targetBuddy
            end tell
            end run'''
    #end applescript
    args = [number, words] #set arguments
    p = Popen(['osascript', '-'] + args, stdin=PIPE, stdout=PIPE, stderr=PIPE, universal_newlines=True)
    stdout, stderr = p.communicate(scpt) #pass arguments
           

           

send_Message() #full send
