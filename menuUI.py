from src.service import *


def generateCirclesUI(circles):
    while True:
        try:
            nr = int(input("How many circles do you want to generate? "))
            break
        except ValueError:
            print("The number is not valid!")
    generateCircles(circles, nr)


def deleteCirclesUI(circles):
    pass


def displayCirclesUI(circles):
    displayCircles(circles)


def print_menu():
    options = ["1. Generate circles",
               "2. Delete all circles from a rectangle",
               "3. Display circles",
               "4. EXIT"]

    for option in options:
        print(option)


def run_menu_UI():
    circles = []
    commands = {'1': generateCirclesUI,
                '2': deleteCirclesUI,
                '3': displayCirclesUI}
    while True:
        print_menu()
        command = input("What would you like to do? ")
        try:
            if command in commands:
                commands[command](circles)
            elif command == '4':
                return False
            else:
                print("Invalid option!")
        except ValueError as ve:
            print(str(ve))
