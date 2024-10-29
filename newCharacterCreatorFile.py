#The idea will be that someone presses a button on an interface and it creates a file with as many characters as they want.
#Creates a QTWidget that you enter in a dropdown that passes down how long the character
import sys
from PySide6.QtWidgets import (QApplication, QLineEdit, QWidget, QComboBox, QLabel, QVBoxLayout, QHBoxLayout, QPushButton)
from PySide6.QtCore import Qt
from PySide6.QtCore import Slot  
from PySide6.QtGui import QColor
from __feature__ import snake_case, true_property # type: ignore
import random

my_qt_app = QApplication([])
class characterMaker():
    def __init__(self, filename):
        #Call All The Methods and write them into the file
        self.filename = filename
        self.rollName()
        self.rollRace()
        self.filename = filename
        with open(self.filename, "a") as text:
            text.write("\n")

    def rollAlign(self):
        align = ["Lawful Good", "Nuetral Good", "Chaotic Good", "Lawful Nuetral", "Nuetral Nuetral", "Chaotic Nuetral", "Lawful Evil", "Nuetral Evil", "Chaotic Evil"]
        return random.choice(align)

    def rollName(self):
        name = ["Alice", "Azrael", "Bee", "Brandon", "Ceris", "Crowder", "Daniel", "Desperita", "Eugene", "Eustace", "Feria", "Ferris", "Fan", "Gerald", "Giratina", "Harold", "Harmony", "Iridescent", "Igneus", "Janus", "Jessica", "Jabari", "Jinky", "Karsus", "Kira", "Kayley", "Romulus", "Larry", "Levitana", "Makena", "Mabel", "Mateo", "Nobara", "Nathat", "Nakan", "Orion", "Octavia", "Olive", "Omar", "Patrick", "Periwinkle", "Qing", "Qadir", "Quinn", "Reginald", "Riot", "Revel", "Fear", "Hatred", "Hope", "Samantha", "Sariel", "Sin", "Grace", "Eliza", "Tianyi", "Taylor", "Chang", "Lang", "Long", "Short", "Tall", "Undyne", "Ashe", "Zola", "Urban", "Rural", "Uriel", "Ulla", "Vasilisa", "Victor", "Winona", "Winston", "Xavier", "Xylophone", "Xenos", "Xendara", "Zendaya", "Zuri", "Zaire"] #A big long list of names, two for each letter, one for each standard gender.
        modifier = {
            "Lawful":{"Good": ["Goody Two Shoes", "Courageus", "Unbreakable", "Pacifist", "Paragon"], "Evil":["Tyrant", "Pencil-Pusher", "Accountant", "Sinister Advisor", "Fascist"], "Nuetral":["Conformist", "Law-Abiding", "Empty", "Stiff", "One with a Spear up their Ass"]},
            "Chaotic":{"Good": ["Scoundrel", "Rogueishly Handsome", "Freedom Fighter", "Revolutionary", "Uncornced with what Others Think", "Breaker of Chains", "Anarchist", "Graphiti Artist"], "Evil":["Monster", "Vile", "Baleful", "Childish", "Horrifying"], "Nuetral":["Bastich", "#$^!@#%", "Free", "Patron of Cats and Small Children", "Severely Affected by ADHD"]},
            "Nuetral": {"Good": ["Pure", "Earnest", "Steadfast", "Confused but Well-Intentioned", "Unconcerned with Obstacles"], "Evil":["Giggler", "Cruel", "Practical", "Goal Oriented Asshole", "Coward"], "Nuetral":["Dull", "Boring", "Unopinionated", "Unconcerned", "One who Traps you in Endless Conversation about Nothing in Particular"]}
        }
        align = self.rollAlign()
        alignList = align.split()
        first = alignList[0]
        second = alignList[1]
        with open(self.filename, "a") as text:
            text.write("\nName: "+random.choice(name) + " the " + random.choice(modifier[first][second]) + "\nAlignment: " + align) 

    def printStats(self, stats):
        with open(self.filename, "a") as text:
            text.write("\nStats: ")
            text.write("\n\tStrength: " + str(stats[0]))
            text.write("\n\tDexterity: " + str(stats[1]))
            text.write("\n\tConstitution: " + str(stats[2]))
            text.write("\n\tIntelligence: " + str(stats[3]))
            text.write("\n\tWisdom: " + str(stats[4]))
            text.write("\n\tCharisma: " + str(stats[5]))

    def swap(self, stats, max, core):
        temp = stats[max]
        stats[max] = stats[core]
        stats[core] = temp
    
    def rollClass(self, stats):
            #This is a dictionary that holds all the classes and the position of their most important stat
            charClass = {
                "Artificer":3,
                "Barbarian":2,
                "Bard":5,
                "Cleric":4,
                "Druid":4,
                "Fighter":random.randint(0,1),
                "Monk":1,
                "Paladin":5,
                "Ranger":1,
                "Rogue":1,
                "Sorceror":5,
                "Warlock":5,
                "Wizard":3
            }
            charClassName = random.choice(list(charClass.keys()))
            max = 0
            for i in range(0,6):
                if(stats[i] > stats[max]):
                    max = i
            self.swap(stats, max, charClass[charClassName])
            with open(self.filename, "a") as text:
                text.write("\nClass: " + charClassName)
            return stats

    def rollSingleStat(self):
        smallest = 30
        sum = 0
        for i in range(4):
            roll = random.randint(1,6)
            if(roll < smallest):
                smallest = roll
            sum += roll
        return (sum - smallest)
    
    def rollStats(self):
        stats = [0, 0, 0, 0, 0, 0]
        for i in range(0, 6):
            stats[i] = self.rollSingleStat()
        return stats
    
    def rollRace(self):
        race = {
            "Human":[1,1,1,1,1,1],
            "High Elf":[0,2,0,1,0,0],
            "Wood Elf":[0,2,0,0,1,0],
            "Half Elf":[0,1,1,0,0,2],
            "Aarakocra":[0,2,0,0,1,0],
            "Bugbear":[2,1,0,0,0,0],
            "Centaur":[2,0,0,0,1,0],
            "Hill Dwarf":[0,0,2,0,1,0],
            "Mountain Dwarf":[2,0,2,0,0,0],
            "Sea Elf":[0,2,1,0,0,0],
            "Goblin":[0,2,1,0,0,0],
            "Goliath":[2,0,1,0,0,0],
            "Grung":[0,2,1,0,0,0],
            "Half Orc":[2,0,1,0,0,0],
            "Hobgoblin":[0,0,2,1,0,0],
            "Kenku":[0,2,0,0,1,0],
            "Kobold":[0,2,0,0,0,0],
            "Leonin":[1,0,2,0,0,0],
            "Lizardfolk":[0,0,2,0,1,0],
            "Locathath":[2,1,0,0,0,0],
            "Loxadon":[0,0,2,0,1,0],
            "Minotaur":[2,0,1,0,0,0],
            "Satyr":[0,1,0,0,0,2],
            "Tabaxi":[0,2,0,0,0,1],
            "Tiefling":[0,0,0,1,0,2],
            "Tortle":[2,0,0,0,1,0],
            "Vedalken":[0,0,0,2,1,0],
            "Verdan":[0,0,1,0,0,2],
            "Viashino":[1,2,0,0,0,0],
            "Warforged Skirmisher":[0,2,1,0,0,0],
            "Warforged Juggernaut":[2,0,1,0,0,0],
            "Yuan-Ti Pureblood": [0,0,0,1,0,2]
        }
        raceName = random.choice(list(race.keys()))
        statDist = race[raceName]
        stats = self.rollStats()
        with open(self.filename, "a") as text:
            text.write("\nRace: " + raceName)
        newStats = self.rollClass(stats)
        for i in range(0,6):
            newStats[i] = stats[i] + statDist[i]
        self.printStats(newStats)
         #To be deleted when this is instead passed into a writing function.
        

    # # def rollBackground(self):
    #     theoritcal because the player may want to do this themselves.
    #     pass

class MainWindow(QWidget):
        def __init__(self):
            super().__init__()
            label2 = QLabel("Your File Has Been Created!\nHave A Beautiful Day! -Azrael")
            self.layout = QVBoxLayout()
            self.layout.add_widget(label2)
            self.set_layout(self.layout)
            self.show()

class searchWindow(QWidget):
    def __init__(self, trans):
        super().__init__()
        self.trans = trans
        vbox = QVBoxLayout()
        self.my_le = QLineEdit("Desired File Name And Location: ")
        self.my_le.minimum_width = 250
        self.my_le.select_all()
        my_btn = QPushButton("Create")
        self.my_lbl = QLabel('')
        label = QLabel("Remember To Account For The Relative Location Of This File")
        my_btn.clicked.connect(self.on_submit)
        self.my_le.returnPressed.connect(self.on_submit)
        vbox.add_widget(label)
        vbox.add_widget(self.my_le)
        vbox.add_widget(my_btn)
        vbox.add_widget(self.my_lbl)
        self.set_layout(vbox)

        self.show()

    @Slot()
    def on_submit(self):
        search_term = self.my_le.text
        with open(search_term, "w") as text:
                text.write("Characters")
        for i in range(int(self.trans)):
            characterMaker(search_term)
            with open(search_term, "a") as text:
                text.write("\n")
        #Display a small message that gives the person the relative if
        blah = MainWindow()

class MyDropWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.my_list = ["How Many Characters Do You Want", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11"]    
        self.my_combo_box = QComboBox()
        self.my_combo_box.add_items(self.my_list)
        vbox = QVBoxLayout()
        vbox.add_widget(self.my_combo_box)
        self.set_layout(vbox)
        self.my_combo_box.currentIndexChanged.connect(self.showColor)

    @Slot()
    def showColor(self):
        my_choice = self.my_combo_box.current_index
        charNum = self.my_list[my_choice]
        searchWindow(charNum)
        #After all the things are created change the window so that it says the name of the file and creates it
        # self.newWin.show()

#This clears previous incarnations of the file to write "Characters"
my_drop_window = MyDropWindow()
my_drop_window.show()
sys.exit(my_qt_app.exec())