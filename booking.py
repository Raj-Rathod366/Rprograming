#this t_movie function is used to select movie name 
booking = {"k":"booked","j":"booked"}
time = 0
movie = " "

def rv_movie():
    global movie
    global time
    print("WELCOME TO RV CINEMA")
    print("which movie you would like to watch?")
    print("1 :- SALAAR ")
    print("2 :- KGF ")
    print("3 :- ANIMAL")
    print("4 :- ANOR ")
    movie = int(input("choose your movie: "))
    time = rv_time()
    pattern()
    
    

def rv_time():
    print( "\n1: 10.15-1.15 \n2: 1.25-4.25 \n3: 4.35-7.35 \n4: 7.45-10.45")
    t = int(input("SELECT YOU TIME SIR :-"))
    return t

def rv_ppl():
    p = int(input("HOW MANY PEOPLE :-"))
    return p


def pattern():
    print(" _____    _____   _____   _____               _____    _____   _____   _____   \n|     |  |     | |     | |     |             |     |  |     | |     | |     | \n|  Q  |  |  R  | |  S  | |  T  |             |  U  |  |  V  | |  W  | |  X  |\n|_____|  |_____| |_____| |_____|             |_____|  |_____| |_____| |_____|\n")
    print(" _____    _____   _____   _____               _____    _____   _____   _____   \n|     |  |     | |     | |     |             |     |  |     | |     | |     | \n|  I  |  |  J  | |  K  | |  L  |             |  M  |  |  N  | |  O  | |  P  |\n|_____|  |_____| |_____| |_____|             |_____|  |_____| |_____| |_____|\n")
    print(" _____    _____   _____   _____               _____    _____   _____   _____   \n|     |  |     | |     | |     |             |     |  |     | |     | |     | \n|  A  |  |  B  | |  C  | |  D  |             |  E  |  |  F  | |  G  | |  H  |\n|_____|  |_____| |_____| |_____|             |_____|  |_____| |_____| |_____|\n")
    rv_seat()

def rv_seat():
    global booking
    print("booked seats are :-")
    print(booking)
    s = input("\n ENTER SEAT NO :-")
    b = booking.get(s)
    if(b== None):
        booking[s] = "booked"
        print("YOUR SIT HAS BOOKED")
    else:
        print("ITS ALREADY BOOKED")
        rv_seat()

 














