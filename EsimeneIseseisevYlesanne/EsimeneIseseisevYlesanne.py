import random
def EsimeneIseseisevYlesanne():
    kasutaja = input("Süsteem on ülesse seatud - kas käivitada süsteem (jah/ei)?")
    if kasutaja == 'ei':
        print("Süsteemi ei võeta tööle!")
        return
    min_rõhk = 1.8
    max_rõhk = 2.8
    rõhk = 0
    print("Süvaveepump käivitus!")
    print("Hüdrofoori rõhk:")
    while rõhk < max_rõhk:
        rõhk += 0.15
        print("{0:.2f} bar".format(rõhk))
    print("Süvaveepump seiskus!")
    kasutaja = input("Kas keerata kraanid lahti (jah/ei)?")
    if kasutaja == 'ei':
        return
    pump = False
    tarbimine = False
    while kasutaja == 'jah':
        tarbimine = bool(random.randint(0,1))
        if tarbimine and not pump:
            rõhk -= 0.05
            print("[Seisab] [Tarbitakse] [Alaneb] : {0:.2f} bar".format(rõhk))
        elif tarbimine and pump:
            rõhk += 0.10
            print("[Töötab] [Tarbitakse] [Tõuseb] : {0:.2f} bar".format(rõhk))
        elif not tarbimine and not pump:
            print("[Seisab] [Ei tarbita] [Seisab] : {0:.2f} bar".format(rõhk))
        elif not tarbimine and pump:
            rõhk += 0.15
            print("[Töötab] [Ei tarbita] [Tõuseb] : {0:.2f} bar".format(rõhk))
        if rõhk >= (max_rõhk-0.05) and not pump:
            continue
        elif rõhk <= min_rõhk:
            kasutaja = input("Kas soovite jätkata (jah/ei)?")
            pump = True
        elif rõhk >= (max_rõhk-0.05):
            kasutaja = input("Kas soovite jätkata (jah/ei)?")
            pump = False
        if kasutaja == 'ei':
            print("Süsteem suleti")
EsimeneIseseisevYlesanne()
