# Selles programmis loome kasutajate haldamiseks süsteemi, mis võimaldab registreerimist, autoriseerimist,
# nime või parooli muutmist ning parooli taastamist. Kõik vajalikud funktsioonid on defineeritud MyModule.py.
# MyModule.py
import random
import string

def registreerimine(k:list, s:list) -> None:
    login = input("Sisesta uus kasutajanimi: ")
    if login in k:
        print("Kasutajanimi juba olemas! Proovi uuesti.")
        return
    
    print("Vali parooli loomise viis:")
    print("A - Automaatne genereerimine")
    print("B - Loo ise parool")
    valik = input("Vali A või B: ").upper()
    
    if valik == "A":
        str0 = ".,:;!_*-+()/#¤%&"
        str1 = '0123456789'
        str2 = 'qwertyuiopasdfghjklzxcvbnm'
        str3 = str2.upper()
        str4 = str0 + str1 + str2 + str3
        ls = list(str4)
        random.shuffle(ls)
        psword = ''.join([random.choice(ls) for x in range(12)])
        print("Sinu automaatselt genereeritud parool:", psword)
        k.append(login)
        s.append(psword)
        
    elif valik == "B":
        while True:
            psword = input("Sisesta parool: ")
            if (any(c.isdigit() for c in psword) and
                any(c.islower() for c in psword) and
                any(c.isupper() for c in psword) and
                any(c in ".,:;!_*-+()/#¤%&" for c in psword)):
                k.append(login)
                s.append(psword)
                print("Kasutaja registreeritud edukalt!")
                break
            else:
                if not any(c.isdigit() for c in psword):
                    print("Parool peab sisaldama vähemalt ühte numbrit!")
                if not any(c.islower() for c in psword):
                    print("Parool peab sisaldama vähemalt ühte väikest tähte!")
                if not any(c.isupper() for c in psword):
                    print("Parool peab sisaldama vähemalt ühte suurt tähte!")
                if not any(c in ".,:;!_*-+()/#¤%&" for c in psword):
                    print("Parool peab sisaldama vähemalt ühte erimärki!")
    else:
        print("Vale valik! Registreerimine katkestatud.")


def autoriseerimine(k:list, s:list) -> None:
    login = input("Sisesta kasutajanimi: ")
    psword = input("Sisesta parool: ")
    if login in k and s[k.index(login)] == psword:
        print(f"Tere, {login}! Sisselogimine õnnestus.")
    else:
        print("Vale kasutajanimi või parool!")


def muuda(k:list, s:list) -> None:
    login = input("Sisesta oma praegune kasutajanimi: ")
    if login not in k:
        print("Kasutajat ei leitud!")
        return
    
    index = k.index(login)
    print("Vali, mida muuta:")
    print("1 - Kasutajanimi")
    print("2 - Parool")
    valik = input("Vali 1 või 2: ")
    
    if valik == "1":
        uus_login = input("Sisesta uus kasutajanimi: ")
        if uus_login in k:
            print("Kasutajanimi juba olemas!")
        else:
            k[index] = uus_login
            print("Kasutajanimi muudetud!")
    elif valik == "2":
        while True:
            uus_psw = input("Sisesta uus parool: ")
            if (any(c.isdigit() for c in uus_psw) and
                any(c.islower() for c in uus_psw) and
                any(c.isupper() for c in uus_psw) and
                any(c in ".,:;!_*-+()/#¤%&" for c in uus_psw)):
                s[index] = uus_psw
                print("Parool muudetud!")
                break
            else:
                if not any(c.isdigit() for c in uus_psw):
                    print("Parool peab sisaldama vähemalt ühte numbrit!")
                if not any(c.islower() for c in uus_psw):
                    print("Parool peab sisaldama vähemalt ühte väikest tähte!")
                if not any(c.isupper() for c in uus_psw):
                    print("Parool peab sisaldama vähemalt ühte suurt tähte!")
                if not any(c in ".,:;!_*-+()/#¤%&" for c in uus_psw):
                    print("Parool peab sisaldama vähemalt ühte erimärki!")
    else:
        print("Vale valik!")


def parooli_taastamine(k:list, s:list) -> None:
    login = input("Sisesta oma kasutajanimi: ")
    if login not in k:
        print("Kasutajat ei leitud!")
        return
    
    str0 = ".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str0 + str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    uus_psw = ''.join([random.choice(ls) for x in range(12)])
    s[k.index(login)] = uus_psw
    print("Sinu uus parool:", uus_psw)