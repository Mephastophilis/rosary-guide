"""
Haily Mary prayer. Contains functions for the triplet at the beginning of the Rosary and for the 5 decades.
Mode is a varible for the option of the abbreviated format wherein the faithful simply repeates the prayer each time before providing an input on the keyboard.
"""
def triplet(mode):
    ordinal = ['first', 'second', 'third']
    if mode == 0:
        print("~Repeat three times. Once on each bead in the triplet.~")
        print("Hail Mary, full of grace,")
        print("the Lord is with thee;")
        print("blessed art thou among women,")
        print("and blessed is the fruit of thy womb, Jesus.")
        print("Holy Mary, Mother of God,")
        print("Pray for us sinners,")
        print("now and at the hour of our death. Amen")
        input()

    else:
        for i in range(3):
            print("~Pray on the " + ordinal[i] + " bead in the triplet.~")
            print("Hail Mary, full of grace,")
            print("the Lord is with thee;")
            print("blessed art thou among women,")
            print("and blessed is the fruit of thy womb, Jesus.")
            print("Holy Mary, Mother of God,")
            print("Pray for us sinners,")
            print("now and at the hour of our death. Amen")
            input()

def decade(mode, decade):
    ordinal = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
    if mode == 0:
        print("~Repeat ten times. Once on each bead in the " + ordinal[decade] + " decade.~")
        print("Hail Mary, full of grace,")
        print("the Lord is with thee;")
        print("blessed art thou among women,")
        print("and blessed is the fruit of thy womb, Jesus.")
        print("Holy Mary, Mother of God,")
        print("Pray for us sinners,")
        print("now and at the hour of our death. Amen")
        input()

    else:
        for i in range(10):
            print("~Pray on the " + ordinal[i] + " bead in the " + ordinal[decade] + " decade.~")
            print("Hail Mary, full of grace,")
            print("the Lord is with thee;")
            print("blessed art thou among women,")
            print("and blessed is the fruit of thy womb, Jesus.")
            print("Holy Mary, Mother of God,")
            print("Pray for us sinners,")
            print("now and at the hour of our death. Amen")
            input()
