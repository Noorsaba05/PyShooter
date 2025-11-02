# Nikkah Process 
class Person:
    def __init__(self, name):
        self.name = name

class Nikkah:
    def __init__(self, groom, bride, mahr, witnesses):
        self.groom = groom
        self.bride = bride
        self.mahr = mahr
        self.witnesses = witnesses

    def perform_nikkah(self):
        if len(self.witnesses) < 2:
            print("y Nikkah cannot be performed. At least 2 witnesses are required.")
            return False

        print("\n Nikkah Ceremony")
        print(f"Groom: {self.groom.name}")
        print(f"Bride: {self.bride.name}")
        print(f"Mahr yes: {self.mahr} agreed upon.")
        print(f"Witnesses: {', '.join(self.witnesses)}")

        
        print("\n Kazi: Do you accept this marriage?")
        response_groom = input(f" {self.groom.name}, do you accept the marriage? (yes/no): ")
        response_bride = input(f" {self.bride.name}, do you accept the marriage? (yes/no): ")

        if response_groom.lower() == 'yes' and response_bride.lower() == 'yes':
            print("\n Nikkah is completed! May Allah bless this marriage.")
            return True
       

groom = Person("Arish")
bride = Person("Noorsaba")
mahr_amount = "100 Euro"
witnesses_list = ["bhalu", "kaalu"]

nikkah_ceremony = Nikkah(groom, bride, mahr_amount, witnesses_list)
nikkah_ceremony.perform_nikkah()
