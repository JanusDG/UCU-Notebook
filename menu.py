import sys
from notebook import Notebook, Note
import string

def train():
    trial_sample = Note("The tester string")
    possible = ['', "object", "atributes", "self", "__init__", "__str__"]

    def show(item):
        result = []
        for i in range(30):
            result.append("\n")
            i+2

        result.append(f"This is the result of type({item}) in the instance of class Notef")
        if possible.index(item) == 1:
            result.append(type(object))
        elif possible.index(item) == 2:
            result.append(type(trial_sample.memo))
        elif possible.index(item) == 3:
            result.append(type(trial_sample))
        elif possible.index(item) == 4:
            result.append(type(trial_sample.__init__))
        elif possible.index(item) == 5:
            result.append(type(trial_sample.__str__))
        result.append("\n")
        result.append(f"This are methods of {item} in the instance of class Note")
        
        if possible.index(item) == 1:
            for item in dir(object):
                result.append(item)
        elif possible.index(item) == 2:
            for item in dir(trial_sample.memo):
                result.append(item)
        elif possible.index(item) == 3:
            for item in dir(trial_sample):
                result.append(item)
        elif possible.index(item) == 4:
            for item in dir(trial_sample.__init__):
                result.append(item)
        elif possible.index(item) == 5:
            for item in dir(trial_sample.__str__):
                result.append(item)
        return result

    
    what_to_do = {}
    what_to_do["1"] = show(possible[1])
    what_to_do["2"] = show(possible[2])
    what_to_do["3"] = show(possible[3])
    what_to_do["4"] = show(possible[4])
    what_to_do["5"] = show(possible[5])

    message = "\n"+"1"+" "+"What is object "+\
                    "\n"+"2"+" "+"What is class atributes "+\
                    "\n"+"3"+" "+"That is self "+\
                    "\n"+"4"+" "+"What is __init__"+\
                    "\n"+"5"+" "+"What is __str__"+\
                    "\n\n"
                    
    while True:
        print()
        print("What exactry do you want to know about OOP?")
        print("P.S type 'q' or Enter to quit ")
        print("Choose from these:")
        print()
        answer = input(message)

        if answer.lower() == "q" or answer == '':
            break
        while answer != 'q' and answer != '' and int(answer) not in range(1,6):
            print("\n"*50)
            print("This is incorrect option")
            print("Please try again")
            print("Chose from these:")
            print()
            answer = input(message)
            
        if answer.lower() == "q" or answer == '':
            break       

        for item in what_to_do[answer]:
            print(item)
        print()
        
    

class Menu:
    '''Display a menu and respond to choices when run.'''
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
                        "1": self.show_notes,
                        "2": self.search_notes,
                        "3": self.add_note,
                        "4": self.modify_note,
                        "5": self.quit
                        }
    
    
    def display_menu(self):
        print("""
        Notebook Menu
        1. Show all Notes
        2. Search Notes
        3. Add Note
        4. Modify Note
        5. Quit
        """)
    
    
    def run(self):
        '''Display the menu and respond to choices.'''
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("{0} is not a valid choice".format(choice))
            
            if choice == '5':
                break
    
    def show_notes(self, notes=None):
        if not notes:
            notes = self.notebook.notes
        for note in notes:
            print("{0}: {1}\n{2}".format(
                    note.id, note.tags, note.memo))
    
    
    def search_notes(self):
        filter = input("Search for: ")
        notes = self.notebook.search(filter)
        self.show_notes(notes)
    
    
    def add_note(self):
        memo = input("Enter a memo: ")
        self.notebook.new_note(memo)
        print("Your note has been added.")
    
    
    def modify_note(self):
        id = input("Enter a note id: ")
        memo = input("Enter a memo: ")
        tags = input("Enter tags: ")
        if memo: self.notebook.modify_memo(id, memo)
        if tags: self.notebook.modify_tags(id, tags)

    
    def quit(self):
        print("Thank you for using your notebook today.")
        proceed = input("Do you want to know more about object oriented programming? [Y/N]")
        if proceed.lower() == "n":
            sys.exit(0)
        else: 
            train()
        
        sys.exit(0)




if __name__ == "__main__":
    Menu().run()
