cor_pin="123"

attem=3
for i in range (attem):
   pin=(input("enter a pin : "))  
   if pin == cor_pin:
        print("Access Granted")
        break
   else:
        print("WRONG PIN!")    
else:
    print("Account Locked")        
