#val min
# koki laika matysime po 1 min
valandos = int(input("iveskite valandas: "))
minutes = int(input("iveskite minutes: "))
minutes = minutes + 1
if minutes >=59 : 
    minutes = 0 
    valandos = valandos + 1
if valandos >= 24 :
    valandos = 00
    minutes = 00
if (valandos >= 25) or (minutes >= 61) :
    print("Neteisingai ivestas laikas")


print(valandos, minutes)

# pomin = minutes + 1
# valpomin = valandos + (pomin//60)
# pomin = pomin % 60 
# valpomin = valpomin % 24
# print(f"po minutes bus{valpomin} : {pomin}")

# viskasminpomin= valandos *60 + min + 1
# pomin = viskasminpomin % 60
# valpomin= (viskasminpomin // 60) % 24