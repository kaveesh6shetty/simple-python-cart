# -*- coding: utf-8 -*-
"""
Created on Wed Jul 11 15:26:27 2018

@author: harshith s
"""
vege={'carrot':20,'ladysfinger':60,'beetroot':30}
fruits={'apple':30,'mango':40,'peach':80}
processed={'bingo':30,'cake':30}
def vege_func(item,number):
        if(item in vege.keys()):
            f=vege[item]
            return f*number 
        else:print("item not available")

def fruits_func(item,number):
    for i in fruits:
        if(item in fruits.keys()):
            f=fruits[item]
            return f*number        
        else:print("item not available")

def processed_func(item,number):
    for i in processed:
        if(item in processed.keys()):
          f=processed[item]
          return f*number
        else:print("item not available")

print("enter the item name")
print("'vege' or 'fruits' or 'processed'")
item = input()
file=open('write.txt','a')
if(item=='vege'):
          print(vege)
          s=input("enter the item\n")
          
          print("enter the number of items required\n")
          req = input()
          file.writelines([s])
          file.writelines(['   ' '   ',req])
          x=str(vege_func(s,int(req)))
          file.writelines(['   ' '   ''    ',x])
          file.write("\n")
          file.close()
          print("total",x)
elif(item=='fruits'):
         print(fruits)
         s=input("enter the item\n")
         print("enter the number of items required\n")
         req = input()
         file.writelines([s])
         file.writelines(['   ' '   ',req])
         x=str(fruits_func(s,int(req)))
         file.writelines(['   ' '   ''    ',x])
         file.write("\n")
         file.close()
         print("total",x)
else:
         print(processed)
         s=input("enter the item\n")
         print("enter the number of items required\n")
         req = input()
         file.writelines([s])
         file.writelines(['   ' '   ',req])
         x=str(processed_func(s,int(req)))
         file.writelines(['   ' '   ''    ',x])
         file.write("\n")
         file.close()

         print("total",x)


    
    