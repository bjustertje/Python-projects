import random

def gooi_dobbelsteen():
    invoer = input("Druk op enter om te gooien...")
    if invoer == "":
        print("Je hebt " + str(random.randint(1, 6)) + " gegooid!")

gooi_dobbelsteen()