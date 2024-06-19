#EX-8 : SNAKE WATER GUN

#PROBLEM : MAKE SANKE WATER GUN GAME,10 POINTS PLAYER WILL BE WIN

#SOLUTION :
import random as rd

scr_comp=0
scr_player=0

while True :
    if scr_player==5:
        print("game over!!\nPLAYER won\nfinal score:\ncomputer score : ", scr_comp,'\n','player score :',scr_player)
        exit()
    elif scr_comp==5:
        print("game over!!\nPLAYER won\nfinal score:\ncomputer score : ", scr_comp,'\n','player score :',scr_player)
        exit()
    opt=['s','w','g']
    comp_opt=rd.choice(opt)
    player_opt=input("take a guess\npress s for snake\npress w for water\npress g for gun\n")
    print("computer opted : ",comp_opt,'\n')
    if player_opt=='s' and comp_opt=='g':
        scr_comp=scr_comp+1
        print("computer won the round\n","computer score : ", scr_comp,'\n','player score :',scr_player)
    elif player_opt=='s' and comp_opt=='w':
        scr_player=scr_player+1
        print("computer score : \n", scr_comp,'\n','player score :',scr_player)
    elif player_opt==comp_opt:
        scr_comp==scr_comp 
        print("round tie\n","computer score : ", scr_comp,'\n','player score :',scr_player)
    elif player_opt=='w' and comp_opt=='s':
        scr_comp=scr_comp+1
        print("computer won the round\n","computer score : ", scr_comp,'\n','player score :',scr_player)
    elif player_opt=='w' and comp_opt=='g':
        scr_player=scr_player+1
        print("player won the round\n","computer score : ", scr_comp,'\n','player score :',scr_player)
    elif player_opt=='g' and comp_opt=='s':
        scr_player=scr_player+1
        print("player won the round\n","computer score : ", scr_comp,'\n','player score :',scr_player)
    else :
        scr_comp=scr_comp+1
        print("computer won the round\n","computer score : ", scr_comp,'\n','player score :',scr_player)

#OUTPUT :
"""
take a guess     
press s for snake
press w for water
press g for gun  
w
computer opted :  w  

round tie
 computer score :  0 
 player score : 0    
take a guess
press s for snake    
press w for water    
press g for gun      
g
computer opted :  s  

player won the round 
 computer score :  0 
 player score : 1    
take a guess
press s for snake    
press w for water    
press g for gun      
w
computer opted :  w 

round tie
 computer score :  0
 player score : 1
take a guess
press s for snake
press w for water
press g for gun
s
computer opted :  g 

computer won the round
 computer score :  1
 player score : 1
take a guess
press s for snake
press w for water
press g for gun
s
computer opted :  s 

round tie
 computer score :  1
 player score : 1

.    .    .
.    .    .

take a guess
press s for snake
press w for water
press g for gun
s
computer opted :  w 

computer score :
 3
 player score : 4
take a guess
press s for snake
press w for water
press g for gun
s
computer opted :  s 

round tie
 computer score :  3
 player score : 4
take a guess
press s for snake
press w for water
press g for gun
w
computer opted :  g 

player won the round
 computer score :  3
 player score : 5
game over!!
PLAYER won
final score:
computer score :  3
 player score : 5"""

 #                                                  END 
 