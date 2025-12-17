from mymodule import *

k=["mari","Juku","kati"]
s=["1234","4321", "abcdf1"]

while True:
    print("\n=== Põhiprogrammi menüü ===")
    print("1 - Registreerimine")
    print("2 - Autoriseerimine (Sisselogimine)")
    print("3 - Nime või parooli muutmine")
    print("4 - Unustatud parooli taastamine")
    print("5 - Lõpetamine")
    
    valik = input("Vali number (1-5): ")
    
    if valik == "1":
        registreerimine(k, s)
    elif valik == "2":
        autoriseerimine(k, s)
    elif valik == "3":
        muuda(k, s)
    elif valik == "4":
        parooli_taastamine(k, s)
    elif valik == "5":
        print("Programm lõpetab töö. Nägemist!")
        break
    else:
        print("Vale valik! Proovi uuesti.")