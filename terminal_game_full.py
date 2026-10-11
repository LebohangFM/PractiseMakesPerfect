print ('                                                                                            SPACE ADVENTURES!!!                                                                       ')

print('Welcome to Space Adventures! We are about to venture into the Andromada Galaxy. Are you ready to tour it with me?')

print('1 - Yes. Ive got my astronaut boots on🥾!')
print('2 - No. sorry. Im not yet ready😔')

ans1=int(input('Answer here: '))
if ans1==1:
    print('lets go!')
    
else:
    print('Oh no! Sorry to see you go. Hope you join me next time!')
break

print('It seems the rocket ship needs a bit of maintenance before we leave, We need to complete the next task in a timely manner or the window to leave Earth will pass!')
print('')
print('')
print('')
print('Instructions: The computer box needs to be recalibrated. There are 3 nodes below (Node A, Node B and Node C) random numbers will be generated,') 
print('and you have to make calculations to ensure all nodes have a result of 5')
print('')
print('For Example: ')
print('')
print('if the random numbers for Nodes A, B and C are 4, 10 and 22, you need to enter a number that when multiplied by the random number, it gives you 5')
print('')
print('So,')
print('Node A: 4 x 1.25 = 5')
print('')
print('Node A: 10 x 0.5 = 5')
print('')
print('Node A: 22 x 0.23 = 5')
print('')
print('')
print('There can only be a decimal place of upto 0.5 below and above 5. Lets go!!!')




print('')
print('')




import random




a=0
b=0
c=0




tries=0




NodeA=random.randint(1,100)
NodeB=random.randint(1,100)
NodeC=random.randint(1,100)




print(NodeA)
print(NodeB)
print(NodeC)








num1=float(input('What number will calibrate Node A?: '))
print('')
num2=float(input('What number will calibrate Node B?: '))
print('')
num3=float(input('What number will calibrate Node C?: '))




a=NodeA*num1




b=NodeB*num2




c=NodeC*num3




print (NodeA*num1)
print(NodeB*num2)
print(NodeC*num3)








while a != 5 and b!=5 and c!=5 and tries<3:
        print ('Uncalibrated. Please try again')
        tries=tries+1
        NodeA=random.randint(1,100)
        NodeB=random.randint(1,100)
        NodeC=random.randint(1,100)
        
        print(NodeA)
        print(NodeB)
        print(NodeC)
        
        num1=float(input('What number will calibrate Node A?: '))
        num2=float(input('What number will calibrate Node B?: '))
        num3=float(input('What number will calibrate Node C?: '))
        
        a=0
        b=0
        c=0
        
        a=NodeA*num1




        b=NodeB*num2




        c=NodeC*num3




        print(NodeA*num1)
        print(NodeB*num2)
        print(NodeC*num3)
        
if a != 5 and b!=5 and c!=5:
    print('The rocket ship couldnt be recalibrated, try again next year!')
    print('')
    print('Do you wish to start again?:')
    print('1 - Yes')
    print('2 - No')
    ans2=int(input('Answer here: '))
    
    if ans2==1:
        print('Welcome back!')
        
    else:
        print('I hope to journey with you one day. Good luck!')
    
else:
    print('Rocket ship calibrated! T-minus: ')
    print('10')
    print('9')
    print('8')
    print('7')
    print('6')
    print('5')
    print('4')
    print('3')
    print('2')
    print('1')
    print('0')
    print('LIFT OFFFFFF!!!!!')

print ('                                                    Rocky Pasteurs                                          ')
print('')
print('')
print('What an amazing journey this has been!')
print('')
print('Oh no! What do we have here? Looks like we have run into an astroid belt.')
print('But wait, it looks like there is a clear path right above')
print('We are going to need to pass at least 4 asteroids to reach the clear!')
print('to do that we will need to fire at them with the laser beams')
print('')
print('')
print('Instructions: To fire at each astroid we need to give the correct answers to each question below:')
print('')
print('')




print('Q2: How many hearts does an octopus have?')
print('1 - 1')
print('2 - 2')
print('3 - 3')
print('')
print('Q3: Bananas are technically classified as what type of fruit?')
print('1 - Berries')
print('2 - Pomes')
print('3 - Drupes')
print('')
print('Q4: According to astronauts, what does outer space smell like?')
print('1 - Seared steak')
print('2 - Hot metal')
print('3 - Welding fumes')
print('4 - All of the above')




print('')
print('If you get each answer correct, the laser beam will disintegrate the asteroids')
print('The ship can handle crashing into only one astroid, so make sure to get at least 3 right!')
print('')
print('Good Luck!')








an1=0
an2=0
an3=0
an4=0
total=0




print('                                 Question 1                                              ')




print('Q1: What kind of environment does Shrek live in?')
print('1 - Swamp')
print('2 - Valley')
print('3 - Tropical Forest')
print('')




ans3=int(input('Answer to question 1: '))




if ans3==1:
    an1=+1
    print('Correct!')
else:
    an1=0
    print('Incorrect')
    








print('                                 Question 2                                              ')




ans4=int(input('Answer to question 2: '))




if ans4==3:
    an2=+1
    print('Correct!')




else:
    an2=0
    print('Incorrect')












print('                                 Question 3                                             ')




ans5=int(input('Answer to question 3: '))




if ans5==1:
    an3=+1
    print('Correct!')
else:
    an3=0
    print('Incorrect')








print('                                 Question 4                                              ')
ans6=int(input('Answer to question 4: '))




if ans6==4:
    an4=+1
    print('Correct!')
    
else:
    an4=0
    print('Incorrect')




total=an1+an2+an3+an4








if total>=3:
    print('Congratulations! You did so well! We have finally reached he andromeda Galaxy!')




else:
    total<3
    print('Astroids destroyed the ship, we have to escape through the emergency pods!')
    print('Better luck next time!')
break 
