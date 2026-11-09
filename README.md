D&D 5e Character Creator
A command-line Dungeons & Dragons character creator developed using Python, based on the 2014 edition of D&D Fifth Edition.
Project Overview
My D&D Character Creator is a text-based application that guides users through the process of creating a Dungeons & Dragons character and produces a character sheet they can use in a new campaign or one-shot adventure.

Users can select their character's race, class, background, level, abilities, equipment and other available options. The program calculates relevant statistics and generates a detailed character sheet, reducing the need for players to work through calculations manually or remember every modifier.

This project was developed as part of my software development learning, and I consider it my first major passion project. It demonstrates my understanding of Python programming, user input validation, data structures, functions, calculations, debugging and software testing.
Features
Character Creation
- Character naming and customisation
- Five playable races, including available subraces
- Five playable classes: Barbarian, Fighter, Rogue, Cleric and Wizard
- Background selection
- Character levels from 1 to 20
- Ability score generation and improvements
- Class and subclass selection
- Physical appearance and backstory
Character Statistics
- Ability scores and modifiers
- Proficiency bonuses
- Saving throws and skill proficiencies
- Expertise calculations
- Hit points, armour class and initiative
- Movement speed and hit dice
Class Features
- Barbarian Rage, Brutal Critical and Totem Warrior choices
- Fighter fighting styles, Action Surge and Battle Master manoeuvres
- Rogue Sneak Attack, Expertise and Arcane Trickster spellcasting
- Cleric Divine Domains and Channel Divinity
- Wizard Arcane Recovery, Spell Mastery and Signature Spells
Class features are displayed according to the character's level and selected subclass, with player choices offered where applicable.
Equipment and Spellcasting
- Class and background starting equipment
- Weapon and armour selection
- Equipment proficiency tracking
- Weapon attack and damage calculations
- Shield and two-handed weapon compatibility checks
- Spell selection for supported spellcasting classes
- Spell slots, spellcasting modifiers and spell save DCs
Character Sheet
Once character creation is complete, the application displays a character sheet containing the character's information, statistics, equipment, proficiencies, spells and available features.
Technologies Used
- Python 3 — Main programming language
- Python standard library — Including random and math
- Git — Version control
- GitHub — Source code hosting and project history
The application runs through a terminal or command-line interface.
Installation and Usage
Requirements
- A compatible Python 3 installation
- A terminal or command prompt
Running the Program
1. Clone this repository or download its contents.
2. Open a terminal in the project directory.
3. Run the main Python script:
   python character_creator.py
Depending on your operating system, you may need to use python3 instead of python.
Character Creation Process
The application guides the user through a series of prompts to build a usable D&D character:
1. Enter a character name.
2. Select a race and any applicable subrace.
3. Choose a class.
4. Generate and allocate ability scores.
5. Select a background and character level.
6. Make available class, subclass, equipment and spellcasting choices.
7. Enter character appearance and backstory information.
8. Review the completed character sheet.
The available choices depend on the character's race, class and level, which the user selects according to their preferred playstyle.
Rules and Customisation
This project is primarily based on the Dungeons & Dragons Fifth Edition (2014) ruleset.

Some mechanics have been customised for this application.
Custom Racial Ability Score Bonuses
The application uses a house rule for racial ability score increases:
- Humans: +1 to all six ability scores.
- Non-Humans: +2 to one chosen ability score and +1 to a different chosen ability score.
This replaces the standard fixed racial ability score increases for non-Human races.

The application is a character creation and character-sheet tool, rather than a full combat simulator or virtual tabletop.
Testing and Debugging
The application has undergone extensive manual testing covering character creation, class and racial features, equipment, spellcasting and the completed character sheet.

Testing included characters of different races, classes, subclasses and levels, with particular attention to features that unlock or change at specific levels.

Issues identified during development and testing were investigated and corrected.

One example involved Dragonborn racial features incorrectly appearing on a Human character sheet. The problem was traced to how racial data was selected, and the relevant logic was corrected before retesting.

Other areas reviewed included:
- Fighter Action Surge availability
- Battle Master superiority dice
- Rogue Expertise and Sneak Attack progression
- Arcane Trickster cantrip selection
- Barbarian Totem Warrior features
- Cleric Channel Divinity uses
- Wizard Arcane Recovery calculations
- Equipment compatibility and armour class calculations
The planned manual tests were completed successfully following these corrections.
Skills Demonstrated
Developing this project helped me practise and improve my understanding of:
- Python functions and program structure
- Dictionaries, lists and nested data structures
- Conditional logic and loops
- Input validation and exception handling
- Mathematical calculations and rule implementation
- Debugging and troubleshooting
- Manual testing and regression testing
- Git version control and GitHub workflows
- Developing a larger application incrementally
Current Scope and Limitations
- The application uses a command-line interface rather than a graphical interface.
- It supports five playable classes and five playable races.
- It focuses on character creation and sheet generation, not gameplay or combat simulation.
- It uses selected custom rules and is not intended to be a complete implementation of every D&D 5e character option.
Potential Future Improvements
Possible improvements include:
- Refactoring larger sections into smaller, reusable modules
- Adding automated unit tests
- Supporting additional playable classes and races
- Saving and loading characters
- Exporting character sheets to files
- Developing a graphical user interface
These are potential future improvements I have identified that could enhance the project and improve the user experience.
Project Status
Current status: Functional and manually tested.

The application has completed its planned feature development and testing, with the working version committed and pushed to GitHub.
Disclaimer
This is an independent educational project based on Dungeons & Dragons Fifth Edition (2014). It is not an official Wizards of the Coast product and is not affiliated with or endorsed by Wizards of the Coast.

## Development Process and Evaluation

For a detailed reflection on my development decisions, software
engineering practices, testing, challenges and lessons learned,
see my [Development Process and Evaluation](DEVELOPMENT_EVALUATION.md).
