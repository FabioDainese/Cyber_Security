#!/usr/bin/env python3
import subprocess
import re
import sys
import datetime

#Quick overview of the regexes used. They will be explained in more detail at the time of their use
#Regex used to extract the informations from the equations (with both 2 and 3 parameters and also containing parentheses)
reg = re.compile('[^0-9]*([({]*)\s*([0-9]+)\s*([+\-*/%^]+)\s*([({]*)\s*([0-9]+)\s*([)}]*)\s*([+\-*/%^]*)\s*([0-9]*)\s*([)}]*)')
#Regex used to extrapolate the 'color' from the question "What is the color of Napoleon's <actual_color> horse?"
reg2 = re.compile('[A-Z][a-z\s]*([A-Z][a-zA-Z\s-]*)\sNapoleon')
#Regex used to extrapolate the 'name' contained in the question "How long is the name <actual_name>?"
reg3 = re.compile('How long is the name ([a-zA-Z-\s]*)\?')
#Regex used to extrapolate the 'year' of birth contained in the string "... is born in <actual_year>"
reg4 = re.compile('.*is born in ([0-9]*).*')
#Regex used to understand if we answered all the question, basically if the program is finished (giving us the flag)
reg5 = re.compile('.*Goodbye.*')

#Dictionary containing the formal definition of all algebraic operations. They will be used in sync with the extrapolated data thanks to the first regex to calculate the outcomes
operators = { '+': (lambda x,y : x+y),'*': (lambda x,y: x*y),'/': (lambda x,y: x//y),'-': (lambda x,y: x-y),'%': (lambda x,y: x%y),'^': (lambda x,y: x**y) }

#Function that reads a Byte (character) at a time and saves it on an accumulator (string) which will then be returned as soon as it contains a given pattern of characters
def read_until(stream, pattern):
    r=''
    while pattern not in r:
        b = stream.read(1).decode()
        sys.stdout.flush()
        r += b
    return r

#Execution of the 'alienquiz' program
process = subprocess.Popen("Resources/./alienquiz-32",stdin=subprocess.PIPE,stdout=subprocess.PIPE)

#Starting to analyze the output that prints 'alienquiz'
while True:
    #I recall the previous function to read the various questions of the 'alienquiz' program (all the strings of the program end with the ':' symbol)
    input_str = read_until(process.stdout,': ')
    print(input_str)

    #If the string returned by the function is of the form ({NUMBER OPERAND ({NUMBER}) OPERAND NUMBER}) <- To specify that the parentheses, the third number and/or the second operand may not even be present
    if reg.match(input_str):
        #Recover the 1st and 2nd NUMBER and the 1st OPERAND calling up the respective groups of the regex
        st = reg.match(input_str).group(2)
        st_op = reg.match(input_str).group(3)
        nd = reg.match(input_str).group(5)

        #If the string contains a third NUMBER (identified by the regex group number 8)
        if reg.match(input_str).group(8):
            #Recover the 3rd NUMBER and the 2nd OPERANDO calling up the respective groups of the regex
            nd_op = reg.match(input_str).group(7)
            rd = reg.match(input_str).group(8)
            #If the equation contains a parenthesis immediately after the 2nd NUMBER, it means that the equation is of the form: {(NUM OPER NUM)} OPER NUM
            if reg.match(input_str).group(6)==')' or reg.match(input_str).group(6)=='}':
                #Calculate the equation result using the previously built dictionary
                res = operators[nd_op](operators[st_op](float(st),float(nd)),float(rd))
            else:
                #Otherwise, it means that the equation is of the form: NUM OPER {(NUM OPER NUM)} and I calculate the result
                res = operators[st_op](float(st),operators[nd_op](float(nd),float(rd)))
        else:
            #Otherwise, it means that the equation is of the form: NUM OP NUM and I calculate the result
            res = operators[st_op](float(st),float(nd))

        #Convert/Encode the found result and insert it as input to the 'alienquiz' program
        process.stdin.write((str(res)+'\n').encode())
        process.stdin.flush() # flushes the write to the program
    else:
        #Otherwise, it means that the string read is not an equation, but rather a textual question
        #If the string contains the word 'Napoleon' <- Substring of one of the 'alienquiz' questions
        if reg2.search(input_str):
            #Retrieve the 'color' (formed by a single word starting with a capital letter), convert it and insert it as input to the 'alienquiz' program
            process.stdin.write((reg2.search(input_str).group(1)+'\n').encode())
        elif reg3.search(input_str):
            #Otherwise, if the string contains the phrase "How long is the name ...", I retrieve the 'name', calculate its length, convert it and insert it as input to the 'alienquiz' program
            process.stdin.write((str(len(reg3.search(input_str).group(1)))+'\n').encode())
        elif reg4.search(input_str):
            #Otherwise, if the string contains the phrase "<name> is born in <year>. How old is <name>?", I recover the year (placed immediately after it), calculate the difference with the current year, convert it and insert it as input to the 'alienquiz' program
            now = datetime.datetime.now()
            process.stdin.write((str(now.year - int(reg4.search(input_str).group(1)))+'\n').encode())
        elif reg5.search(input_str):
            #Otherwise, this means that the program is finished correctly
            break
        else:
            #Finally, if none of the previous regex matches, it means that no extrapolation and processing is required, so I return '\n' as input to the 'alienquiz' program
            process.stdin.write(('\n').encode())
        process.stdin.flush() # flushes the write to the program