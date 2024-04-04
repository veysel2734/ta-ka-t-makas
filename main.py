import random
import time


sen_puan=0
pc_puan=0

while True:

    sen=input("Hangi seçenek taş / kağıt / makas")
    
    
    if sen=="taş" or sen=="kağıt" or sen=="makas":
        pc=random.randint(1,3)
        if pc == 1:
            pc="taş"
    
        elif pc == 2:
            pc="kağıt"
    
        else:
            pc="makas"
        
        print('Taş, Kağıt, Makas')
        time.sleep(1)
        print('1')
        time.sleep(1)
        print('2')
        time.sleep(1)
        print('3')
        time.sleep(1)    
    
      
        print("Bilgisayar seçimi:",pc)
    
        if pc == sen:
            print("Beraberlik")
    
    
        elif sen=="taş" and pc=="makas":
            sen_puan += 1
            print("Sen kazandın,senin puanın:",sen_puan)
            
        
        elif sen=="kağıt" and pc=="taş":
            sen_puan += 1
            print("Sen kazandın,senin puanın:",sen_puan)

        elif sen=="makas" and pc=="kağıt":
            sen_puan += 1
            print("Sen kazandın,senin puanın:",sen_puan)
            
    
        else:
            print("kaybettin")
            pc_puan+=1

        
    
    
    else:
        print("böyle bir seçenek yok")
    
        
    print("bilgisayar puanı:",pc_puan)
    print("senin puanın:",sen_puan)   
    
    