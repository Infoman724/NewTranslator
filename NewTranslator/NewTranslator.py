from Mymodule import *
ruswords=[]
engwords=[]
ruswords=faile_reader("RUS_WORDS.txt",ruswords)
engwords=faile_reader("ENG_WORDS.txt",engwords)

while True:
       
        print("Здравствуйте! это Русско<-->английский переводчик")
        print()
        print()
        print("T-Перевод слов из нашей системы,U-добавить слово/а в словарь,E-исправить ошубку в словаре,C-Проверить своий познания,S-Посмотреть все слова в списке,R-Проговорить слово,STOP-закончить программу")
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


        elif vast=="E":#замена слов/а с ошибкой 
            er=int(input("Какое слово вы хотите заменить? (1-рус) (2-eng)-->"))
            if er==1:
                sõna=input("Слово которое надо исправить--> ")
                correction(sõna,ruswords)
                #на этом месте я должен был использовать функцию rida_salvestamine но я не смог найти способ обратится к переменной внутри функции который бы подходит под мой случай и перестроить функцию замены тоже не получилась так как она слишком чувствительна.
                #эта функция работает и заменяет слова из списка но они не сохраняются в файле
                print(ruswords)

            elif er==2:
                sõna=input("Слово которое надо исправить--> ")
                correction(sõna,engwords)
                #таже тема и здесь
                print(engwords)


        elif vast=="C":
            Test(ruswords,engwords,"computer")
        #elif vast=="R":
            #keel=input("На каком языке говорим? ") #ru et en
            #sõna=input("Слово---> ")
            #heli(sõna,keel)
        #else:
             #break
