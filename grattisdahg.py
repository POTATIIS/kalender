import datetime   #lägger till funktionen att jobba med tid
while True:       #låter dig köra programet utan att behöva starta om
    dt = datetime.datetime.now() #sätter variabeln för tiden nu
    personnummer = input("Skriv ditt personnummer(ååååmmdd): ") #säger vad man ska skriva när man kör programmet
    dtpers = dt.strptime(personnummer, '%Y%m%d')
    if (dt.month == dtpers.month and dt.day == dtpers.day):
        print("Grattis på födelsedagen!")
    else:
        print("Inte födelsedag!")
