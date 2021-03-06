#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 15:29:27 2019


mint vm ip : 192.168.105.151     where we are running our scripts from

our gateway ip : 192.168.105.1
email server ip : 192.168.105.102

NOTICE. These are all the valid assets we could get during my times of doing
coursework, since these were the only ones running at the time of testing.
If these scripts were run on time when all of our group members were present 
the list of valid assets would had been bigger.
Despite the fact that these were the conditions during the testing,
the scripts are made to handle bigger lists of assets also.

@author: Jesse Rontti
"""
#Start by importing namp module for python
#to makes things more clear we put nmp.PortScanner to variable nm
#Next part is to make file of current task 
#using the f.write instead of print makes saves our gathered information 
#to designated txt file instead of just printing it in terminal

import nmap
import time

startTime = time.time()

nm = nmap.PortScanner()

getAssets = nm.scan('192.168.105.0/24', '0-520')

scanData = (getAssets['scan'])

f = open('task4.txt','w')

f.write('Nmap scan results:')
f.write('\n---------------------------------------------------\n')


#print (str(getAssets)) # This is the actual scan
#f.write(str(getAssets)) # This is the actual scan
for address in scanData:
    ipAddress = address
    
    f.write('\n\nIPADDRESS: ' + str(ipAddress) + ' HAS BEEN FOUND.')
    hostName = getAssets['scan'][ipAddress]['hostnames'][0]['name']
    #print (hostName)

    if hostName == '':
        f.write('\nNo host name detected.')

    else:
        f.write('\nHost name: ' + hostName)
        
    try:
        portServices = [] #Create a new list variable called portServices
        tcpList = [] #Create a new list variable called tcpList
        tcpPorts = scanData[ipAddress]['tcp'].keys() #Get the keys for the tcp dictionary
        f.write("The following port(s) are open!")
    
        for port in tcpPorts:
            portService = getAssets['scan'][ipAddress]['tcp'][port]['name']
            product = getAssets['scan'][ipAddress]['tcp'][port]['product']
            version = getAssets['scan'][ipAddress]['tcp'][port]['version']
            extraInfo = getAssets['scan'][ipAddress]['tcp'][port]['extrainfo']
            config = getAssets['scan'][ipAddress]['tcp'][port]['conf']
            tcpList.append(str(port)) #Add port number value to a list variable 
            portServices.append(portService) #Add portServices value to a list variable
            
        f.write('\nTCP Ports: ' + str(tcpList)) #Print a list of open ports
                
    except:
          f.write("\n")
        
f.write('\n\nNmap command line we used to scan : ') #
f.write(str(nm.command_line()))
f.write('\n\nScan attempt details: ')
f.write(str(nm.scaninfo()))

f.write('\n---------------------------------------------------')

f.write("\nScan Complete!")
endTime = time.time()
scanDuration = round(endTime-startTime, 2)

f.write('\nThe duration of the scan was: ' + str(scanDuration) + ' seconds!')
f.close()