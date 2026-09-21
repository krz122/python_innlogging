brukernavn = "abc"
passord = "abc"

def loggin():
    b = input ("brukernavn:     ")
    p = input ("passord:    ")
    if b == brukernavn and p == passord:
        print ("du har logget in")
        return True 
    else:
        print ("feil brukernavn eller passord")
        return False

def main():
    state = "start"  # gyldige: "start", "innlogget", "quit"

    while state != "quit":
        if state == "start":
            state = vis_startermeny()
        elif state == "innlogget":
            state = vis_innlogget_meny()


def vis_startermeny():
    print("\n=== StartMeny ===")
    print("1) Logg inn")
    print("2) Registrer ny bruker")
    print("3) Avslutt")

    valg = input("Hva ønsker du å gjøre? ")

    if valg == "1":
        if loggin():
            return "innlogget"
        else:
            return "start"

    elif valg == "2":
        print("Bruker registrert")
        return "start"

    elif valg == "3":
        return "quit"

    else:
        print("Ugyldig valg, prøv på nytt")
        return "start"


def vis_innlogget_meny():
    print("\n=== Meny (innlogget) ===")
    print("1) Fortell vits")
    print("2) Logg ut")
    print("3) Avslutt")

    valg = input("Hva ønsker du å gjøre? ")

    if valg == "1":
        print("Hvorfor gikk datamaskinen til legen? Fordi den hadde virus!")
        return "innlogget"

    elif valg == "2":
        print("Du er logget ut")
        return "start"

    elif valg == "3":
        return "quit"

    else:
        print("Ugyldig valg, prøv igjen")
        return "innlogget"


main()