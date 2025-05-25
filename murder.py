import time

def print_slow(text):
    """Print text slowly for dramatic effect"""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.03)
    print()

class DetectiveGame:
    def __init__(self):
        self.name = ""
        self.inventory = []
        self.known_clues = []
        self.suspects_questioned = []
        self.game_over = False
        
    def start_game(self):
        """Initialize the game"""
        print_slow("=== TEXT DETECTIVE GAME ===")
        print_slow("You are a famous detective called to investigate a mysterious case.")
        self.name = input("First, tell me your name: ").strip()
        print_slow(f"\nVery well, Detective {self.name}. Let's begin the investigation!")
        self.current_location = "Main Hall"
        self.game_loop()
    
    def game_loop(self):
        """Main game loop"""
        while not self.game_over:
            print_slow(f"\nCurrent Location: {self.current_location}")
            self.show_location_options()
            choice = input("\nWhat will you do? (Enter number or Q to quit): ").strip().upper()
            
            if choice == 'Q':
                self.game_over = True
                print_slow("\nCase suspended. Thanks for playing!")
                break
                
            self.handle_choice(choice)
            
            # Check if player has collected enough clues to solve the case
            if len(self.known_clues) >= 5 and "Study" in self.current_location:
                self.solve_case()
                break
    
    def show_location_options(self):
        """Display available actions for current location"""
        locations = {
            "Main Hall": ["1. Investigate the hall", "2. Go to Dining Room", "3. Go to Study", "4. Go to Bedroom", "5. Review clues"],
            "Dining Room": ["1. Examine dining room", "2. Question the chef", "3. Return to Main Hall", "4. Go to Kitchen", "5. Review clues"],
            "Study": ["1. Search the study", "2. Examine the desk", "3. Return to Main Hall", "4. Check bookshelf", "5. Review clues"],
            "Bedroom": ["1. Inspect bedroom", "2. Check nightstand", "3. Return to Main Hall", "4. Search wardrobe", "5. Review clues"],
            "Kitchen": ["1. Investigate kitchen", "2. Talk to maid", "3. Return to Dining Room", "4. Examine cutlery", "5. Review clues"]
        }
        
        for option in locations.get(self.current_location, []):
            print_slow(option)
    
    def handle_choice(self, choice):
        """Handle player's choice"""
        location_actions = {
            "Main Hall": {
                "1": lambda: self.investigate("You find strange footprints on the hall carpet."),
                "2": lambda: self.move_to("Dining Room"),
                "3": lambda: self.move_to("Study"),
                "4": lambda: self.move_to("Bedroom"),
                "5": self.show_clues
            },
            "Dining Room": {
                "1": lambda: self.investigate("There's a half-empty wine glass and a broken plate on the table."),
                "2": self.question_chef,
                "3": lambda: self.move_to("Main Hall"),
                "4": lambda: self.move_to("Kitchen"),
                "5": self.show_clues
            },
            "Study": {
                "1": lambda: self.investigate("The bookshelf has been ransacked."),
                "2": lambda: self.investigate("You find a torn letter in the desk drawer.", "Torn letter"),
                "3": lambda: self.move_to("Main Hall"),
                "4": lambda: self.investigate("You notice a bookmark in a book about poisons.", "Marked poison book"),
                "5": self.show_clues
            },
            "Bedroom": {
                "1": lambda: self.investigate("The bedsheets are messy, suggesting a struggle."),
                "2": lambda: self.investigate("You find an empty pill bottle on the nightstand.", "Empty pill bottle"),
                "3": lambda: self.move_to("Main Hall"),
                "4": lambda: self.investigate("A coat is missing from the wardrobe.", "Missing coat"),
                "5": self.show_clues
            },
            "Kitchen": {
                "1": lambda: self.investigate("You notice suspicious red stains on a knife.", "Stained knife"),
                "2": self.question_maid,
                "3": lambda: self.move_to("Dining Room"),
                "4": lambda: self.investigate("One of the dinner knives is missing."),
                "5": self.show_clues
            }
        }
        
        action = location_actions.get(self.current_location, {}).get(choice)
        if action:
            action()
        else:
            print_slow("Invalid choice. Please try again.")
    
    def move_to(self, new_location):
        """Move to a new location"""
        print_slow(f"\nYou move from {self.current_location} to {new_location}...")
        self.current_location = new_location
    
    def investigate(self, description, clue=None):
        """Investigate the current location"""
        print_slow("\nYou carefully examine your surroundings...")
        time.sleep(1)
        print_slow(description)
        if clue and clue not in self.known_clues:
            self.known_clues.append(clue)
            print_slow(f"\nNew clue discovered: {clue}!")
    
    def question_chef(self):
        """Question the chef"""
        if "Chef" not in self.suspects_questioned:
            print_slow("\nThe chef wipes sweat from his brow nervously:")
            print_slow('"I went to bed early last night, didn\'t hear anything. Though the master was having business troubles..."')
            self.suspects_questioned.append("Chef")
            self.known_clues.append("Business dispute")
            print_slow("\nNew clue discovered: Business dispute!")
        else:
            print_slow("\nChef: 'I\'ve told you everything I know, detective.'")
    
    def question_maid(self):
        """Question the maid"""
        if "Maid" not in self.suspects_questioned:
            print_slow("\nThe maid appears uneasy:")
            print_slow('"Last night I saw the mistress go to the study very late... This morning the master\'s glass smelled strange..."')
            self.suspects_questioned.append("Maid")
            self.known_clues.append("Mistress's movements")
            print_slow("\nNew clue discovered: Mistress's movements!")
        else:
            print_slow("\nMaid: 'I... I really don\'t know anything else.'")
    
    def show_clues(self):
        """Display collected clues"""
        if not self.known_clues:
            print_slow("\nYou haven't found any clues yet. Keep investigating!")
        else:
            print_slow("\nCollected Clues:")
            for i, clue in enumerate(self.known_clues, 1):
                print_slow(f"{i}. {clue}")
    
    def solve_case(self):
        """Solve the mystery"""
        print_slow("\n\nYou've gathered enough clues. Time to reveal the truth!")
        time.sleep(1)
        print_slow("\nYou piece together the evidence:")
        print_slow("- The mistress visited the study late at night")
        print_slow("- The master's glass had a strange smell")
        print_slow("- A book about poisons was marked in the study")
        print_slow("- An empty pill bottle in the bedroom")
        print_slow("- The master was having business troubles")
        
        time.sleep(2)
        print_slow("\nAfter careful deduction, you conclude:")
        print_slow("The mistress poisoned the master's wine due to his infidelity and financial problems.")
        print_slow("She tried to make it look like suicide, but the empty pill bottle and poison book gave her away.")
        
        time.sleep(1)
        print_slow("\nCongratulations, detective! You've solved the case!")
        self.game_over = True

# Start the game
if __name__ == "__main__":
    game = DetectiveGame()
    game.start_game()