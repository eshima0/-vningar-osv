#detta är swag
import time 
import random
slump = random.randint(1, 10)
klocka = 7.00

#funktioner
#def check2():
    
def check():
    if klocka > 8:
        print("ajdå nu kommer du komma sent till skolan ajdå otur skill issue osv")
        print("nu förlorade du ganska hårt imo gg ez osv")
        
#story
print(f"Mamma väcker dig. Klockan är {klocka:.2f}\n")
time.sleep(1)
if slump > 5:
    klocka = klocka + 0.2
    print(f"Du somnar om.\nKlockan är nu {klocka:.2f}\n")

print("Skriv till Max.\n")
time.sleep(1)
frukost = input("Äter du frukost? [Y]/[N]\n")
if frukost in ("Y", "y"):
    print("Nice 🤤\n")
    klocka = klocka + 0.1
    time.sleep(1)
    print(f"Klockan är nu {klocka:.2f}\n")


elif frukost in ("N", "n"):
    print("ajdå")
    time.sleep(0.5)
    frukost2 = input("och du är säker att du inte vill? [Y]/[N]\n")

    if frukost2 in ("N", "n"):
        print("Nice 🤤\n")
        klocka = klocka + 0.1
        time.sleep(1)
        print(f"Klockan är nu {klocka:.2f}\n")

    if frukost2 in("Y", "y"):
        print("ajdå")
        klocka = klocka + 0.1
        time.sleep(0.3)
        print("\nDu väljer att surfa internet istället.\n")
        print(f"Klockan är nu {klocka:.2f}\n")
        
        print("Det kan börja bli dags att gå till skolan.")
        börjagå = input("Kommer du börja gå till skolan? [Y]/[N]\n")
        if börjagå in ("Y", "y"):
            klocka = 
            print("Nice, du kommer inte sent till skolan")
            print("Du hann dit klockan ")

else:
    print("lägg ner")
    print("rage quit")
    exit()