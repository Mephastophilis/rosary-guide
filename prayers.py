#Apostles' Creed
def ac():
  print("I believe in God, the Father Almighty, Creator of heaven and earth;")
  print("and in Jesus Christ, His only Son, our Lord;")
  print("Who was conceived by the Holy Spirit, born of the Virgin Mary,")
  print("suffered under Pontius Pilate, was crucified, died, and was buried.")
  print("He descended into hell; the third day He arose again from the dead.")
  print("He ascended into heaven, and sits at the right hand of God, the Father Almighty;")
  print("from thence He shall come to judge the living and the dead.")
  print("I believe in the Holy Spirit, the Holy Catholic Church,")
  print("the communion of Saints, the forgiveness of sins,")
  print("the resurrection of the body and life everlasting. Amen.")
  input()

#The Lord's Prayer
def lp():
    print("Our Father, who art in heaven,")
    print("hallowed by thy name;")
    print("Thy kingdom come;")
    print("Thy will be done on earth as it is in heaven.")
    print("Give us this day our daily bread;")
    print("and forgive us our trespasses")
    print("as we forgive those who trespass against us;")
    print("and lead us not into temptation,")
    print("but deliver us from evil. Amen.")
    input()

#Haily Mary prayer. Contains functions for the triplet at the beginning of the Rosary and for the 5 decades. Mode is a varible for the option of the abbreviated format wherein the faithful simply repeates the prayer each time before providing an input on the keyboard.
def hailmary_triplet(mode):
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

def hailmary_decade(mode, decade):
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

#Glory To the Father prayer
def gb():
    print("Glory be to the Father")
    print("and to the son, and to the Holy Spirit")
    print("as it was in the beginning,")
    print("is now, and ever shall be,")
    print("world without end. Amen.")
    input()

#Oh My Jesus prayer
def omj():
    print("Oh my Jesus,")
    print("forgive us our sins,")
    print("save us from the fires of hell,")
    print("lead all souls to Heaven,")
    print("especially those who have the most need of your mercy. Amen.")
    input()

#Hail Holy Queen prayer
def hhq():
  print("Hail, Holy Queen, Mother of Mercy, our life, our sweetness and our hope!")
  print("To thee do we cry, poor banished children of Eve;")
  print("to thee do we send up our sighs, mourning and weeping in this vale of tears.")
  print("Turn then, most gracious advocate, thine eyes of mercy toward us,")
  print("and after this our exile, show unto us the blessed fruit of thy womb, Jesus.")
  print("O clement, O loving, O sweet Virgin Mary!")
  print("     V. Pray for us, O Holy Mother of God. ")
  print("     R. That we may be made worthy of the promises of Christ.")
  input()
