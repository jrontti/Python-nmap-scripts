"""
Created on Thu Mar 16 12:25:15 2019

ETHICAL HACKING COURSEWORK TASK 5.


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

nm = nmap.PortScanner()

getAssets = nm.scan('192.168.105.0/24', '0-520')

scanData = (getAssets['scan'])

f = open('task5a.txt','w')
g = open('task5b.txt','w')

ipcount = 0
ipcount2 = 0
portcount = 0
portcount2 = 0

f.write('Nmap scan results:')
f.write('\n---------------------------------------------------\n')



for address in scanData:
    ipAddress = address
    
    if ipAddress != "" and nm[ipAddress].has_tcp(22):
        ipcount +=1
        f.write("\n" +str(ipcount)+". ASSET FOUND WITH OPEN PORTS")
        f.write('\nIPADDRESS: ' + str(ipAddress) + ' HAS BEEN FOUND.')
        hostName = getAssets['scan'][ipAddress]['hostnames'][0]['name']
        if hostName == '':
            f.write('\nNo host name detected.')

        else:
            f.write('\nHost name: ' + hostName)
               
            try:
                portServices = [] #Create a new list variable called portServices
                tcpList = [] #Create a new list variable called tcpList
                tcpPorts = scanData[ipAddress]['tcp'].keys() #Get the keys for the tcp dictionary
                f.write("\nThe following port(s) are open!")
    
                for port in tcpPorts:
                    portcount = portcount +1
                    portService = getAssets['scan'][ipAddress]['tcp'][port]['name']
                    product = getAssets['scan'][ipAddress]['tcp'][port]['product']
                    version = getAssets['scan'][ipAddress]['tcp'][port]['version']
                    extraInfo = getAssets['scan'][ipAddress]['tcp'][port]['extrainfo']
                    config = getAssets['scan'][ipAddress]['tcp'][port]['conf']
                    tcpList.append(str(port)) #Add port number value to a list variable 
                    portServices.append(portService)

                f.write('\nTCP Ports: ' + str(tcpList) + '\n') #Print a list of open ports
            except:
                f.write("\n")
          
          
          
    else:
        ipcount2 +=1
        g.write("\n" +str(ipcount2)+". ASSET FOUND WITHOUT OPEN PORTS\n")
        g.write('\nIPADDRESS: ' + str(ipAddress) + ' HAS BEEN FOUND.')
        hostName = getAssets['scan'][ipAddress]['hostnames'][0]['name']
        if hostName == '':
            g.write('\nNo host name detected.')

        else:
            f.write('\nHost name: ' + hostName)

f.write('\n---------------------------------------------------')
f.close()
g.close()