#!/usr/bin/env python

import random

print('Добрый день!')
number_player=raw_input("Введите число игроков \n ")

#def vvod():
#for count in mumber_player:
name1=raw_input("Введите имя игрока 1 \n ")
#age1=raw_input("Введите возраст игрока 1 \n ")

mny1=int(raw_input("Введите общую сумму игрока 1 \n "))

name2=raw_input("Введите имя игрока 2 \n ")

#age2=raw_input("Введите возраст игрока 2 \n ")

mny2=int(raw_input("Введите общую сумму игрока 2 \n "))

many1=int(str(mny1))
many2=int(str(mny2))

        
class player(object):
    def __init__(self,name,many):
            self.name=name
            #self.age=age
            self.many=many
            #self.stavka=stavka
            
    def vug_prog(self,many,stavka):
        if stavka>0:
            return stavka
        else:
            return many
        
    def prog():
        if player.many==0:
            print('Извините '+player.name+ 'но вы проиграли все. Вы покидаете игру')

    def numb(self,name):
           return raw_input(name+" Введите число от 1 до 100 \n ")
           
            
            
class kazino:
        
    def __init__(self,name,many):
            self.namek=namek
            self.manyk=manyk
            #self.stavka=stavka
    
    def num_player():
        return count

    def wins():
        if player.stavka>many:
            print('Wins player '+player.name)

player1=player(name1,many1)

player2=player(name2,many2)

print(player1.name)

        
while player1.many!=0 and player2.many!=0:
                
                print('Hello dear players '+name1+' and '+name2+'\n Начинаем игру')
                print(player1.many,player2.many)
               
                stav=raw_input(name1+" Введите вашу ставку \n ")
                stav1=raw_input(name2+" Введите вашу ставку \n ")

                stavka=int(str(stav))
                stavka1=int(str(stav1))
                
                #many1=many1-player1.vug_prog(many1,stavka)
                #many2=many2-player2.vug_prog(many2,stavka1)
                
                print(player2.vug_prog(many2,stavka1))
                c=random.randint(1, 100)
                
                vb=player1.numb(name1)
                vb1=player2.numb(name2)
                
                number=int(str(vb))
                number1=int(str(vb1))
                
                print(number,number1,c)

                if abs(c-number1)>abs(c-number):
                        print (player1.name+' win ')
                        player2.many=player2.many-player2.vug_prog(many2,stavka1)
        
                        print(player2.many,many1,player2.vug_prog(many2,stavka1))
                        
                else:
                        print (player2.name+' win')
                        player1.many=player1.many-player1.vug_prog(many1,stavka)
                        print(player1.many,many2,player1.vug_prog(many1,stavka))


print('Игра окончена')


        



