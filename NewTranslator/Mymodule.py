#import os
#from gtts import gTTS
from random import *
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
    """
    fail=open(f,'a',encoding="utf-8-sig")
    fail.write(rida+'\n',)
    fail.close()

def faile_saver(f:str,l:list):
    """Loetelu salvastamine failise
    """
    fail=open(f,"w",encoding="utf-8-sig")
    for el in l:
        fail.write(el+'/n')
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
    obj=gTTS(text=text,lang=keel,slow=False).save("heli.mp3")
    os.system("heli.mp3")


def testing():  
    print("Сейчас начнут появлятся слова на обоих языках постарайтесь перевести правильно все слова!")
    test=print(random.index.ruswords)
