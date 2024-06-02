# import system library
import sys
import json

# take passed variable values 
c_code = sys.argv[1]

import nltk
nltk.download('punkt')  # Uncomment if punkt is not downloaded
from nltk.tokenize import word_tokenize

# Initialize CondCounter
CondCounter = 0

# Read C code from file 
#with open('variables.c', 'r') as file:
#    c_code = file.read()

# Tokenize the C code
tokens = word_tokenize(c_code)
final_tokens = []

# Merge consecutive tokens if they form an operator
i = 0
while i < len(tokens):
    if i < len(tokens) - 1 and tokens[i] + tokens[i + 1] in [">=", "<=", "!=", "==", "&&", "||"]:
        final_tokens.append(tokens[i] + tokens[i + 1])
        i += 2
    else:
        final_tokens.append(tokens[i])
        i += 1

n = len(final_tokens)
maxval = 2**31 - 1
minval = -2**31    

# Define C operators
c_operators = ['>', '<', '==', '=', '+', '-', '*', '/', '%', '++', '--', '+=', '-=', '*=', '/=', '%=', '!=', '<=', '>=', '!', '&&', '||', '&', '|', 
               '^', '~', '<<', '>>', '&=', '|=', '^=', '<<=', '>>=', ',', '.', '->', '[', ']', '{', '}', ';', ':', '?']

# Function to evaluate parentheses counting
def eval_cond(x):
    global CondCounter
    if x == '(':
        CondCounter += 1
    elif x == ')':
        CondCounter -= 1
    elif CondCounter == 0:
        return True
    return False

# Extract conditional statements
Condition = []   
for i in range(len(final_tokens)):
    if final_tokens[i] == 'if':
        for j in range(i + 1, len(final_tokens)):
            if eval_cond(final_tokens[j]) == False:
                Condition.append(final_tokens[j])
            else:
                break

# Possible Test Cases in conditional statements
possible_test_cases = []
for i in range(len(Condition) - 1):
    if Condition[i] in c_operators:
        # Assuming the condition immediately followed by an operator and a value
        operator = Condition[i]
        if i < len(Condition):
            value = Condition[i + 1]
            if operator == '>':
                possible_test_cases.append([value, maxval])
                possible_test_cases.append([minval, value])
            elif operator == '<':
                possible_test_cases.append([value, minval])
                possible_test_cases.append([maxval, value])
            else:
                possible_test_cases.append([minval, value])
                possible_test_cases.append([value, maxval])

# print('Conditional Statements')
# Print Results
#print('Conditional Statements Identified: \n')
#for condition in Condition:
#    print(f"{condition}", end=' ')
#print('')


print('>>> Internal Test cases Identified in Conditional Statements:\n\t')
if not Condition:
    print('No Conditional Statements detected')
for i in range(0,len(Condition)):
    if Condition[i] in ['&&','||']:
        print(')',' ( ', end="")
    else:
        print(Condition[i]," ", end="")
print('\n')   
print('>>> Possible Test cases Identified in Conditional Statements: \n\t')
if not Condition:
    print('No Conditional Statements detected')

print("( ",end="")
for i in range(1,len(Condition)-1):
    if Condition[i] in ['&&','||']:
        print(')','( ', end="")
    elif Condition[i] == '>':
        print(c_operators[1]," ", end="")
    elif Condition[i] == '<':
        print(c_operators[0]," ", end="")
    elif Condition[i] == '<=':
        print(c_operators[18]," ", end="")
    elif Condition[i] == '>=':
        print(c_operators[17]," ", end="")
    elif Condition[i] == '==':
        print(c_operators[0]," ", end="")
    elif Condition[i] == '!=':
        print(c_operators[0]," ", end="")
    else:
        print(Condition[i]," ", end="")
print(")",end="")
print('')
print("( ",end="")
for i in range(1,len(Condition)-1):
    if Condition[i] in ['&&','||']:
        print(')','( ', end="")
    elif Condition[i] == '>':
        print(c_operators[2]," ", end="")
    elif Condition[i] == '<':
        print(c_operators[2]," ", end="")
    elif Condition[i] == '==':
        print(c_operators[1]," ", end="")
    elif Condition[i] == '<=':
        print(c_operators[2]," ", end="")
    elif Condition[i] == '>=':
        print(c_operators[2]," ", end="")
    elif Condition[i] == '!=':
        print(c_operators[1]," ", end="")
    else:
        print(Condition[i]," ", end="")
print(")")
print()

# Extract Loops
Loops = []
bracket = ['}']
i = 0

def nested_do_while(start,end) :
    i=start
    while(i<end):
        if final_tokens[i] in ['for', 'while']:
            loop_start_index = i
            loop_end_index = final_tokens.index('{', i)
            Loops.append(final_tokens[loop_start_index:loop_end_index + 1] + bracket)
            i = loop_end_index 
        i+=1
        
        
while i < len(final_tokens):
    if final_tokens[i] in ['for', 'while']:
        loop_start_index = i
        loop_end_index = final_tokens.index('{', i)
        Loops.append(final_tokens[loop_start_index:loop_end_index + 1] + bracket)
        i = loop_end_index 
    elif final_tokens[i] == 'do':
        loop_start_index = i
        Loops.append(final_tokens[loop_start_index:loop_start_index + 2])
        depth=1
        i=i+2
        while(depth!=0):
            if final_tokens[i]=='}':
                depth-=1
            if final_tokens[i]=='{':
                depth+=1
            i+=1
        loop_end_index = final_tokens.index(';', i-1)
        #print("at pos : ",loop_start_index,loop_end_index)
        
        #while_index = final_tokens.index('while', loop_end_index)  # Find the 'while' keyword
        nested_do_while(loop_start_index+2,i-1) #nested part
        loop_condition = final_tokens[i-1 : loop_end_index+ 1]  # Extract loop condition
        Loops.append(loop_condition)
               
    i += 1

#print('Loops :- \n' )
# Print loop statements
#print('Loop Statements Identified : ')
#for loop in Loops:
#    print(' '.join(loop))
#print('')

# Possible Range of Test Cases in Loops
possible_test_cases_in_loops = []
for element in Loops:
    for i in range(len(element)):
        if element[i] in ['for', 'while']:
            if element[i + 2] == 'int':
                operators_in_loops = element[i + 4]
            else:
                operators_in_loops = element[i + 3]
            if i < len(element):
                if element[i + 2] == 'int':
                    values = element[i + 5]
                else:
                    values = element[i + 4]
                if operators_in_loops in ['>', '<', '!=', '<=', '>=', '==']:
                    possible_test_cases_in_loops.append([minval, values])
                    possible_test_cases_in_loops.append([values, maxval])
                    j = i + 1
                    while j < len(element):
                        if element[j] in ['&&', '||']:
                            if element[j + 1] == 'int':
                                values2 = element[j + 4]
                            else:
                                values2 = element[j + 3]
                            possible_test_cases_in_loops.append([minval, values2])
                            possible_test_cases_in_loops.append([values2, maxval])
                        j += 1
                elif operators_in_loops == '=':
                    possible_test_cases_in_loops.append([minval, values])
                    if element[i + 2] == 'int':
                        values1 = element[i + 9]
                    else:
                        values1 = element[i + 8]
                    possible_test_cases_in_loops.append([values, values1])
                    possible_test_cases_in_loops.append([values1, maxval])
                else:
                    # Append some default test cases if operator is not a comparison operator
                    possible_test_cases_in_loops.append([minval, values])
                    possible_test_cases_in_loops.append([values, maxval])

#print('Possible Range of Test Cases Identified in Loops:')
#print(possible_test_cases_in_loops)

print('\n>>> Internal Test cases Identified in Loops:\n\t')
if not Loops:
    print('No Loops detected')

for loop in Loops:
    for i in range(len(loop)):
        if loop[i] == 'for':
            if loop[i+2] == 'int':
                print('(',' '.join(loop[i+3:i+6]),')',end=" ")
                print('(',' '.join(loop[i+5]),' - ',''.join(loop[i+9]),')',end=" ")
            else:
                print('(',' '.join(loop[i+2:i+5]),')',end=" ")
                print('(',' '.join(loop[i+4]),' - ',''.join(loop[i+8]),')',end=" ")
        elif loop[i] == 'while':
            print('(',' '.join(loop[i+2:i+5]),')',end=" ")
            j=i+1
            while j < len(loop):
                if loop[j] in ['&&', '||']:
                   print('(',' '.join(loop[j+1:j+4]),')',end=" ")
                j+=1
    print('')
print('\n>>> Possible Test cases Identified in Loops: \n\t')
if not Loops:
    print('No Loops detected')
for loop in Loops:
    for i in range(len(loop)):
        if loop[i] == 'while':
            if loop[i+3] == '>':
                print('(',' '.join(loop[i+2]),c_operators[1],''.join(loop[i+4]),')',"", end="")
                print('(',' '.join(loop[i+2]),c_operators[3],''.join(loop[i+4]),')',"", end="")
            elif loop[i+3] == '<':
                print('(',' '.join(loop[i+2]),c_operators[0],''.join(loop[i+4]),')',"", end="")
                print('(',' '.join(loop[i+2]),c_operators[3],''.join(loop[i+4]),')',"", end="")
            elif loop[i+3] in ['==','!=']:
                print('(',' '.join(loop[i+2]),c_operators[0],''.join(loop[i+4]),')',"", end="")
                print('(',' '.join(loop[i+2]),c_operators[1],''.join(loop[i+4]),')',"", end="")
            elif loop[i+3] == '>=':
                print('(',' '.join(loop[i+2]),c_operators[17],''.join(loop[i+4]),')',"", end="")
                print('(',' '.join(loop[i+2]),c_operators[3],''.join(loop[i+4]),')',"", end="")
            elif loop[i+3] == '<=':
                print('(',' '.join(loop[i+2]),c_operators[18],''.join(loop[i+4]),')',"", end="")
                print('(',' '.join(loop[i+2]),c_operators[3],''.join(loop[i+4]),')',"", end="")
            else:
                print('(',' '.join(loop[i+2:i+5]),')',end="")
                print(loop[i+3]," ", end="")
            j=i+1
            while j < len(loop):
                if loop[j] in ['&&', '||']:
                    if loop[j+2] == '>':
                        print('(',' '.join(loop[j+1]),c_operators[1],''.join(loop[j+3]),')',"", end="")
                        print('(',' '.join(loop[j+1]),c_operators[3],''.join(loop[j+3]),')',"", end="")
                    elif loop[j+2] == '<':
                        print('(',' '.join(loop[j+1]),c_operators[0],''.join(loop[j+3]),')',"", end="")
                        print('(',' '.join(loop[j+1]),c_operators[3],''.join(loop[j+3]),')',"", end="")
                    elif loop[j+2] in ['==','!=']:
                        print('(',' '.join(loop[j+1]),c_operators[0],''.join(loop[j+3]),')',"", end="")
                        print('(',' '.join(loop[j+1]),c_operators[1],''.join(loop[j+3]),')',"", end="")
                    elif loop[j+2] == '>=':
                        print('(',' '.join(loop[j+1]),c_operators[17],''.join(loop[j+3]),')',"", end="")
                        print('(',' '.join(loop[j+1]),c_operators[3],''.join(loop[j+3]),')',"", end="")
                    elif loop[j+2] == '<=':
                        print('(',' '.join(loop[j+1]),c_operators[18],''.join(loop[j+3]),')',"", end="")
                        print('(',' '.join(loop[j+1]),c_operators[3],''.join(loop[j+3]),')',"", end="")
                    else:
                        print('(',' '.join(loop[j+1:j+5]),')',end="")
                        print(loop[j+1:j+5]," ", end="")
                j+=1
        elif loop[i] == 'for':
            if loop[i+2] == 'int':
                if loop[i+5] == '0':
                    print('(',' '.join(loop[i+3]),c_operators[1],''.join(loop[i+5]),')',"", end="")
                    print('(',' '.join(loop[i+3]),c_operators[0],''.join(loop[i+9]),')',"", end="")
                    if(loop[i+9].isdigit()):
                        mid = str(int(loop[i+9])//2)
                        print('(',' '.join(loop[i+3]),c_operators[3],''.join(mid),')',"", end="")
                    else:
                        print('(',' '.join(loop[i+3]),c_operators[3],''.join(loop[i+9]),'/2)',"", end="")
                else:
                    print('(',' '.join(loop[i+3]),c_operators[0],''.join(loop[i+5]),')',"", end="")
                    print('(',' '.join(loop[i+3]),c_operators[1],''.join(loop[i+9]),')',"", end="")
                    if(loop[i+5].isdigit()):
                        mid = str(int(loop[i+5])//2)
                        print('(',' '.join(loop[i+3]),c_operators[3],''.join(mid),')',"", end="")
                    else:
                        print('(',' '.join(loop[i+3]),c_operators[3],''.join(loop[i+5]),'/2)',"", end="")
                if loop[i+8] in ['>','>=','<','<=']:
                    print('(',' '.join(loop[i+3]),c_operators[3],''.join(loop[i+9]),')',"", end="")
                else:
                    print('(',' '.join(loop[i+7:i+10]),')',end="")
            else:
                if loop[i+4] == '0':
                    print('(',' '.join(loop[i+2]),c_operators[1],''.join(loop[i+4]),')',"", end="")
                    print('(',' '.join(loop[i+2]),c_operators[0],''.join(loop[i+8]),')',"", end="")
                    if(loop[i+8].isdigit()):
                        mid = str(int(loop[i+8])//2)
                        print('(',' '.join(loop[i+2]),c_operators[3],''.join(mid),')',"", end="")
                    else:
                        print('(',' '.join(loop[i+2]),c_operators[3],''.join(mid),')',"", end="") 
                else:
                    print('(',' '.join(loop[i+2]),c_operators[0],''.join(loop[i+4]),')',"", end="")
                    print('(',' '.join(loop[i+2]),c_operators[1],''.join(loop[i+8]),')',"", end="")
                    if(loop[i+4].isdigit()):
                        mid = str(int(loop[i+4])//2)
                        print('(',' '.join(loop[i+2]),c_operators[3],''.join(mid),')',"", end="")
                    else:
                        print('(',' '.join(loop[i+2]),c_operators[3],''.join(loop[i+4]),'/2)',"", end="")
                if loop[i+7] in ['>','>=','<','<=']:
                    print('(',' '.join(loop[i+2]),c_operators[3],''.join(loop[i+8]),')',"", end="")
                else:
                    print('(',' '.join(loop[i+6:i+9]),')',end="")
                     
           
    print('')

    

# call the function and pass variables to it
#print(code)
