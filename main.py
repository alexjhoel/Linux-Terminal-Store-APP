import sqlite3
from os import system
from datetime import datetime


class bcolors:
    n6 = '\033[96m'
    n7 = '\033[97m'
    n8 = '\033[98m'
    n9 = '\033[99m'
    n10 = '\033[100m'
    n11 = '\033[107m'
    n0 = '\033[90m'
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def command(commando, printall=False, sch=False):
    conn = sqlite3.connect('db.db')

    c = conn.cursor()
    # tienda |name |quantity |cost |

    c.execute(commando)

    print(bcolors.BOLD, end="")
    if sch:
        for i in c.fetchall():
            i = str(i).replace(",", "")
            i = i.replace("(", "")
            print(i.replace(")", ""), end=", ")
    elif printall:

        print(c.fetchall())
    print(bcolors.ENDC)
    conn.commit()

    conn.close()


def START():
    """ Start The Terminal APP """

    system("clear")
    print(bcolors.ENDC, end="")
    print(datetime.today())
    print(bcolors.BOLD + "h For help" + bcolors.ENDC)
    k = True

    while k:
        try:
            inpt = input(bcolors.ENDC + bcolors.n0 + "$ " + bcolors.ENDC + bcolors.BOLD)
            print(bcolors.ENDC, end="")
            if inpt == "h".lower():
                Help()

            elif inpt.lower() == "put":
                print(bcolors.ENDC+bcolors.BOLD+"<Name> <Quantity> <Cost>"+bcolors.ENDC)
                name = input(bcolors.OKGREEN+":Name $ ")
                try:
                    quantity = int(input(bcolors.OKGREEN + ":Quantity $ "))
                except Exception:
                    raise TypeError("Quantity argument type error")
                try:
                    cost = float(input(bcolors.OKGREEN + ":Cost $ "))
                except Exception:
                    raise TypeError("Cost argument type error")
                iD = getA()
                command("INSERT INTO tienda VALUES ("+str(iD)+",'"+str(name)+"',"+str(quantity)+","+str(cost)+");")
                putA(iD)

            elif inpt.lower() == "del":
                ID = input(bcolors.OKGREEN + ":ID $ ")
                Q = input(bcolors.FAIL + "ARE YOU SURE? y/n $ ")
                if Q.lower() == "y":
                    if check(ID):
                        command("DELETE FROM tienda WHERE id="+str(ID)+";")
                        delA(ID)
                    else:
                        raise RuntimeError("ID NOT FOUND")

            elif inpt.lower() == "get":
                name = input(bcolors.OKGREEN+":Name $ ")
                command("SELECT * FROM tienda WHERE name='"+str(name)+"';", sch=True)

            elif inpt.lower() == "sch" or inpt.lower() == "search":
                command("SELECT name FROM tienda", sch=True)

            elif inpt.lower() == "ctm":
                inpt = input(bcolors.OKGREEN+":Command $ ")
                command(inpt, printall=True)
            elif inpt.lower() == "exit" or inpt.lower() == "quit" or inpt.lower() == "ex" or inpt.lower() == "q":
                k = False
                print(bcolors.ENDC)
            elif inpt.lower() == "cl" or inpt.lower() == "clear":
                system("clear")
            elif inpt.lower() == "t" or inpt.lower() == "time":
                print(datetime.today())
        except Exception as e:
            print(str(e))


def Help():
    print(bcolors.ENDC + bcolors.OKBLUE +
          "| Put | -- Put an element in the data base")
    print("| Del | -- Delete an element in the data base")
    print("| Get | -- Get an element by their name")
    print("| H   | -- Show this list of commands")
    print("| Ctm | -- Execute custom db commands")
    print("| RGS | -- New Order")
    print("| Cl , Clear  | -- Clear Terminal")
    print("| Exit , Quit | -- Exit")
    print("| T , Time    | -- Print the time and date")
    print("| Sch, Search | -- Search elements"
          + bcolors.ENDC)


def check(ID):
    fl = open('.Occ', 'r')
    lst = []
    lin = ""
    In=False
    for line in fl:
        for char in line:
            if char == ":":
                In=True
            elif char == ";":
                In=False
                lst.append(int(lin))
                lin = ""
            else:
                lin = lin + char
    fl.close()
    if int(ID) in lst:
        return True
    return False


def getA():
    fl = open('.Occ', 'r')
    lst = []
    lin = ""
    In = False
    for line in fl:
        for char in line:
            if char == ":":
                In = True
            elif char == ";":
                In = False
                lst.append(int(lin))
                lin = ""
            else:
                lin = lin + char
    K=True
    x=0
    while K:
        if not x in lst:
            K=False
        else:
            x += 1
    fl.close()
    return x


def putA(Id):
    """PutA, jsjsjs"""
    fl = open('.Occ', 'a')
    fl.write(":"+str(Id)+";")
    fl.close()


def delA(Id):
    aLl = ""
    with open('.Occ', 'r') as fl:
        aLl = fl.read()
        fl.close()
    aLl = aLl.replace(":"+Id+";", "")
    with open('.Occ', 'w') as fl:
        fl.write(aLl)



START()