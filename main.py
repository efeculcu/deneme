import random 
x = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

password_len = int(input("Parolanın uzunluğunu girin: "))
password_adeti = int(input("Kaç adet şifre oluşturulsun: "))
for y in range (0, password_len):
 password = ""
for y in range (0,password_adeti):
    print (password)
for password in range(0, password_len):
   sifre2= random.choice(x)
   sifre = sifre + sifre2
print ("random sifreniz" + password)




