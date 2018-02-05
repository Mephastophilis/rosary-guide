"""
A python program to guide you through praying the Rosary.
"""
import datetime
import time
import hailmary as hm
from apostlescreed import ac
from lordsprayer import lp
from glorybe import gb
from ohmyjesus import omj
from hailholyqueen import hhq

hmmode=0 #default setting. Abbreviated Hail Mary repetition format.

datetime.datetime.today()
datetime.datetime(2012, 3, 23, 23, 24, 55, 173504)
wd=datetime.datetime.today().weekday()
daysofweek=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
mysteries=[['Joyful Mysteries', 'The Annunciation of the Lord to Mary', 'The Visitation of Mary to Elizabeth', 'The Nativity of our Lord Jesus Christ', 'The Presentation of Our Lord', 'The Finding of Jesus in the Temple at Age 12'], ['Sorrowful Mysteries', 'The Agony of Jesus in the Garden', 'The Scourging at the Pillar', 'Jesus is Crowned with Thorns', 'Jesus is Carried on the Cross', 'The Crucifixion of Our Lord'], ['Glorious Mysteries', 'The Resurrection of Jesus Christ', 'The Ascension of Jesus into Heaven', 'The Descent of the Holy Ghost', 'The Assumption of Mary into Heaven', 'Mary is Crowned as Queen of Heaven and Earth'], ['Luminous Mysteries', 'The Baptism in the Jordan', 'The Wedding at Cana', 'The Proclamation of the Kingdom', 'The Transfiguration', 'The Institution of the Eucharist'], ['Sorrowful Mysteries', 'The Agony of Jesus in the Garden', 'The Scourging at the Pillar', 'Jesus is Crowned with Thorns', 'Jesus is Carried on the Cross', 'The Crucifixion of Our Lord'], ['Joyful Mysteries','The Annunciation of the Lord to Mary', 'The Visitation of Mary to Elizabeth', 'The Nativity of our Lord Jesus Christ', 'The Presentation of Our Lord', 'The Finding of Jesus in the Temple at Age 12'], ['Glorious Mysteries', 'The Resurrection of Jesus Christ', 'The Ascension of Jesus into Heaven', 'The Descent of the Holy Ghost', 'The Assumption of Mary into Heaven', 'Mary is Crowned as Queen of Heaven and Earth']]
Ordinal = ['First', 'Second', 'Third', 'Fourth', 'Fifth']
ordinal = ['first', 'second', 'third', 'fourth', 'fifth']
mystery = wd

print("\nWelcome to the Python3 Rosary Prayer Guide!")

while True:
    print("\nFor instructions, enter 1")
    print("To toggle settings, enter 2")
    print("To begin your prayer session, enter 3")
    print("Enter any other key to quit")

    menus = input()

    if menus == '1':
        print("\nThis is a simple tool to lead you through praying the Rosary")
        print("Each step will instruct where on the Rosary beads to say the prayer.")
        print("~Instructions are marked with squiggles~")
        print("After saying each prayer, press enter to continue.")
        print("Toggle settings to can change the Mysteries you contemplate.")
        print("Enter any key to return to the menu")
        input()

    elif menus == '2':
        print("\nHere in the options menu you can change the Mysteries you contemplate.")
        print("You can also change the how the Hail Mary prayer is displayed.")
        print("The abbreviated form only displays Hail Mary once for each bead set.")
        print("The long form displays Hail Mary for each bead you pray on.")
        print("To toggle the Mysteries of the Rosary, enter 1")
        print("To toggle the Hail Mary display form, enter 2")
        print("Enter any other key to return to the menu.")

        togglemenu = input()

        if togglemenu == '1':
            print("\nToday is " + daysofweek[wd] + " which is a day to pray the " + mysteries[wd][0] + ".")
            print("Enter 1 to pray the "+mysteries[wd][0]+". \nEnter any other key to choose another mystery")
            mysteryoption = input()
            if mysteryoption == '1':
                mystery = datetime.datetime.today().weekday()
            else:
                print("\nEnter 1 for the Joyful Mysteries.")
                print("Enter 2 for the Sorrowful Mysteries.")
                print("Enter 3 for the Glorious Mysteries.")
                print("Enter 4 for the Luminous Mysteries.")
                mysteryoption = input()
                if mysteryoption == '1':
                    mystery = int(mysteryoption)-1
                elif mysteryoption == '2':
                    mystery = int(mysteryoption)-1
                elif mysteryoption == '3':
                    mystery = int(mysteryoption)-1
                elif mysteryoption == '4':
                    mystery = int(mysteryoption)-1
                else:
                    print("\nThat was not an available option. \nThe program will end now and you can try again. \nI'll pray for you.")
                    time.sleep(4)
                    quit()
        elif togglemenu == '2':
            print("\nFor abbreviated Hail Mary display, enter 1.")
            print("For long form Hail Mary display, enter 2.")
            hmoption = input()
            if hmoption == '1':
                hmmode = 0
            elif hmoption == '2':
                hmmode = 1
            else:
                print("\nThat was not an available option. \nThe program will end now and you can try again. \nI'll pray for you.")
                time.sleep(4)
                quit()
        else:
            pass
    elif menus == '3':

        print("\nPlease cross yourself.")
        print("In the name of the Father, the Son, and the Holy Spirit. Amen.")
        input()
        print("~Begin at the Crucifix~")
        ac()
        print("~First bead past the Crucifix~")
        lp()
        hm.triplet(hmmode)
        print("~Pray Glory Be to the Father~")
        gb()

        print("~It is time to contemplate the " + mysteries[mystery][0] + "~")
        print("~Announce the First Mystery at the bead after the triplet.~")
        print("~Then say the Lord's Prayer~")
        print("The First Mystery: "+ mysteries[mystery][1])

        for i in range(5):

            if i==0:
                lp()
                hm.decade(hmmode, i)
                gb()
                omj()

            else:
                print("~After completing the " + ordinal[i-1] + " decade, move to the next bead.")
                print("~Announce the " + Ordinal[i] + " Mystery and then say the Lords Prayer~")
                print("The " + Ordinal[i] + " Mystery: " + mysteries[mystery][i+1])
                lp()

                hm.decade(hmmode, i)
                gb()
                omj()

        print("~Conclude with Rosary by praying Salve Regina.~")
        hhq()
        break

    else:
        quit()
