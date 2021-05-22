''' Purpose: compare results of random game outcomes between two players with answers provided 
in same order vs different order for each player, and at different range of event numbers. 

Hypothesis: With less events, results will be more diverse when one list of outcomes is scrambled.
When number of events gets the spread will even out between the two experiments. 

https://github.com/SmashAF/rock_paper_scissors_study.git

'''
import random

# future update to allow input of name when used as game

Scott = ['Lizard', 'Paper', 'Rock', 'Scissors', 'Spock']
Gina = ['Spock', 'Rock', 'Paper', 'Scissors', 'Lizard']
Sofia = ['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
Jack =['Rock', 'Paper', 'Scissors', 'Lizard', 'Spock']
num_turns = 5

# function for player1   
def p1_turn(num_turns):
    result_p1 = []
   
    for i in range(num_turns):
        roll = random.choice(Scott)
        result_p1.append(roll)
    return result_p1


def result_p1(p1_turn):
    d1 = { }
    p1data = p1_turn(num_turns)
    
    for idx, result in enumerate(p1data):
        d1[idx+1] = result      
    return d1
          
d1 = result_p1(p1_turn)
 
for idx in range(1):
    print(f'Player 1 {d1}')

# function for player2

def p2_turn(num_turns):
    result_p2 = []
    for i in range(num_turns):
        roll = random.choice(Gina)
        result_p2.append(roll)
    return result_p2
          
def result_p2(p2_turn):
    d2 = { }
    p2data = p2_turn(num_turns)
    
    for idx, result in enumerate(p2data):
        d2[idx + 1] = result 
    return d2
          
d2 = result_p2(p2_turn)
  
for idx in range(1):
    print(f'Player 2 {d2}')

    
    
# function for player3

def p3_turn(num_turns):
    result_p3 = []
   
    for i in range(num_turns):
        roll = random.choice(Sofia)
        result_p3.append(roll)
    return result_p3

def result_p3(p3_turn):
    d3 = { }
    p3data = p3_turn(num_turns)
    
    for idx, result in enumerate(p3data):
        d3[idx + 1] = result 
    return d3
          
d3 = result_p1(p3_turn)

for idx in range(1):
    print(f'Player 3 {d3}')  


# function for player4

def p4_turn(num_turns):
    result_p4 = []
    for i in range(num_turns):
        roll = random.choice(Jack)
        result_p4.append(roll)
    return result_p4
          
def result_p4(p4_turn):
    d4 = { }
    p4data = p4_turn(num_turns)
    
    for idx, result in enumerate(p4data):
        d4[idx + 1] = result
        
    return d4
          
d4 = result_p4(p4_turn)

for idx in range(1):
    print(f'Player 4 {d4}')  
    
# Comparisons

'''
ds = [d1,d2]
d={}
for k in d1.keys():
    d[k] = tuple(d[k] for d in ds)
'''
comp_1_and_2 = d1.copy()
comp_2_and_3 = d2.copy() 
comp_3_and_4 = d3.copy()
comp_1_and_4 = d1.copy()

for k, v in  d2.items():
        comp_1_and_2 [k] += ' ' + v
        
for k, v in  d3.items():
        comp_2_and_3 [k] += ' ' + v

for k, v in  d4.items():
        comp_3_and_4 [k] += ' ' + v
        
for k, v in  d4.items():
        comp_1_and_4 [k] += ' ' + v        
        
       

print (f'mix vs slide {comp_1_and_2}')    
print (f'order vs slide {comp_2_and_3}')    
print (f'both order {comp_3_and_4}')    
print (f'order vs mix {comp_1_and_4}')    









# future edits to compare turns and display winner
"""Scissors cuts paper, paper covers rock, rock crushes lizard, lizard poisons Spock, 
Spock smashes scissors, scissors decapitates lizard, lizard eats paper, paper disproves Spock,
Spock vaporizes rock, and as it always has, rock crushes scissors."""


# def argument_solver(turns = 5):
   
#     result_p1 = []
#     result_p2 = []
    
#     for i in  range(turns):
#         result_p1.append(random.choice(Scott))
#         result_p2.append(random.choice(Gina))
#     return result_p1 , result_p2
        
# # print (argument_solver())


# def compare_results( ):
#     d= {} 
#     argue_results = argument_solver() 
    
#     for idx, result in enumerate(argue_results):
#         d[idx] = result
#     return d
# # print (compare_results())

