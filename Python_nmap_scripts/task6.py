"""
Created on Thu Mar 18 12:25:15 2019

ETHICAL HACKING COURSEWORK TASK 6.

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

lines= []                   # declare our list where we are gonna write the lines of task1.txt file

f=open('task6.txt','w')     # enable writing to our txt file

with open('task1.txt','rt')as in_file:       # copy the task1.txt lines to our list lines
    for line in in_file:
        lines.append(line)

substr = "22"           # Substring to search for, in this case our port
for linenum, line in enumerate(lines):  # For every line in lines, enumerated by linenum,
    index = 0               # Set the search index to the first character,
    str = lines[linenum]	# and store the line in a string variable, str.
    while index < len(str): # While search index is less than the length of the string:
        index = str.find(substr, index)# If substring is located, set search index to that location.
        if index == -1:         # If nothing is found,
            break                   # break out of the while loop. Otherwise,
        print("Line: ", linenum, "Index: ", index) #Print the linenum and index of the located substr.
        ipline = linenum -2 # get the ipaddress line, since we know our format is ip address -newline host name if known -newline openports (portlist) 
        for i, line2 in enumerate(lines):  #another for loop to write the ip addresses in new file
            if i == ipline:         #write the specific ip address line 
                f.write('\n' + lines[ipline])  #newline and ip address from text file1
        tcp_portline=str                                   # declare the tcp list
        f.write('Found our requested port from this list:  ' + tcp_portline)
        index += len(substr)    # Before repeating search, increment index by length of substr. 


f.close()  # close our file since we are not using with open statement what closes the file itself after looping








