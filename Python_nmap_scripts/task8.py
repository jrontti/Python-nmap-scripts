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

@author: Jesse Rontti
"""
import nmap        #allows us to use nmap with python
import sys         #helps us during exiting while true loop, allowing sys_functions

choice_loop = True          #makes our loop work, allowing restart option

while choice_loop:                         #starts loop
    print ('Welcome to Nmap-Python scanner')

    print('\nWhat ip address you want to scan?')
    user_ip = raw_input(' > ')
    user_ip = "'" +user_ip+"'"
    
    
    print('\nDo you want to scan all ports or some specific one?')
    user_choice= raw_input('A/S>')
    if user_choice =='A' or user_choice == 'a':
        searchPort = '0-520'
        searchPort2 = searchPort
    if user_choice =='S' or user_choice == 's':
        print('Select port number 0-520')
        searchPort = raw_input(' > ')
        searchPort2= searchPort
        searchPort = '0-520'
    
    
    print('\nReady to scan?(S)')
    print('I want to change my scan details(R)')
    print('Exit(E)')
    user_choice2 = raw_input ('S  /  R  /  E > ')
    if user_choice2 =='S' or user_choice2 =='s':
        print('Starting scan!')
        break
    if user_choice2 =='R' or user_choice2 =='r':
        continue
    if user_choice2=='E' or user_choice2 =='e':
        sys.exit()
nm = nmap.PortScanner()

getAssets = nm.scan(user_ip, searchPort)

scanData = (getAssets['scan'])

f = open('task8.txt','w')

f.write('Nmap scan results:')
f.write('\n---------------------------------------------------\n')


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
        f.write("\nThe following port(s) are open!")

    
        for port in tcpPorts:
            portService = getAssets['scan'][ipAddress]['tcp'][port]['name']
            product = getAssets['scan'][ipAddress]['tcp'][port]['product']
            version = getAssets['scan'][ipAddress]['tcp'][port]['version']
            extraInfo = getAssets['scan'][ipAddress]['tcp'][port]['extrainfo']
            config = getAssets['scan'][ipAddress]['tcp'][port]['conf']
            tcpList.append(str(port)) #Add port number value to a list variable 
            portServices.append(portService) #Add portServices value to a list variable
            searchTcp = tcpList
        
        if user_choice =='S' or user_choice == 's':
            if searchPort2 in tcpList :
                f.write('\nSearch port: ' + searchPort2 + ' has been found!')
                        #Write ipAddress and relevent data to "found file.txt"           
            else:
                f.write('\nSearch port: ' + searchPort2 + ' not found!')
                        #Write ipAddress and relevent data to "NOT found file.txt"
        f.write('\nTCP Ports: ' + str(tcpList)) #Print a list of open ports
    except:
          f.write("\n")
        
#f.write('\n\nNmap command line we used to scan : ') #
#f.write(str(nm.command_line()))
#f.write('\n\nScan attempt details: ')
#f.write(str(nm.scaninfo()))

print ('Your nmap output was saved in task8.txt file.')

f.write('\n---------------------------------------------------')
f.close()





        
