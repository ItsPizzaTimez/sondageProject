import os

def clearSys():
    os.system("cls")

def sondage():
    voting = True
    compteur = 0
    vote1 = 0
    vote2 = 0
    vote3 = 0
    vote4 = 0
    vote5 = 0

    bddSondage = {

    }

    while compteur < 5:
        compteur += 1
        choices = str(input("CHOIX :\n- veuillez ajouter un choix (max 5 choix)\n- pour arrêter tapez 0\n> "))
        if choices == "0":
            compteur -= 1
            break
        dictio = {choices:compteur}
        bddSondage.update(dictio)

    while voting:
        clearSys()
        vote = int(input("VOTE :\n- votez une des possibilités {0} suivantes :\n{1}\n- appuyer sur 0 pour arreter le sondage\n> ".format(compteur,bddSondage)))
        if vote == 1:
            clearSys()
            vote1 += 1
            print("vote comptabilisé : {} vote(s)".format(vote1))
        elif vote == 2:
            clearSys()
            vote2 += 1
            print("vote comptabilisé : {} vote(s)".format(vote2))
        elif vote == 3:
            clearSys()
            vote3 += 1
            print("vote comptabilisé : {} vote(s)".format(vote3))
        elif vote == 4:
            clearSys()
            vote4 += 1
            print("vote comptabilisé : {} vote(s)".format(vote4))
        elif vote == 5:
            clearSys()
            vote5 += 1
            print("vote comptabilisé : {} vote(s)".format(vote5))
        elif vote == 0:
            voting = False
        else:
            clearSys()
            print("choix non disponible")
    clearSys()
    print("RESULTATS :\n",bddSondage, "Tirages : ","\n- vote 1 :",vote1,"\n- vote 2 :",vote2,"\n- vote 3 :",vote3,"\n- vote 4 :",vote4,"\n- vote 5 :",vote5)

    main()

def main():
    runningMenu = True
    while runningMenu:
        choiceMenuUser = str(input("\n\n*******************************************************\n\nMENU :\n1- créer un sondage\n2- gérer les options\n3- quitter l'application\n> "))
        if choiceMenuUser == "1":
            clearSys()
            sondage()
            runningMenu = False
        elif choiceMenuUser == "2":
            clearSys()
            print("En travaux !\n")
            continue
        elif choiceMenuUser == "3":
            exit()
        else:
            clearSys()
            print("---CHOIX INCORRECT---")

main()