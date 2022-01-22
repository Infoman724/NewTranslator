from MYmodule import *
ruswords=[]
engwords=[]
ruswords=faile_reader("RUS_WORDS.txt",ruswords)
engwords=faile_reader("ENG_WORDS.txt",engwords)

while True:
       
        print("Здравствуйте! это Русско<-->английский переводчик")
        print()
        print()
        print("T-Перевод слов из нашей системы,U-добавить слово/а в словарь,E-исправить ошубку в словаре,C-Проверить своий познания,S-Посмотреть все слова в списке,R-Проговорить слово")
        vast=str(input())
        if vast=="T":#переводчик
            while True:
                print("У нас есть перевод слов",ruswords)
                print()
                print("eng->rus(1),rus->eng(2),stop(3)")
                tvast=int(input())
                if tvast==1:
                    trans1=engwords.index(input("--> "))
                    print("-->",ruswords[trans1])
                if tvast==2:
                    trans1=ruswords.index(input("--> "))
                    print("-->",engwords[trans1])
                if tvast==3:
                    break

        elif vast=="U":#добавления нового/ых слов

            print("добавить в русский словарь и в английский")
            print()
            ruswords=uus_sõna("RUS_WORDS.txt",input("Напишите новое слово--> "))
            engwords=uus_sõna("ENG_WORDS.txt",input("Write new word--> "))
                
        elif vast=="S":#вывод всех слов которые есть в наличии
            print("Вот все слова которые есть у нас в наличии")
            print(ruswords)
            print(engwords)


        elif vast=="E":
            er=int(input("Какое слово вы хотите заменить? (1-рус) (2-eng)-->"))
            if er==1:
                sõna=input("Слово которое надо исправить--> ")
                correction(sõna,ruswords)
                rida_salvestamine("RUS_WORDS.txt",uus_sona)
                print(ruswords)

            elif er==2:
                sõna=input("Слово которое надо исправить--> ")
                correction(sõna,engwords)
                print(engwords)

        #elif vast=="R":
            #keel=input("На каком языке говорим? ") #ru et en
            #sõna=input("Слово---> ")
            #heli(sõna,keel)
        #else:
             #break
