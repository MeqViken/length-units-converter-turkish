import types

mmcm=0
cmmetre=0
metrekm=0
mmcmtoplam=0

Greeting = '''
   _____ ____  _   ___      ________ _____ _______ ______ _____  
  / ____/ __ \| \ | \ \    / /  ____|  __ \__   __|  ____|  __ \ 
 | |   | |  | |  \| |\ \  / /| |__  | |__) | | |  | |__  | |__) |
 | |   | |  | | . ` | \ \/ / |  __| |  _  /  | |  |  __| |  _  / 
 | |___| |__| | |\  |  \  /  | |____| | \ \  | |  | |____| | \ \ 
  \_____\____/|_| \_|   \/   |______|_|  \_\ |_|  |______|_|  \_\ 
  
  '''
print(Greeting)

print("Lütfen üçünden birini seçiniz= ","mmcm,","cmmetre,","metrekm")
uzunlukbirim=input()

if "mmcm" in uzunlukbirim:
    mmcm=int(input("Lütfen milimetreden santimetreye çevirmek istediğiniz uzunluğu belirtin. = "))
    mmcmtoplam = mmcm / 10
    
if mmcmtoplam > 0:
    print(mmcmtoplam,"cm")


if "cmmetre" in uzunlukbirim:
    cmmetre=int(input("Lütfen santimetreden metreye çevirmek istediğiniz uzunluğu belirtin. = "))
    cmmetre = cmmetre / 100
    
if cmmetre > 0:
    print(cmmetre,"m")

if "metrekm" in uzunlukbirim:
    metrekm=int(input("Lütfen metreden kilometreye çevirmek istediğiniz uzunluğu belirtin. = "))
    metrekm = metrekm / 1000
    
if metrekm > 0:
    print(metrekm,"km")




    