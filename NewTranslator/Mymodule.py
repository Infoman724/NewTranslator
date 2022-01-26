#import os
#from gtts import gTTS
import random
ruswords=[]
engwords=[]




def faile_reader(f:str,l:list):
    """ Info failist f listisse l
    """
    fail=open(f,"r",encoding="utf-8-sig")
    for rida in fail:
        l.append(rida.strip())
    fail.close()
    return l


def rida_salvestamine(f:str,rida:str):
    """Üks sõna või lause(rida) salvestame
    failisse
    :param str f:файл в который нужно дозаписать
    :param str rida:строка которая будет дозаписана в конец файла
    """
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(rida+'\n',)
    fail.close()

def faile_saver(f:str,l:list):
    """
    Loetelu salvastamine failise
    :param str f:файл в который нужно перезаписать
    :param list l:список который сохраняется в файл
    """
    fail=open(f,"w",encoding="utf-8-sig")
    for el in l:
        fail.write(el+'\n')
    fail.close




def uus_sõna(f:str,rida:str)->list:
    
    """Lisame uus sõna failisse ja listisse 
    :param str file:faili nimetus
    :param str x:lisatav sõna
    """
    l=[]
    with open(f,'a',encoding="utf-8-sig") as fail:
        fail.write(rida+"\n")



def correction(sona:str,l:list): 
    
	for i in range(len(l)):
		if l[i]==sona:
			uus_sona=sona.replace(sona,input("Новое слово--> "))
			l.insert(i,uus_sona)
			l.remove(sona)

	return l



def heli(text:str,keel:str):
    """функция проговоаривает слово которое вводите
    """
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")

def test(l1:list,l2:list):
    """
    функция запрашивает два списка и из них проверяет ваши знания и в конце выдает процентуальное соотношение правильных ответов
    :param list l1:первый список(в моём случае "RUS_WORDS.txt")
    :param list l2:второй список (в моём случае "ENG_WORDS.txt")
    """
    result=0
    lists=[]
    lists.extend(l1)
    lists.extend(l2)
    random.shuffle(lists)
    for z in range(len(l1)):
        otvet=input(f"Переведи данное слово - '{lists[i]}': ")
        if otvet in l1 or otvet in l2:
            if lists[z] in l1:
               if l1.index(lists[z])==l2.index(otvet):
                    result+=1
                    print('правильно!')
                    print()
            elif lists[z] in l2:
                if l2.index(lists[z])==l1.index(otvet):
                    result+=1
                    print('правильно!')
                    print()
        else:
            print('Неправильно!')
            print()
    resultPer=(result/len(l1))*100
    print(f"Ваш результат: {resultPer}%")