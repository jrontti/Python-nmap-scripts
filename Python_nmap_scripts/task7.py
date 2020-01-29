#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 12:25:15 2019

ETHICAL HACKING COURSEWORK TASK 8.


mint vm ip : 192.168.105.151     where we are running our scripts from

our gateway ip : 192.168.105.1
email server ip : 192.168.105.102

NOTICE. These are all the valid assets we could get during my times of doing
coursework, since these were the only ones running at the time of testing.
If these scripts were run on time when all of our group members were present 
the list of valid assets would had been bigger.
Despite the fact that these were the conditions during the testing,
the scripts are made to handle bigger lists of assets also.

Inspiration from: https://thispointer.com/python-how-to-sort-a-dictionary-by-key-or-value/
https://stackoverflow.com/questions/26825729/extract-number-from-string-in-python/26825781


@author: Jesse Rontti
"""



import re

ipPortDict = {} #Create an empty dictionary

list= []

ipAddPortCount = ""

openPortCount = 0

ipAddress = ""

task7File = open("task7.txt", "w") #Create a task7.txt file object to WRITE to
task4File  = open("task4.txt", "r") #Create a task4.txt file object to READ from

print("\nLIST OF IP ADDRESSES WITH PORT COUNTS IN DESCENDING ORDER:")
task7File.write("LIST OF IP ADDRESSES WITH PORT COUNTS IN DESCENDING ORDER:\n")

for line in task4File: #Loop through each line in the task4.txt file

	if "IPADDRESS:" in line: #For each line in the task4.txt file, check for a match of the following string "The IP address was: " in each line

		ipAddress = line.replace("IPADDRESS: ", "") #Where a match is found, remove it and assign what remains to a variable

	if "TCP Ports: " in line: #For each line in the task4.txt file, check for a match of the following string "The IP address was: " in each line

		ipAddPortCount = line.replace("TCP Ports: ", "").replace("[","").replace("]","").replace("'","").replace("\n","")#Where a match is found, remove it and assign what remains to a variable
        s =ipAddPortCount           #put string into 
        s = re.findall("\d+",s)

        openPortCount = len(s)
        #print("Open Port Count Is: " + str(openPortCount))

	ipPortDict.update({ipAddress.strip('\n'): openPortCount}) #Add the ipAdd variables and the ipAddPortCount varible as a key/value pair to the ipPortDictionary

sortedDict = sorted(ipPortDict.items(), reverse = True, key=lambda x: x[1]) #Sort ther contents of the ipPort Dictionary; based on values and in descending order

for elem in sortedDict: #Loop for all dictionary entries

	print("IP Address: " + elem[0] + " has " + str(elem[1]) + " ports open.")
	task7File.write("IP Address: " + elem[0] + " has " + str(elem[1]) + " ports open.\n")

print("End of process")
task4File.close()
task7File.close()
