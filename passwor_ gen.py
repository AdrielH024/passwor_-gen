import random

normalchar= "abcdefghijklmnopqrstuvwxyz"
upperchar= "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
espec= "@!#$%+"

i = int(input("number of characteres in new password?\n"))
j=0

newpass = []

while(j <= i):
 typechar = random.randint(1,4)
 if(typechar == 1):
     charn = random.randint(0,25)
     newpass.append(normalchar[charn])
 if(typechar == 2):
     charn = random.randint(0,25)
     newpass.append(upperchar[charn])
 if(typechar == 3):
     charn = random.randint(0,9)
     newpass.append(numbers[charn])
 if(typechar == 4):
     charn = random.randint(0,5)
     newpass.append(espec[charn])
 j = j+1
 
newpass = ''.join(newpass)
print (newpass)
