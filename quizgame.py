
print('welcome to quiz game')

player=input('do you want to play? ')

if player.lower() !="yes":
    quit()

print ('ok lets play') 
score=0

question=input ("How many days do we have in a week? ")
if question.lower()=="seven":
    print('correct')
    score +=1
else:
    print('incorrect') 

question=input ("In which direction does the sun rise? ")
if question.lower()=="east":
    print('correct')
    score +=1
else:
    print('incorrect')  

question=input ("what is our national bird? ")
if question.lower()=="peacock":
    print('correct')
    score +=1
else:
    print('incorrect')     

question=input ("which is the fastest animal on the land? ")
if question.lower()=="cheetah":
    print('correct')
    score +=1
else:
    print('incorrect')             

question=input ("what is the largest ocean in the world? ")
if question.lower()=="pacific ocean":
    print('correct')
    score +=1
else:
    print('incorrect')   
print("your score "+ str(score))            