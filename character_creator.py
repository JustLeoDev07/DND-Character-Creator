import random
import math

def roll_dice(sides):
    return random.randint(1, sides)
#For a dice roll, use roll_dice(6) or whatever number you need, d6 = roll_dice(6)  etc etc


print('''
===============================
THE ADVENTURER'S GUILD 
=============================== 
''')
print('Welcome, Adventurer! Here you will start your quest into the many realms you may encounter, but my first question... is your name!')
character_name = input("Enter your character's name: ")
print(f"Nice to meet you, {character_name}!")
print("The next thing you need to do is tell me what race you are?")

all_skill_options = [
    "Acrobatics", "Animal Handling", "Arcana",
    "Athletics", "Deception", "History",
    "Insight", "Intimidation", "Investigation",
    "Medicine", "Nature", "Perception",
    "Performance", "Persuasion", "Religion",
    "Sleight of Hand", "Stealth", "Survival"
]


battle_master_manoeuvres = {
    "Commander's Strike": {
        "description": "Forgo one attack and use a bonus action to let an ally attack using their reaction, adding the superiority die to damage."
    },

    "Disarming Attack": {
        "description": "Add the superiority die to weapon damage. The target makes a Strength save or drops a held item."
    },

    "Distracting Strike": {
        "description": "Add the superiority die to weapon damage. The next attack by another creature against the target gains advantage before your next turn."
    },

    "Evasive Footwork": {
        "description": "While moving, add the superiority die roll to your AC until you stop moving."
    },

    "Feinting Attack": {
        "description": "Use a bonus action to gain advantage on your next attack this turn against a creature within 5 feet, adding the die to damage if it hits."
    },

    "Goading Attack": {
        "description": "Add the superiority die to weapon damage. A failed Wisdom save gives the target disadvantage on attacks against creatures other than you."
    },

    "Lunging Attack": {
        "description": "Increase the reach of a melee weapon attack by 5 feet on your turn, adding the superiority die to damage if it hits."
    },

    "Maneuvering Attack": {
        "description": "Add the superiority die to weapon damage. An ally can use their reaction to move up to half their speed without provoking an opportunity attack from the target."
    },

    "Menacing Attack": {
        "description": "Add the superiority die to weapon damage. A failed Wisdom save frightens the target until the end of your next turn."
    },

    "Parry": {
        "description": "Use your reaction when damaged by a melee attack to reduce the damage by the superiority die roll plus your Dexterity modifier."
    },

    "Precision Attack": {
        "description": "Add the superiority die roll to a weapon attack roll, before or after rolling but before the attack's effects are applied."
    },

    "Pushing Attack": {
        "description": "Add the superiority die to weapon damage. A Large or smaller target that fails a Strength save is pushed up to 15 feet."
    },

    "Rally": {
        "description": "Use a bonus action to grant an ally who can see or hear you temporary hit points equal to the superiority die roll plus your Charisma modifier."
    },

    "Riposte": {
        "description": "When a creature misses you with a melee attack, use your reaction to make a melee weapon attack, adding the die to damage if it hits."
    },

    "Sweeping Attack": {
        "description": "After hitting with a melee weapon attack, potentially damage a second nearby creature for an amount equal to the superiority die roll."
    },

    "Trip Attack": {
        "description": "Add the superiority die to weapon damage. A Large or smaller target that fails a Strength save falls prone."
    }
}

fighting_styles = {
    "Archery": {
        "description": "You gain a +2 bonus to attack rolls you make with ranged weapons."
    },
    "Defense": {
        "description": "While you are wearing armour, you gain a +1 bonus to AC."
    },
    "Dueling": {
        "description": "You gain a +2 damage bonus when wielding a melee weapon in one hand and no other weapons."
    },
    "Great Weapon Fighting": {
        "description": "You can reroll a 1 or 2 on eligible two-handed melee weapon damage dice."
    },
    "Protection": {
        "description": "While wielding a shield, you can use your reaction to impose disadvantage on an attack against another creature within 5 feet."
    },
    "Two-Weapon Fighting": {
        "description": "You can add your ability modifier to the damage of your second attack when two-weapon fighting."
    }
}

weapon_data = {
    "Club": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light"],
        "damage": "1d4",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Dagger": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Light", "Thrown"],
        "damage": "1d4",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Greatclub": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Two-Handed"],
        "damage": "1d8",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Handaxe": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light", "Thrown"],
        "damage": "1d6",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Javelin": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Thrown"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Light Hammer": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light", "Thrown"],
        "damage": "1d4",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Mace": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d6",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Quarterstaff": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d6",
        "damage_type": "Bludgeoning",
        "versatile_damage": "1d8"
    },
    "Sickle": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Light"],
        "damage": "1d4",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Spear": {
        "category": "Simple Weapons",
        "attack_type": "Melee",
        "properties": ["Thrown", "Versatile"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": "1d8"
    },

    # SIMPLE RANGED WEAPONS
    "Light Crossbow": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Loading", "Two-Handed"],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Dart": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Finesse", "Thrown"],
        "damage": "1d4",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Shortbow": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Two-Handed"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Sling": {
        "category": "Simple Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition"],
        "damage": "1d4",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },

    # MARTIAL MELEE WEAPONS
    "Battleaxe": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d8",
        "damage_type": "Slashing",
        "versatile_damage": "1d10"
    },
    "Flail": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d8",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Glaive": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Reach", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Greataxe": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Two-Handed"],
        "damage": "1d12",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Greatsword": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Two-Handed"],
        "damage": "2d6",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Halberd": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Reach", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Lance": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Reach", "Special"],
        "damage": "1d12",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Longsword": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d8",
        "damage_type": "Slashing",
        "versatile_damage": "1d10"
    },
    "Maul": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Two-Handed"],
        "damage": "2d6",
        "damage_type": "Bludgeoning",
        "versatile_damage": None
    },
    "Morningstar": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Pike": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Heavy", "Reach", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Rapier": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse"],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Scimitar": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Light"],
        "damage": "1d6",
        "damage_type": "Slashing",
        "versatile_damage": None
    },
    "Shortsword": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Light"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Trident": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Thrown", "Versatile"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": "1d8"
    },
    "War Pick": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": [],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Warhammer": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Versatile"],
        "damage": "1d8",
        "damage_type": "Bludgeoning",
        "versatile_damage": "1d10"
    },
    "Whip": {
        "category": "Martial Weapons",
        "attack_type": "Melee",
        "properties": ["Finesse", "Reach"],
        "damage": "1d4",
        "damage_type": "Slashing",
        "versatile_damage": None
    },

    # MARTIAL RANGED WEAPONS
    "Blowgun": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Loading"],
        "damage": "1",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Hand Crossbow": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Light", "Loading"],
        "damage": "1d6",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Heavy Crossbow": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Heavy", "Loading", "Two-Handed"],
        "damage": "1d10",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Longbow": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Ammunition", "Heavy", "Two-Handed"],
        "damage": "1d8",
        "damage_type": "Piercing",
        "versatile_damage": None
    },
    "Net": {
        "category": "Martial Weapons",
        "attack_type": "Ranged",
        "properties": ["Special", "Thrown"],
        "damage": None,
        "damage_type": None,
        "versatile_damage": None
    }
}

armour_names = {
    "Padded Armour": {"base_ac": 11, "category": "Light"},
    "Leather Armour": {"base_ac": 11, "category": "Light"},
    "Studded Leather Armour": {"base_ac": 12, "category": "Light"},

    "Hide Armour": {"base_ac": 12, "category": "Medium"},
    "Chain Shirt": {"base_ac": 13, "category": "Medium" },
    "Scale Mail": {"base_ac": 14, "category": "Medium"},
    "Breastplate": {"base_ac": 14, "category": "Medium"},
    "Half Plate": {"base_ac": 15, "category": "Medium"},

    "Ring Mail": {"base_ac": 14, "category": "Heavy"},
    "Chain Mail": {"base_ac": 16, "category": "Heavy"},
    "Splint": {"base_ac": 17, "category": "Heavy"},
    "Plate": {"base_ac": 18, "category": "Heavy"},
}

available_tool_types = {
    "Artisan's Tools": ["Smith's Tools", "Carpenter's Tools", "Alchemist's Tools", "Brewer's Supplies"
                        , "Calligrapher's Supplies", "Cartographer's Tools", "Cobbler's Tools", "Cook's Utensils", "Glassblower's Tools",
                        "Jeweler's Tools", "Leatherworker's Tools", "Mason's Tools", "Painter's Supplies", "Potter's Tools",
                        "Tinker's Tools", "Weaver's Tools", "Woodcarver's Tools"],
    "Gaming Set": ["Dice Set", "Dragonchess set", "Playing Card Set", "Three-Dragon Ante Set"]
}

skill_abilities = {
    "Acrobatics": "dexterity",
    "Animal Handling": "wisdom",
    "Arcana": "intelligence",
    "Athletics": "strength",
    "Deception": "charisma",
    "History": "intelligence",
    "Insight": "wisdom",
    "Intimidation": "charisma",
    "Investigation": "intelligence",
    "Medicine": "wisdom",
    "Nature": "intelligence",
    "Perception": "wisdom",
    "Performance": "charisma",
    "Persuasion": "charisma",
    "Religion": "intelligence",
    "Sleight of Hand": "dexterity",
    "Stealth": "dexterity",
    "Survival": "wisdom"
}

character_races = {
    1: {"name": "Elf",
        "speed": 30,
        "size": "Medium",
        "features": ["Darkvision", "Fey Ancestry", "Trance", "Keen Senses"],
        "skill_proficiencies": ["Perception"],
        "languages": ["Common", "Elvish"],

        "subraces": {
            1: {
                "name": "High Elf",
                "weapon_proficiencies": ["Longsword", "Shortsword", "Shortbow", "Longbow"],
                "extra_languages": 1,
                "features": ["Elf Weapon Training", "Cantrip", "Extra Language"]
            },
            2: {
                "name": "Wood Elf",
                "speed": 35,
                "weapon_proficiencies": ["Longsword", "Shortsword", "Shortbow", "Longbow"],
                "features": ["Elf Weapon Training", "Fleet of Foot", "Mask Of The Wild"],
            },
            3: {"name": "Drow",
                "weapon_proficiencies": ["Rapier", "Shortsword", "Hand Crossbow"],
                "features": ["Superior Darkvision", "Sunlight Sensitivity", "Drow magic", "Drow Weapon Training"]

            }

            }
        },


    2: {"name": "Human",
        "speed": 30,
        "size": "Medium",
        "features": [],
        "skill_proficiencies": [],
        "languages": ["Common"],
        "extra_languages": 1,
        "subraces": {}},

    3: {"name": "Dwarf",
        "speed": 25,
        "size": "Medium",
        "features": ["Darkvision", "Dwarven Resilience", "Dwarven Combat Training", "Tool Proficiency", "Stonecunning", "Dwarven Speed"],
        "skill_proficiencies": [],
        "weapon_proficiencies": ["Battleaxe", "Handaxe", "Light Hammer", "Warhammer"],
        "languages": ["Common", "Dwarvish"],
        "tool_proficiency_choice": ["Smiths Tools", "Brewers Supplies", "Masons Tools"],
        "tool_proficiency_choice_count": 1,

        "subraces": {
            1: {
                "name": "Hill Dwarf",
                "features": ["Dwarven Toughness"]
            },
            2: {
                "name": "Mountain Dwarf",
                "features": ["Dwarven Armour Training"],
                "armour_proficiencies": ["Light Armour", "Medium Armour"]

            }
        }
        },

    4: {"name": "Tiefling",
        "speed": 30,
        "size": "Medium",
        "features": ["Darkvision", "Hellish Resistance", "Infernal Legacy"],
        "skill_proficiencies": [],
        "languages": ["Common", "Infernal"],
        "subraces": {},
        "damage_Resistance": ["Fire"],

        "racial_spells": {
            1: ["Thaumaturgy"],
            3: ["Hellish Rebuke"],
            5: ["Darkness"]
        },
        "racial_spellcasting_stat": "charisma"

        },

    5: {"name": "Dragonborn",
        "speed": 30,
        "size": "Medium",
        "features": ["Draconic Ancestry", "Breath Weapon", "Damage Ressistance"],
        "skill_proficiencies": [],
        "languages": ["Common", "Draconic"],
        "subraces": {
            1: {
                "name": "Black",
                "damage_type": "Acid",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            2: {
                "name": "Blue",
                "damage_type": "Lightning",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            3: {
                "name": "Brass",
                "damage_type": "fire",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            4: {
                "name": "Bronze",
                "damage_type": "Lightning",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            5: {
                "name": "Copper",
                "damage_type": "Acid",
                "breath_shape": "5 x 30ft line",
                "saving_throw": "dexterity"
            },
            6: {
                "name": "Gold",
                "damage_type": "Fire",
                "breath_shape": "15ft cone",
                "saving_throw": "dexterity"
            },
            7: {
                "name": "Green",
                "damage_type": "Poison",
                "breath_shape": "15ft cone",
                "saving_throw": "constitution"
            },
            8: {
                "name": "Red",
                "damage_type": "Fire",
                "breath_shape": "15ft cone",
                "saving_throw": "dexterity",
            },
            9: {
                "name": "Silver",
                "damage_type": "cold",
                "breath_shape": "15ft cone",
                "saving_throw": "constitution"
            },
            10: {
                "name": "White",
                "damage_type": "Cold",
                "breath_shape": "15ft cone",
                "saving_throw": "constitution"
            }
        }
        },
}

character_classes = {
    1: {"name": "Fighter",
        "hit_die": 10,
        "subclass_level": 3,
        "saving_throw_proficiencies": ["Strength", "Constitution"],
        "armour_proficiencies": ["Light Armour", "Medium Armour", "Heavy Armour", "Shields"],
        "weapon_proficiencies": ["Simple Weapons", "Martial Weapons"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["Acrobatics", "Animal Handling", "Athletics", "History", "Insight", "Intimidation", "Perception", "Survival"]
        },
        "level_features": {
            1: ["Fighting Style", "Second Wind"],
            2: ["Action Surge"],
            3: ["Martial Archetype"],
            4: ["Ability Score Improvement"],
            5: ["Extra Attack (2 Attacks)"],
            6: ["Ability Score Improvement"],
            7: ["Martial Archetype Feature"],
            8: ["Ability Score Improvement"],
            9: ["Indomitable (1 Use)"],
            10: ["Martial Archetype Feature"],
            11: ["Extra Attack (3 Attacks)"],
            12: ["Ability Score Improvement"],
            13: ["Indomitable (2 Uses)"],
            14: ["Ability Score Improvement"],
            15: ["Martial Archetype Feature"],
            16: ["Ability Score Improvement"],
            17: ["Action Surge (2 Uses)", "Indomitable (3 Uses)"],
            18: ["Martial Archetype Feature"],
            19: ["Ability Score Improvement"],
            20: ["Extra Attack (4 Attacks)"],
        },
        "subclasses": {
            1: {
                "name": "Champion",
                "level_features": {
                    3: ["Improved Critical"],
                    7: ["Remarkable Athlete"],
                    10: ["Additional Fighting Style"],
                    15: ["Superior Critical"],
                    18: ["Survivor"]

                }
            },

            2: {
                "name": "Battle Master",
                "level_features": {
                    3: ["Combat Superiority", "Student of War"],
                    7: ["Know Your Enemy"],
                    10: ["Improved Combat Superiority (d10)"],
                    15: ["Relentless"],
                    18: ["Improved Combat Superiority (d12)"],
                }
                },
            3: {
                "name": "Eldritch Knight",
                "level_features": {
                    3: ["Spellcasting", "Weapon Bond"],
                    7: ["War Magic"],
                    10: ["Eldritch Strike"],
                    15: ["Arcane Charge"],
                    18: ["Improved War Magic"]
                }
            }
        }
    },


    2: {"name": "Wizard",
        "hit_die": 6,
        "subclass_level": 2,
        "saving_throw_proficiencies": ["Intelligence", "Wisdom"],
        "armour_proficiencies": [],
        "weapon_proficiencies": ["Dagger", "Dart", "Sling", "Quarterstaff", "Light Crossbow"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["Arcana", "History", "Insight", "Investigation", "Medicine", "Religion"]
        },
        "level_features": {
            1: ["Spellcasting", "Arcane Recovery"],
            2: ["Arcane Tradition"],
            3: [],
            4: ["Ability Score Improvement"],
            5: [],
            6: ["Arcane Tradition Feature"],
            7: [],
            8: ["Ability Score Improvement"],
            9: [],
            10: ["Arcane Tradition Feature"],
            11: [],
            12: ["Ability Score Improvement"],
            13: [],
            14: ["Arcane Tradition Feature"],
            15: [],
            16: ["Ability Score Improvement"],
            17: [],
            18: ["Spell Mastery"],
            19: ["Ability Score Improvement"],
            20: ["Signature Spells"]
        },
        "subclasses": {
            1: {
                "name": "School of Abjuration",
                "level_features": {
                    2: ["Abjuration Savant", "Arcane Ward"],
                    6: ["Projected Ward"],
                    10: ["Improved Abjuration"],
                    14: ["Spell Resistance"]
                }
            },
            2: {
                "name": "School of Conjuration",
                "level_features": {
                    2: ["Conjuration Savant", "Minor Conjuration"],
                    6: ["Benign Transposition"],
                    10: ["Focused Conjuration"],
                    14: ["Durable Summons"]
                }
            },
            3: {
                "name": "School of Divination",
                "level_features": {
                    2: ["Divination Savant", "Portent"],
                    6: ["Expert Divination"],
                    10: ["The Third Eye"],
                    14: ["Greater Portent"]
                }
            },
            4: {
                "name": "School of Enchantment",
                "level_features": {
                    2: ["Enchantment Savant", "Hypnotic Gaze"],
                    6: ["Instinctive Charm"],
                    10: ["Split Enchantment"],
                    14: ["Alter Memories"]

                }
            },
            5: {
                "name": "School of Evocation",
                "level_features": {
                    2: ["Evocation Savant", "Sculpt Spells"],
                    6: ["Potent Cantrip"],
                    10: ["Empowered Evocation"],
                    14: ["Overchannel"]
                }
            },
            6: {
                "name": "School of Illusion",
                "level_features": {
                    2: ["Illusion Savant", "Improved Minor Illusion"],
                    6: ["Malleable Illusions"],
                    10: ["Illusory Self"],
                    14: ["Illusory Reality"]
                }
            },
            7: {
                "name": "School of Necromancy",
                "level_features": {
                    2: ["Necromancy Savant", "Grim Harvest"],
                    6: ["Undead Thralls"],
                    10: ["Inured to Undeath"],
                    14: ["Command Undead"]
                }
            },
            8: {
                "name": "School of Transmutation",
                "level_features": {
                    2: ["Transmutation Savant", "Minor Alchemy"],
                    6: ["Transmuter's Stone"],
                    10: ["Shapechanger"],
                    14: ["Master Transmuter"]
                }
            },
        },
        "spellcasting": {
            "ability": "Intelligence",
            "starting_cantrips": 3,
            "starting_spellbook_spells": 6,
            "spells_added_per_level": 2,
            "cantrip_progression": {
                1: 3,
                4: 4,
                10: 5
            }
        }
        },

    3: {"name": "Rogue",
        "hit_die": 8,
        "subclass_level": 3,
        "saving_throw_proficiencies": ["Dexterity", "Intelligence"],
        "armour_proficiencies": ["Light Armour"],
        "weapon_proficiencies": ["Simple Weapons", "Hand Crossbow", "Longsword", "Rapier", "Shortsword",],
        "tool_proficiencies": ["Thieves' Tools"],
        "skill_choices": {
            "amount": 4,
            "options": ["Acrobatics", "Athletics", "Deception", "Insight", "Intimidation", "Investigation", "Perception", "Performance", "Persuasion", "Sleight of Hand", "Stealth"]
        },
        "level_features": {
            1: ["Expertise", "Sneak Attack", "Thieves' Cant"],
            2: ["Cunning Action"],
            3: ["Roguish Archetype"],
            4: ["Ability Score Improvement"],
            5: ["Uncanny Dodge"],
            6: ["Expertise"],
            7: ["Evasion"],
            8: ["Ability Score Improvement"],
            9: ["Roguish Archetype Feature"],
            10: ["Ability Score Improvement"],
            11: ["Reliable Talent"],
            12: ["Ability Score Improvement"],
            13: ["Roguish Archetype Feature"],
            14: ["Blindsense"],
            15: ["Slippery Mind"],
            16: ["Ability Score Improvement"],
            17: ["Roguish Archetype Feature"],
            18: ["Elusive"],
            19: ["Ability Score Improvement"],
            20: ["Stroke of Luck"]
        },
        "subclasses": {
            1: {
                "name": "Thief",
                "level_features": {
                    3: ["Fast Hands", "Second-Story Work"],
                    9: ["Supreme Sneak"],
                    13: ["Use Magic Device"],
                    17: ["Thief's Reflexes"]
                }
            },
            2: {
                "name": "Assassin",
                "level_features": {
                    3: ["Bonus Proficiencies", "Assassinate"],
                    9: ["Infiltration Expertise"],
                    13: ["Impostor"],
                    17: ["Death Strike"]
                }
            },
            3: {
                "name": "Arcane Trickster",
                "level_features": {
                    3: ["Spellcasting", "Mage Hand Legerdemain"],
                    9: ["Magical Ambush"],
                    13: ["Versatile Trickster"],
                    17: ["Spell Thief"]
                },
                "spellcasting": {
                    "ability": "Intelligence",
                    "starts_at_level": 3,
                    "spell_list": "Wizard",
                    "cantrip_progression": {
                        3: 3,
                        10: 4
                    },
                    "spells_known_progression": {
                        3: 3,
                        4: 4,
                        7: 5,
                        8: 6,
                        10: 7,
                        11: 8,
                        13: 9,
                        14: 10,
                        16: 11,
                        19: 12,
                        20: 13
                    },
                    "spell_school_restrictions": ["Enchantment", "Illusion"],
                    "unrestricted_spell_levels": [3,8,14,20]
                }
            }
        },
        "sneak_attack_progression": {
            1: "1d6",
            3: "2d6",
            5: "3d6",
            7: "4d6",
            9: "5d6",
            11: "6d6",
            13: "7d6",
            15: "8d6",
            17: "9d6",
            19: "10d6"
        }
        },


    4: {"name": "Cleric",
        "hit_die": 8,
        "subclass_level": 1,
        "saving_throw_proficiencies": ["Wisdom", "Charisma"],
        "armour_proficiencies": ["Light Armour", "Medium Armour", "Shields"],
        "weapon_proficiencies": ["Simple Weapons"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["History", "Insight", "Medicine", "Persuasion", "Religion"],
        },
        "level_features": {
            1: ["Spellcasting", "Divine Domain"],
            2: ["Channel Divinity (1 Use)","Turn Undead", "Divine Domain Feature"],
            3: [],
            4: ["Ability Score Improvement"],
            5: ["Destroy Undead (CR 1/2)"],
            6: ["Channel Divinity (2 Uses)", "Divine Domain Feature"],
            7: [],
            8: ["Ability Score Improvement", "Destroy Undead (CR 1)", "Divine Domain Feature"],
            9: [],
            10: ["Divine Intervention"],
            11: ["Destroy Undead (CR 2)"],
            12: ["Ability Score Improvement"],
            13: [],
            14: ["Destroy Undead (CR 3)"],
            15: [],
            16: ["Ability Score Improvement"],
            17: ["Destroy Undead (CR 4)", "Divine Domain Feature"],
            18: ["Channel Divinity (3 Uses)"],
            19: ["Ability Score Improvement"],
            20: ["Divine Intervention Improvement"],
        },
        "subclasses": {
            1: {
                "name": "Knowledge Domain",
                "extra_languages": 2,
                "level_features": {
                    1: ["Blessings of Knowledge"],
                    2: ["Channel Divinity: Knowledge of the Ages"],
                    6: ["Channel Divinity: Read Thoughts"],
                    8: ["Potent Spellcasting"],
                    17: ["Visions of the Past"]
                }
            } ,
            2: {
                "name": "Life Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "level_features": {
                    1: ["Bonus Proficiency", "Disciple of Life"],
                    2: ["Channel Divinity: Preserve Life"],
                    6: ["Blessed Healer"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Supreme Healing"]
                }
            },
            3: {
                "name": "Light Domain",
                "level_features": {
                    1: ["Bonus Cantrip", "Warding Flare"],
                    2: ["Channel Divinity: Radiance of the Dawn"],
                    6: ["Improved Flare"],
                    8: ["Potent Spellcasting"],
                    17: ["Corona of Light"]
                }
            },
            4: {
                "name": "Nature Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "level_features": {
                    1: ["Acolyte of Nature", "Bonus Proficiency"],
                    2: ["Channel Divinity: Charm Animals and Plants"],
                    6: ["Dampen Elements"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Master of Nature"]
                }
            },
            5: {
              "name": "Tempest Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "weapon_proficiencies": ["Martial Weapons"],
                "level_features": {
                    1: ["Bonus Proficiencies", "Wrath of the Storm"],
                    2: ["Channel Divinity: Destructive Wrath"],
                    6: ["Thunderbolt Strike"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Stormborn"]
                }
            },
            6: {
              "name": "Trickery Domain",
                "level_features": {
                    1: ["Blessing of the Trickster"],
                    2: ["Channel Divinity: Invoke Duplicity"],
                    6: ["Channel Divinity: Cloak of Shadows"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Improved Duplicity"]
                }
            },
            7: {
                "name": "War Domain",
                "armour_proficiencies": ["Heavy Armour"],
                "weapon_proficiencies": ["Martial Weapons"],
                "level_features": {
                    1: ["Bonus Proficiencies", "War Priest"],
                    2: ["Channel Divinity: Guided Strike"],
                    6: ["Channel Divinity: War God's Blessing"],
                    8: ["Divine Strike (1d8)"],
                    17: ["Avatar of Battle"]
                }
            }
        },
        "spellcasting": {
            "ability": "Wisdom",
            "spell_list": "Cleric",
            "preparation_method": "Prepared",
            "preparation_formula": "Cleric Level + Wisdom Modifier",
            "cantrip_progression": {
                1: 3,
                4: 4,
                10: 5
            }
        }

        },


    5: {"name": "Barbarian",
        "hit_die": 12,
        "subclass_level": 3,
        "saving_throw_proficiencies": ["Strength", "Constitution"],
        "armour_proficiencies": ["Light Armour", "Medium Armour", "Shields"],
        "weapon_proficiencies": ["Simple Weapons", "Martial Weapons"],
        "tool_proficiencies": [],
        "skill_choices": {
            "amount": 2,
            "options": ["Animal Handling", "Athletics", "Intimidation", "Nature", "Perception", "Survival"]
        },
        "level_features": {
            1: ["Rage", "Unarmoured Defense"],
            2: ["Reckless Attack", "Danger Sense"],
            3: ["Primal Path"],
            4: ["Ability Score Improvement"],
            5: ["Extra Attack", "Fast Movement"],
            6: ["Primal Path Feature"],
            7: ["Feral Instinct"],
            8: ["Ability Score Improvement"],
            9: ["Brutal Critical (1 Die)"],
            10: ["Primal Path Feature"],
            11: ["Relentless Rage"],
            12: ["Ability Score Improvement"],
            13: ["Brutal Critical (2 Dice)"],
            14: ["Primal Path Feature"],
            15: ["Persistent Rage"],
            16: ["Ability Score Improvement"],
            17: ["Brutal Critical (3 Dice)"],
            18: ["Indomitable Might"],
            19: ["Ability Score Improvement"],
            20: ["Primal Champion"]
        },
        "subclasses": {
            1: {
                "name": "Path of the Berserker",
                "level_features": {
                    3: ["Frenzy"],
                    6: ["Mindless Rage"],
                    10: ["Intimidating Presence"],
                    14: ["Retaliation"],
                }
            },
            2: {
                "name": "Path of the Totem Warrior",
                "level_features": {
                    3: ["Spirit Seeker", "Totem Spirit"],
                    6: ["Aspect of the Beast"],
                    10: ["Spirit Walker"],
                    14: ["Totemic Attunement"]
                }
            }
        },
        "rage_progression": {
            1: {"uses": 2, "damage_bonus": 2},
            3: {"uses": 3, "damage_bonus": 2},
            6: {"uses": 4, "damage_bonus": 2},
            9: {"uses": 4, "damage_bonus": 3},
            12: {"uses": 5, "damage_bonus": 3},
            16: {"uses": 5, "damage_bonus": 4},
            17: {"uses": 6, "damage_bonus": 4},
            20: {"uses": "Unlimited", "damage_bonus": 4},
        }
        }
}
character_backgrounds = {
    1: {"name": "Acolyte",
        "skill_proficiencies": ["Insight", "Religion"],
        "tool_proficiencies": [],
        "tool_choices": {},
        "extra_languages": 2,
        "equipment": ["Holy Symbol", "Prayer book or Prayer Wheel", "5 Sticks of incense", "Vestments", "Common Clothes", "15GP"],
        "features": {
            "name": "Shelter of the Faithful",
            "description": "You can perform religious ceremonies and receive support from others who share your faith"}
        },

    2: {"name": "Criminal",
        "skill_proficiencies": ["Deception", "Stealth"],
        "tool_proficiencies": ["Thieves' Tools"],
        "tool_choices": {"Gaming Set": 1},
        "extra_languages": 0,
        "equipment": ["Crowbar", "Dark Common Clothes with Hood", "15 GP"],
        "features": {
            "name": "Criminal Contact",
            "description": "You have a reliable contact within the criminal underworld and know how to exchange information"
        }
        },

    3: {"name": "Folk Hero",
        "skill_proficiencies": ["Animal Handling", "Survival"],
        "tool_proficiencies": ["Vehicles (Land)"],
        "tool_choices": {"Artisan's Tools": 1},
        "extra_languages": 0,
        "equipment": ["One Set of Artisan's Tools (Chosen Type)", "Shovel", "Iron Pot", "Common Clothes", "10 GP"],
        "features": {
            "name": "Rustic Hospitality",
            "description": "Common people may shelter you, but they won't risk their lives for you, and you must not have made yourself dangerous to them"
        }
        },
    4: {"name": "Noble",
        "skill_proficiencies": ["History", "Persuasion"],
        "tool_proficiencies": [],
        "tool_choices": {"Gaming Set": 1},
        "extra_languages": 1,
        "equipment": ["Fine Clothes", "Signet Ring", "Scroll of Pedigree", "25 GP"],
        "features": {
            "name": "Position of Privilege",
            "description": "Your noble status grants you access to high society, favourable treatment and opportunities"
        }

        },
    5: {"name": "Sage",
        "skill_proficiencies": ["Arcana", "History"],
        "tool_proficiencies": [],
        "tool_choices": {},
        "extra_languages": 2,
        "equipment": ["Bottle of Black Ink", "Quill", "Small Knife", "Letter from a Deceased Colleague", "Common Clothes", "10 GP"],
        "features": {
            "name": "Researcher",
            "description": "When you do not know a piece of lore, you often know where or from whom you could find the source"
        }
        }
}

available_languages = [
    "Common",
    "Dwarvish",
    "Elvish",
    "Giant",
    "Gnomish",
    "Goblin",
    "Halfling",
    "Orc",
    "Abyssal",
    "Celestial",
    "Draconic",
    "Deep Speech",
    "Infernal",
    "Primordial",
    "Sylvan",
    "Undercommon"
]

def add_equipment(inventory, item_name,quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity

def get_available_weapons(category, attack_type=None):
    available_weapons = []

    for weapon_name, weapon_info in weapon_data.items():
        if weapon_info["category"] == category:
            if attack_type is None or weapon_info["attack_type"] == attack_type:
                available_weapons.append(weapon_name)

    return available_weapons

def get_available_armour(inventory):
    available_armour = []
    for items in inventory:
        if items in armour_names and inventory[items] > 0:
            available_armour.append(items)
    return available_armour

def get_owned_weapons(inventory):
    available_weapons = []
    for items in inventory:
        if items in weapon_data and inventory[items] > 0:
            available_weapons.append(items)
    return available_weapons

def confirm_unequip_shield():
    while True:
        answer = input("\nWould you like to unequip your shield? (yes/no): ").strip().lower()

        if answer == "yes":
            return True
        elif answer == "no":
            return False
        else:
            print("That's not a valid answer, please reply with yes or no!")

def choose_equipped_armour(inventory):
    available_armour = get_available_armour(inventory)
    print("\nChoose which armour you would like to equip:")

    print("0. Remain Unarmoured")
    for number, armour in enumerate(available_armour, start=1):
        print(f"{number}. {armour}")
    while True:
        try:
            choice = int(input("\nEnter the number of the armour you would like to equip:"))

            if choice == 0:
                return None

            elif 1 <= choice <= len(available_armour):
                return available_armour[choice - 1]

            else:
                print("That's not a valid armour!")

        except ValueError:
            print("Please enter a valid armour number!")

def choose_equipped_weapon(inventory, equipped_shield ):
    available_weapons = get_owned_weapons(inventory)

    if not available_weapons:
        print("You don't have any weapons to equip!")
        return [], equipped_shield

    while True:
        print("\nChoose which weapon you would like to equip:")
        print("""Choose how you want to hold your weapons for battle:
        1. One-handed weapon
        2. Two handed weapon
        3. Duel-wield weapons""")
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            print("One-handed weapon selected")

            one_handed_weapons = []

            for weapon in available_weapons:
                if "Two-Handed" not in weapon_data[weapon]["properties"]:
                    one_handed_weapons.append(weapon)

            if not one_handed_weapons:
                print("You don't own any suitable one-handed weapons!")

            else:
                for number, weapon in enumerate(one_handed_weapons, start=1):
                    print(f"{number}. {weapon}")
                while True:
                    try:
                        weapon_choice = int(input("\nEnter the number of the weapon you would like to equip:"))

                        if 1 <= weapon_choice <= len(one_handed_weapons):
                            break
                        else:
                            print("Please enter a valid NUMBER!")

                    except ValueError:
                        print("Please enter a valid number!")
                selected_weapon = one_handed_weapons[weapon_choice - 1]
                return [{"weapon": selected_weapon, "hands": 1}], equipped_shield

        elif choice == "2":
            print("Two-Handed weapon selected")

            two_handed_weapons = []

            for weapon in available_weapons:
                properties = weapon_data[weapon]["properties"]
                if "Two-Handed" in properties or "Versatile" in properties:
                    two_handed_weapons.append(weapon)

            if not two_handed_weapons:
                print("You don't own any suitable weapons to use two-handed!")
            else:
                if equipped_shield:
                    print("\nYou currently have a shield equipped...")
                    print("\nUnfortunately, you cannot use a two-handed weapon and a shield simultaneously.")

                    if confirm_unequip_shield():
                        equipped_shield = False
                        print("Your shield has been unequipped.")
                    else:
                        print("Keeping your shield equipped.")
                        continue

                for number, weapon in enumerate(two_handed_weapons, start=1):
                    print(f"{number}. {weapon}")
                while True:
                    try:
                        weapon_choice = int(input("\nEnter the number of the weapon you would like to equip:"))

                        if 1 <= weapon_choice <= len(two_handed_weapons):
                            break
                        else:
                            print("Please enter a valid NUMBER")

                    except ValueError:
                        print("Please enter a valid number!")
                selected_weapon = two_handed_weapons[weapon_choice - 1]
                print(f"You selected {selected_weapon} to wield with two hands!")

                return [{"weapon": selected_weapon, "hands": 2}], equipped_shield
        elif choice == "3":
            print("Dual-wielding selected")

            dual_wield_weapons = []

            for weapon in available_weapons:
                properties = weapon_data[weapon]["properties"]
                attack_type = weapon_data[weapon]["attack_type"]

                if "Light" in properties and attack_type == "Melee":
                    dual_wield_weapons.append(weapon)

            total_duel_wield_weapons = 0

            for weapon in dual_wield_weapons:
                total_duel_wield_weapons += inventory[weapon]

            if total_duel_wield_weapons < 2:
                print("You need atleast 2 suitable weapons to duel-wield!")

            else:
                if equipped_shield:
                    print("\nYou currently have a shield equipped...")
                    print("\nUnfortunately, you cannot use duel wield with a shield equipped.")

                    if confirm_unequip_shield():
                        equipped_shield = False
                        print("Your shield has been unequipped.")
                    else:
                        print("Keeping your shield equipped.")
                        continue

                for number, weapon in enumerate(dual_wield_weapons, start=1):
                    print(f"{number}. {weapon} (Owned: {inventory[weapon]})")

                while True:
                    try:
                        first_choice = int(input("\nChoose your first weapon:"))

                        if 1 <= first_choice <= len(dual_wield_weapons):
                            break
                        else:
                            print("Please enter a valid weapon NUMBER!")

                    except ValueError:
                        print("Please enter a valid number!")

                first_weapon = dual_wield_weapons[first_choice - 1]
                print(f"First weapon selected: {first_weapon}")

                second_weapon_options = []

                for weapon in dual_wield_weapons:
                    if weapon != first_weapon or inventory[weapon] >= 2:
                        second_weapon_options.append(weapon)

                if not second_weapon_options:
                    print("You don't own any suitable weapons for dual-wielding!")

                else:
                    print("\nChoose your second weapon:")

                    for number, weapon in enumerate(second_weapon_options, start=1):
                        print(f"{number}. {weapon}")

                    while True:
                        try:
                            second_choice = int(input("\nChoose your second weapon: "))

                            if 1<= second_choice <= len(second_weapon_options):
                                break
                            else:
                                print("Please enter a valid NUMBER!")

                        except ValueError:
                            print("Please enter a valid number!")

                    second_weapon = second_weapon_options[second_choice - 1]
                    return [
                        {"weapon": first_weapon, "hands": 1},
                        {"weapon": second_weapon, "hands": 1},
                    ], equipped_shield




        else:
            print("That's not a valid choice!")


def choose_equipped_shield(inventory):
    if inventory.get("Shield", 0) > 0:
        print("\nYou have a shield available to equip")
        while True:
            answer = input("Would you like to equip your shield? (yes/no): ").strip().lower()
            if answer == "yes":
                print("You have equipped your shield!")
                return True
            elif answer == "no":
                return False
            else:
                print("That's not a valid answer now, is it! Answer yes or no.")
    else:
        print("\nYou have no shield available to equip")
        return False


def choose_starting_weapon(category, attack_type=None):
    available_weapons = get_available_weapons(category, attack_type)
    if not available_weapons:
        raise ValueError(
            f"No weapons found for category '{category}' "
            f"and attack type {attack_type}"
        )

    print("\nChoose your starting weapon:")
    for number, weapon in enumerate(available_weapons, start=1):
        print(f"{number}. {weapon}")
    while True:
        try:
            choice = int(input("Choose a weapon by its number:"))
            if 1 <= choice <= len(available_weapons):
                selected_weapon = available_weapons[choice - 1]
                print(f"You have chosen {selected_weapon}!")
                return selected_weapon
            else:
                print("Please choose a number in the LIST!")

        except ValueError:
            print("Please choose a NUMBER in the list!")

def choose_equipment_option(options):
    print("\nChoose your starting equipment:")

    for number, option in enumerate(options, start=1):
        print(f"{number}. {option}")

    while True:
        try:
            choice = int(input("Choose an equipment option by its number:"))
            if 1 <= choice <= len(options):
                selected_equipment = options[choice - 1]
                print(f"You have chosen {selected_equipment}!")
                return selected_equipment
            else:
                print("Please choose a number in the LIST!")

        except ValueError:
            print("Please choose a NUMBER in the list!")

def calculate_armour_class(equipped_armour, equipped_shield, dexterity_modifier, character_class, constitution_modifier):
    if character_class == "Barbarian" and equipped_armour is None:
        armour_class = 10 + dexterity_modifier + constitution_modifier
    elif equipped_armour is None:
        armour_class = 10 + dexterity_modifier
    else:
        armour_info = armour_names[equipped_armour]
        base_ac = armour_info["base_ac"]
        category = armour_info["category"]

        if category == "Light":
            armour_class = base_ac + dexterity_modifier

        elif category == "Medium":
            armour_class = base_ac + min(dexterity_modifier, 2)

        else:
            armour_class = base_ac

    if equipped_shield == True:
        armour_class += 2

    return armour_class

def calculate_weapon_attack_bonus(weapon_name, strength_modifier, dexterity_modifier, proficiency_bonus, known_weapon_proficiencies, attack_mode=None, finesse_ability=None):
    weapon_info = weapon_data[weapon_name]
    weapon_type = weapon_info["attack_type"]
    properties = weapon_info["properties"]

    if attack_mode is None:
        attack_mode = weapon_type

    if attack_mode not in ("Melee", "Ranged", "Thrown"):
        raise ValueError("Invalid attack mode.")

    if attack_mode == "Thrown":
        if weapon_type != "Melee" or "Thrown" not in properties:
            raise ValueError(f"{weapon_name} cannot be thrown.")

    elif attack_mode != weapon_type:
        raise ValueError(f"{weapon_name} cannot use {attack_mode} attacks.")

    if weapon_type == "Melee":
        ability_modifier = strength_modifier
    else:
        ability_modifier = dexterity_modifier

    if "Finesse" in properties:
        if finesse_ability == "Strength":
            ability_modifier = strength_modifier
        elif finesse_ability == "Dexterity":
            ability_modifier = dexterity_modifier
        elif finesse_ability is None:
            ability_modifier = max(strength_modifier, dexterity_modifier)
        else:
            raise ValueError("Finesse ability must be Strength or Dexterity.")

    attack_bonus = ability_modifier

    if (
        weapon_info["category"] in known_weapon_proficiencies
        or weapon_name in known_weapon_proficiencies
    ):
        attack_bonus += proficiency_bonus

    return attack_bonus

def calculate_weapon_damage(weapon_name, hands, strength_modifier, dexterity_modifier, off_hand=False, attack_mode=None, finesse_ability=None, chosen_fighting_styles=None):
    weapon_info = weapon_data[weapon_name]

    weapon_type = weapon_info["attack_type"]
    damage_dice = weapon_info["damage"]
    damage_type = weapon_info["damage_type"]
    properties = weapon_info["properties"]

    if attack_mode is None:
        attack_mode = weapon_type

    if attack_mode not in ("Melee", "Ranged", "Thrown"):
        raise ValueError("Invalid attack mode.")

    if attack_mode == "Thrown":
        if weapon_type != "Melee" or "Thrown" not in properties:
            raise ValueError(f"{weapon_name} cannot use {attack_mode} attacks.")

    elif attack_mode != weapon_type:
        raise ValueError(f"{weapon_name} cannot use {attack_mode} attacks.")

    if damage_dice is None:
        return None, None, None

    if hands == 2 and "Versatile" in properties:
        damage_dice = weapon_info["versatile_damage"]

    if weapon_type == "Melee":
        damage_modifier = strength_modifier
    else:
        damage_modifier = dexterity_modifier

    if "Finesse" in properties:
        if finesse_ability == "Strength":
            damage_modifier = strength_modifier
        elif finesse_ability == "Dexterity":
            damage_modifier = dexterity_modifier
        elif finesse_ability is None:
            damage_modifier = max(strength_modifier, dexterity_modifier)
        else:
            raise ValueError("Finesse ability must be strength or dexterity.")

    damage_modifier = apply_two_weapon_fighting_style(damage_modifier, chosen_fighting_styles or [], off_hand)

    return damage_dice, damage_modifier, damage_type

def get_rage_info(character_level):
    rage_progression = character_classes[5]["rage_progression"]

    applicable_level = max(
        level for level in rage_progression
        if level <= character_level
    )

    return rage_progression[applicable_level]

def qualifies_for_rage_damage(weapon_name, strength_modifier, dexterity_modifier, attack_mode="Melee", finesse_ability=None):
    weapon_info = weapon_data[weapon_name]

    if attack_mode != "Melee":
        return False

    if weapon_info["attack_type"] != "Melee":
        return False

    if "Finesse" in weapon_info["properties"]:
        if finesse_ability == "Strength":
            return True
        elif finesse_ability == "Dexterity":
            return False
        elif finesse_ability is None:
            return strength_modifier >= dexterity_modifier
        else:
            raise ValueError("Finesse ability must be Strength or Dexterity.")

    return True

def calculate_rage_damage_bonus(character_class, character_level, equipped_armour, weapon_name, strength_modifier, dexterity_modifier, attack_mode="Melee", finesse_ability=None):
    if character_class != "Barbarian":
        return 0

    if equipped_armour is not None:
        armour_category = armour_names[equipped_armour]["category"]

        if armour_category == "Heavy":
            return 0

    if not qualifies_for_rage_damage(weapon_name, strength_modifier, dexterity_modifier, attack_mode, finesse_ability):
        return 0

    rage_info = get_rage_info(character_level)

    return rage_info["damage_bonus"]

def calculate_movement_speed(base_speed, character_class, character_level, equipped_armour):

    movement_speed = base_speed

    if character_class != "Barbarian" or character_level < 5:
        return movement_speed

    if equipped_armour is None:
        movement_speed += 10

    else:
        armour_category = armour_names[equipped_armour]["category"]
        if armour_category != "Heavy":
            movement_speed += 10

    return movement_speed

def choose_fighting_styles(character_class, character_level, character_subclass):

    chosen_fighting_styles = []

    if character_class != "Fighter":
        return chosen_fighting_styles

    if character_subclass == "Champion" and character_level >= 10:
        number_of_styles = 2
    else:
        number_of_styles = 1

    print(f"\nAs a fighter you get to choose a fighting style, here is a list of them:")
    for style_name, style_details in fighting_styles.items():
        print(f"{style_name}: {style_details['description']}")

    for choice_number in range(number_of_styles):
        while True:
            chosen_style = input("\nChoose your fighting style: ").strip().title()

            if chosen_style not in fighting_styles:
                print("That Fighting Style does not exist. Choose an existing one.")

            elif chosen_style in chosen_fighting_styles:
                print("You've already selected that Fighting Style...Choose another!")

            else:
                chosen_fighting_styles.append(chosen_style)

                print(f"\nYou have chosen: {chosen_style}")
                print(fighting_styles[chosen_style]["description"])

                break

    return chosen_fighting_styles

def apply_defense_fighting_style(armour_class, chosen_fighting_styles, equipped_armour):

    if "Defense" in chosen_fighting_styles and equipped_armour is not None:
        armour_class += 1

    return armour_class

def apply_archery_fighting_style(attack_bonus, chosen_fighting_styles, weapon_name):

    if "Archery" in chosen_fighting_styles and weapon_data[weapon_name]["attack_type"] == "Ranged":
        attack_bonus += 2

    return attack_bonus

def apply_dueling_fighting_style(damage_modifier, chosen_fighting_styles, weapon_name, wielded_two_handed, wielding_another_weapon):

    if "Dueling" not in chosen_fighting_styles:
        return damage_modifier

    if weapon_data[weapon_name]["attack_type"] != "Melee":
        return damage_modifier

    if "Two-Handed" in weapon_data[weapon_name]["properties"]:
        return damage_modifier

    if wielded_two_handed:
        return damage_modifier

    if wielding_another_weapon:
        return damage_modifier

    damage_modifier += 2
    return damage_modifier

def apply_two_weapon_fighting_style(ability_modifier, chosen_fighting_styles, is_second_weapon_attack):

    if not is_second_weapon_attack:
        return ability_modifier

    if "Two-Weapon Fighting" in chosen_fighting_styles:
        return ability_modifier

    if ability_modifier < 0:
        return ability_modifier
    else:
        return 0

def calculate_sneak_attack(character_class, character_level):
    if character_class != "Rogue":
        return None

    progression = character_classes[3]["sneak_attack_progression"]

    eligible_levels = [
        level for level in progression
        if level <= character_level
    ]

    highest = max(eligible_levels)

    damage_value = progression[highest]

    return damage_value

def calculate_remarkable_athlete_bonus(character_class, character_level, subclass_name, proficiency_bonus):
    if character_class != "Fighter":
        return None

    if subclass_name != "Champion":
        return None

    if character_level < 7:
        return None

    athlete_bonus = math.ceil(proficiency_bonus / 2)

    return athlete_bonus

def calculate_superiority_dice(character_class, character_level, subclass_name):
    if character_class != "Fighter":
        return None

    if subclass_name != "Battle Master":
        return None

    if character_level < 3:
        return None

    if character_level >= 15:
        number_of_dice = 6
    elif character_level >= 7:
        number_of_dice = 5
    else:
        number_of_dice = 4

    if character_level <= 9:
        die_size = "d8"
    elif character_level <= 17:
        die_size = "d10"
    else:
        die_size = "d12"

    return number_of_dice, die_size

def calculate_superiority_dice(character_class, character_level, subclass_name):
    if character_class != "Fighter":
        return None

    if subclass_name != "Battle Master":
        return None

    if character_level < 3:
        return None

    if character_level < 3:
        return None

    if character_level >= 18:
        number_of_dice = 6
        die_size = "d12"

    elif character_level >= 15:
        number_of_dice = 6
        die_size = "d10"

    elif character_level >= 10:
        number_of_dice = 5
        die_size = "d10"

    elif character_level >= 7:
        number_of_dice = 5
        die_size = "d8"

    else:
        number_of_dice = 4
        die_size = "d8"

    return number_of_dice, die_size

def calculate_manoeuvre_save_dc(character_class, character_level, subclass_name, proficiency_bonus, ability_modifier):
    if character_class != "Fighter":
        return None

    if subclass_name != "Battle Master":
        return None

    if character_level < 3:
        return None

    save_dc = 8 + proficiency_bonus + ability_modifier

    return save_dc

def calculate_manoeuvres_known (character_class, character_level, subclass_name):
    if character_class != "Fighter":
        return None

    if subclass_name != "Battle Master":
        return None

    if character_level < 3:
        return None

    if character_level <= 6:
        manoeuvres_known = 3

    elif character_level <= 9:
        manoeuvres_known = 5

    elif character_level <= 14:
        manoeuvres_known = 7

    else:
        manoeuvres_known = 9

    return manoeuvres_known

def choose_manoeuvres(manoeuvres_known):
    if manoeuvres_known is None:
        return []

    chosen_manoeuvres = []

    manoeuvre_names = list(battle_master_manoeuvres)

    for number, name in enumerate(manoeuvre_names, start=1):
        print(f"{number}. {name}")

    for selection in range(manoeuvres_known):
        while True:
            choice = input(f"Choose manoeuvre {selection + 1}: ")

            if not choice.isdigit():
                print("Please enter a number.")
                continue

            choice_number = int(choice)

            if not 1 <= choice_number <= len(manoeuvre_names):
                print("Please choose a valid number.")
                continue

            selected_manoeuvre = manoeuvre_names[choice_number - 1]

            if selected_manoeuvre in chosen_manoeuvres:
                print("You chose this manoeuvre, please pick another one.")
                continue

            chosen_manoeuvres.append(selected_manoeuvre)
            print(f"You have selected: {selected_manoeuvre}")
            break

    return chosen_manoeuvres

def calculate_champion_critical_range(character_class, character_level, subclass_name):
    if character_class != "Fighter":
        return None

    if subclass_name != "Champion":
        return None

    if character_level >= 15:
        return 18

    elif character_level >= 3:
        return 19

    return None

def calculate_channel_divinity_uses(character_class, character_level):
    channel_divinity_uses = None
    if character_class != "Cleric":
        return None

    if character_level < 2:
        return None

    if character_level <= 5:
        channel_divinity_uses = 1

    elif character_level <= 17:
        channel_divinity_uses = 2

    elif character_level <= 20:
        channel_divinity_uses = 3

    return channel_divinity_uses

def barbarian_starting_equipment():
    first_choice = choose_equipment_option(["Greataxe", "Any martial melee weapon"])
    if first_choice == "Greataxe":
        add_equipment(character_equipment, "Greataxe", 1)
    else:
        chosen_weapon = choose_starting_weapon("Martial Weapons", "Melee")
        add_equipment(character_equipment, chosen_weapon, 1)

    second_choice = choose_equipment_option(["Two Handaxes", "Any simple weapon"])
    if second_choice == "Two Handaxes":
        add_equipment(character_equipment, "Handaxe", 2)
    else:
        chosen_weapon = choose_starting_weapon("Simple Weapons")
        add_equipment(character_equipment, chosen_weapon, 1)

    add_equipment(character_equipment, "Explorer's Pack", 1)
    add_equipment(character_equipment, "Javelin", 4)

def wizard_starting_equipment():
    first_choice = choose_equipment_option(["Quarterstaff", "Dagger"])
    add_equipment(character_equipment, first_choice, 1)

    second_choice = choose_equipment_option(["Component Pouch", "Arcane Focus"])
    add_equipment(character_equipment, second_choice, 1)

    third_choice = choose_equipment_option(["Scholar's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, third_choice, 1)

    add_equipment(character_equipment, "Spellbook", 1)

def rogue_starting_equipment():
    first_choice = choose_equipment_option(["Rapier", "Shortsword"])
    add_equipment(character_equipment, first_choice, 1)

    second_choice = choose_equipment_option(["Shortbow and 20 Arrows", "Shortsword"])
    if second_choice == "Shortbow and 20 Arrows":
        add_equipment(character_equipment, "Shortbow", 1)
        add_equipment(character_equipment, "Arrow", 20)
    else:
        add_equipment(character_equipment, "Shortsword", 1)

    third_choice = choose_equipment_option(["Burglar's Pack", "Dungeoneer's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, third_choice, 1)

    add_equipment(character_equipment, "Leather Armour", 1)
    add_equipment(character_equipment, "Dagger", 2)
    add_equipment(character_equipment, "Thieves' Tools", 1)

def fighter_starting_equipment():
    first_choice = choose_equipment_option(["Chain Mail", "Leather Armour, Longbow and 20 Arrows"])
    if first_choice == "Chain Mail":
        add_equipment(character_equipment, "Chain Mail", 1)
    else:
        add_equipment(character_equipment, "Leather Armour", 1)
        add_equipment(character_equipment, "Longbow", 1)
        add_equipment(character_equipment, "Arrow", 20)

    second_choice = choose_equipment_option(["Martial weapon and Shield", "Two martial weapons"])
    if second_choice == "Martial weapon and Shield":
        chosen_weapon = choose_starting_weapon("Martial Weapons")
        add_equipment(character_equipment, chosen_weapon, 1)
        add_equipment(character_equipment, "Shield", 1)
    else:
        first_weapon = choose_starting_weapon("Martial Weapons")
        add_equipment(character_equipment, first_weapon, 1)

        second_weapon = choose_starting_weapon("Martial Weapons")
        add_equipment(character_equipment, second_weapon, 1)

    third_choice = choose_equipment_option(["Light Crossbow and 20 Bolts", "Two Handaxes"])
    if third_choice == "Light Crossbow and 20 Bolts":
        add_equipment(character_equipment, "Light Crossbow", 1)
        add_equipment(character_equipment, "Crossbow Bolt", 20)
    else:
        add_equipment(character_equipment, "Handaxe", 2)

    fourth_choice = choose_equipment_option(["Dungeoneer's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, fourth_choice, 1)

def cleric_starting_equipment():
    first_options = ["Mace"]
    if "Martial Weapons" in known_weapon_proficiencies or "Warhammer" in known_weapon_proficiencies:
        first_options.append("Warhammer")

    first_choice = choose_equipment_option(first_options)
    add_equipment(character_equipment, first_choice, 1)

    second_options = ["Scale Mail", "Leather Armour"]
    if "Heavy Armour" in known_armour_proficiencies:
        second_options.append("Chain Mail")

    second_choice = choose_equipment_option(second_options)
    add_equipment(character_equipment, second_choice, 1)

    third_choice = choose_equipment_option(["Light Crossbow and 20 Bolts", "Any simple weapon"])
    if third_choice == "Light Crossbow and 20 Bolts":
        add_equipment(character_equipment, "Light Crossbow", 1)
        add_equipment(character_equipment, "Crossbow Bolt", 20)

    else:
        chosen_weapon = choose_starting_weapon("Simple Weapons")
        add_equipment(character_equipment, chosen_weapon, 1)

    fourth_choice = choose_equipment_option(["Priest's Pack", "Explorer's Pack"])
    add_equipment(character_equipment, fourth_choice, 1)

    add_equipment(character_equipment, "Shield", 1)
    add_equipment(character_equipment, "Holy Symbol", 1)


def stat_sheet():
    print('\nYour stats:')
    for character_stat, stat in character_stats.items():
        modifier = calculate_modifier(stat)
        print(f"{character_stat.capitalize()}: {stat} ({modifier:+})")

def stat_bonus_allocation(bonus, excluded_stat=None):
    while True:
        choice = input(f'Choose a stat to allocate +{bonus} to ').strip().lower()

        if choice not in character_stats:
            print("Please choose a valid stat!")

        elif choice == excluded_stat:
            print("You've already allocated this bonus to a stat! Choose another.")

        elif character_stats[choice] + bonus > 20:
            print("That increase would take your stat above 20! Choose another stat.")

        else:
            character_stats[choice] += bonus
            print(f"{choice.capitalize()} has increased to {character_stats[choice]}!")
            return choice

def character_race_creation():
    for number, race in character_races.items():
        print(f"{number}. {race["name"]}")
    while True:
        try:
            choice = int(input("choose your race 1-5: "))

            if choice in character_races:
                character_race = character_races[choice]["name"]

                if character_race == "Elf":
                    print(f"Ah, you have chosen to be an {character_race}!")
                else:
                    print(f"You have chosen to be a {character_race}!")


                return character_race

            else:
                print("Choose a valid race!")

        except ValueError:
            print("Please enter a NUMBER between 1 and 5!")

character_race = character_race_creation()

def character_subrace_selection():
    for race_details in character_races.values():
        if race_details["name"] == character_race:

            if race_details["subraces"]:
                print(f"Here are the {character_race}'s subraces:")
                for number, subrace in race_details["subraces"].items():
                    print(f"{number}. {subrace['name']}")
                while True:
                    try:
                        choice = int(input(f"choose a subrace between 1 and {len(race_details['subraces'])}: "))

                        if choice in race_details["subraces"]:
                            subrace = race_details["subraces"][choice]["name"]
                            if character_race == "Dragonborn":
                                print(f"You have chosen to be a {subrace} Dragonborn!")
                            else:
                                print(f"You have chosen to be a {subrace}!")

                            return subrace
                        else:
                            print("Choose a valid subrace!")

                    except ValueError:
                        print(f"Please enter a NUMBER between 1 and {len(race_details['subraces'])}!")

character_subrace =character_subrace_selection()





print(f'Okay {character_name}, tell me what starting class you wish to be? Are you a bruising barbarian, a sneaky rogue, or perhaps an intelligent wizard?')

def character_class_creation():
    for number, class_1 in character_classes.items():
        print(f"{number}. {class_1["name"]}")
    while True:
        try:
            choice = int(input("choose your class 1-5: "))

            if choice in character_classes:
                character_class = character_classes[choice]["name"]
                print(f"Marvellous! You have chosen to be a {character_class}!")

                return character_class

            else:
                print("Choose a valid class!")

        except ValueError:
            print("Please enter a NUMBER between 1 and 5!")

character_class = character_class_creation()

print(f''' 
=========================
YOUR CHARACTER (so far!) 
======================== 
Name: {character_name}
Race: {character_race}
Class: {character_class}
''')

print("""Welcome to the next stage of your adventure: Stats!

Every adventurer has six stats that determine their strengths, weaknesses and talents.

Physical stats
- Strength: Your physical power and athleticism.
- Dexterity: Your agility, coordination and reflexes.
- Constitution: Your stamina and endurance.

Mental stats
- Intelligence: Your knowledge, memory and book-smarts.
- Wisdom: Your awareness, intuition and street-smarts.
- Charisma: Your social confidence and ability to influence others.

How are your stats generated?
For each stat, four six-sided die are rolled and then we discard the lowest result and add the remaining three together.
Each stat sits between 3 and 18
We'll repeat this six times, then you'll get to assign your scores to the six abilities.

Now, adventurer... let the dice decide your fate! 🎲""")

def stat_generation(stat_number):
    dice_rolls = []
    print(f"\nRolling stat {stat_number} of 6...")
    for dice in range(4):
        roll = roll_dice(6)
        dice_rolls.append(roll)
    print('So, you rolled:', dice_rolls)

    lowest = min(dice_rolls)
    print(lowest, "is the lowest die and has been discarded.")

    dice_rolls.remove(lowest)
    stat_total = sum(dice_rolls)

    print(f"Your stat {stat_number} is:", stat_total)

    return stat_total

all_generated_character_stats = []

for number in range(1, 7):
    stat = stat_generation(number)
    all_generated_character_stats.append(stat)

print("\nSo far, these are your stats:")

for number, stat in enumerate(all_generated_character_stats, start=1):
    print(f"{number}. {stat}")

character_stats = {
    "strength": None,
    "dexterity": None,
    "constitution": None,
    "intelligence": None,
    "wisdom": None,
    "charisma": None,
}

used_score = set()

for character_stat in character_stats:
    while True:
        print("\nAvailable stats:")
        for number, stat in enumerate(all_generated_character_stats, start=1):
            if number not in used_score:
                print(f"{number}. {stat}")
        try:
            choice = int(input(f"\nAssign a stat for {character_stat} (1-6): "))

            if choice < 1 or choice > 6:
                print("please choose a number between 1 and 6!")

            elif choice in used_score:
                print("You've already allocated this roll to a stat! Choose another.")

            else:
                selected_score = all_generated_character_stats[choice - 1]
                character_stats[character_stat] = selected_score
                used_score.add(choice)
                break
        except ValueError:
            print("Please enter a NUMBER between 1 and 6!")


def calculate_modifier(stat):
        modifier = (stat - 10) // 2
        return modifier

if character_race == 'Human':
    for character_stat in character_stats:
        character_stats[character_stat]+= 1

    print('\nAs a human, all your stats have increased by +1!')

else:
    stat_sheet()

    print('Now you have your stats, you need to choose where to add your racial modifiers, you can choose one stat to add +2 and one stat to add +1.')
    plus_two_stat = stat_bonus_allocation(2)
    stat_bonus_allocation(1, plus_two_stat)
stat_sheet()


def character_background_creation():
    print("\nChoose your background:")
    for number, background_1 in character_backgrounds.items():
        print(f"{number}. {background_1["name"]}")
    while True:
        try:
            choice = int(input("\nSelect one using 1-5: "))

            if choice in character_backgrounds:
                character_background = character_backgrounds.get(choice)

                if character_background["name"][0].lower() in "aeiou":
                    article = "an"
                else:
                    article = "a"
                print(f"ahh! I hear you used to be/still are {article} {character_background["name"]}!")
                return character_background

            else:
                print("Choose a number for your background from the list!")

        except ValueError:
            print("Please enter a NUMBER between 1 and 5!")

character_background = character_background_creation()

def character_level_creation():
    while True:
        try:
            choice = int(input("choose your character's level from 1-20:"))
            if choice > 20 or choice < 1:
                print("Please choose a number between 1 and 20!")
            else:
                print(f"Your Character level is now {choice}")
                return choice

        except ValueError:
            print("Please enter a NUMBER between 1 and 20!")

character_level = character_level_creation()

earned_asi_levels = []

for class_data in character_classes.values():
    if class_data["name"] == character_class:
        for level, features in class_data["level_features"].items():
            if level <= character_level and "Ability Score Improvement" in features:
                earned_asi_levels.append(level)
        break

print(f"\nYou have earned {len(earned_asi_levels)} Ability Score Improvements.")

for asi_level in earned_asi_levels:
    print(f"\nAllocating your Level {asi_level} Ability Score Improvements.")
    stat_sheet()

    plus_two_options = []
    plus_one_options = []

    for stat_name, stat_value in character_stats.items():
        if stat_value <= 18:
            plus_two_options.append(stat_name)

        if stat_value <= 19:
            plus_one_options.append(stat_name)

    if not plus_two_options and len(plus_one_options) < 2:
        print("All available ability scores are too high to allocate this ability score improvement!")
        print("Fear not adventurer, this ability score Improvement shall remain unused!")
        continue

    while True:
        print("\nHow would you like to allocate this ASI?")
        print("1. Increase one stat by +2")
        print("2. Increase two stats by +1 each")

        choice = input("Choose 1 or 2: ").strip()

        if choice == "1":

            if not plus_two_options:
                print("No stat can receive a +2 bonus. Choose option 2 please.")
                continue

            stat_bonus_allocation(2)
            break

        elif choice == "2":

            if len(plus_one_options) < 2:
                print("You need two different stats that can receive +1.")
                print("Choose option 1 please.")
                continue

            first_stat = stat_bonus_allocation(1)
            stat_bonus_allocation(1, first_stat)
            break

        else:
            print("It was a simple question, 1 or 2...")

if character_class == "Barbarian" and character_level == 20:
    print("\nPRIMAL CHAMPION!")
    print("Your strength and constitution increase by 4, up to a max of 24 - enjoy!")

    for stat in ["strength", "constitution"]:
        character_stats[stat] = min(24, character_stats[stat] + 4)
        print(f"{stat.capitalize()} is now {character_stats[stat]}!")

    stat_sheet()

character_modifiers = {}

for stat_name, stat_value in character_stats.items():
    character_modifiers[stat_name] = calculate_modifier(stat_value)



def calculate_proficiency_bonus(level):
    if level <= 4:
        return 2
    elif level <= 8:
        return 3
    elif level <= 12:
        return 4
    elif level <= 16:
        return 5
    else:
        return 6
proficiency_bonus = calculate_proficiency_bonus(character_level)
print(f"Your proficiency bonus is {proficiency_bonus:+}")

saving_throw_proficiencies = []

for class_data in character_classes.values():
    if class_data["name"] == character_class:
        saving_throw_proficiencies = class_data["saving_throw_proficiencies"].copy()
        break

if character_class == "Rogue" and character_level >= 15:
    saving_throw_proficiencies.append("Wisdom")

saving_throw_bonuses = {}

for stat_name, modifier in character_modifiers.items():
    saving_throw_bonuses[stat_name] = modifier
    if stat_name.capitalize() in saving_throw_proficiencies:
        saving_throw_bonuses[stat_name] = modifier + proficiency_bonus

print("\nYour saving throw bonuses:")

for stat_name, bonus in saving_throw_bonuses.items():
    print(f"{stat_name.capitalize()}: {bonus:+}")

for class_details in character_classes.values():
    if class_details["name"] == character_class:
        hit_die = class_details["hit_die"]
        break

def character_subclass_selection(character_class, character_level):
    for class_data in character_classes.values():
        if class_data["name"] == character_class:
            character_class = class_data
            break
    subclass_level = character_class["subclass_level"]

    if character_level < subclass_level:
        return None

    print("\nChoose your subclass:")

    for number, subclass in character_class["subclasses"].items():
        print(f"{number}. {subclass["name"]}")
    while True:
        try:
            choice = int(input("\n Choose a subclass by its number: "))

            if choice in character_class["subclasses"]:
                selected_subclass = character_class["subclasses"][choice]

                print(f"You have chosen the {selected_subclass["name"]} subclass!")
                return selected_subclass
            else:
                print("Please choose a valid number!")

        except ValueError:
            print("Please enter a NUMBER!")

character_subclass = character_subclass_selection(character_class, character_level)

subclass_name = (
    character_subclass["name"]
    if character_subclass is not None
    else None
)

chosen_fighting_styles = choose_fighting_styles(character_class, character_level, subclass_name)

superiority_dice = calculate_superiority_dice(
    character_class, character_level, subclass_name
)

manoeuvres_known = calculate_manoeuvres_known(
    character_class, character_level, subclass_name
)

chosen_manoeuvres = choose_manoeuvres(manoeuvres_known)

manoeuvre_save_dc = None

if superiority_dice is not None:
    while True:
        chosen_ability = input("Choose to use strength or dexterity for your manoeuvre save DC: ").strip().lower()

        if chosen_ability in ("strength", "dexterity"):
            break

        print("Please enter strength or dexterity for your manoeuvre save DC:")

    chosen_modifier = character_modifiers[chosen_ability]

    manoeuvre_save_dc = calculate_manoeuvre_save_dc(character_class, character_level, subclass_name, proficiency_bonus, chosen_modifier)

if superiority_dice is not None:
    number_of_dice, die_size = superiority_dice

    print(f"""\nBATTLE MASTER FEATURES:
Superiority Dice: {number_of_dice}{die_size}
Superiority Dice Recovery: short or long rest
Manouevre Save DC: {manoeuvre_save_dc}
Manoeuvres Known: {manoeuvres_known}""")
    print("\nChosen Manoeuvres:")

    for manoeuvre in chosen_manoeuvres:
        description = battle_master_manoeuvres[manoeuvre]["description"]
        print(f" {manoeuvre}: {description}")


remarkable_athlete_bonus = calculate_remarkable_athlete_bonus(
    character_class,
    character_level,
    subclass_name,
    proficiency_bonus
)

champion_critical_range = calculate_champion_critical_range(character_class, character_level, subclass_name)

channel_divinity_uses = calculate_channel_divinity_uses(character_class, character_level)
if channel_divinity_uses is not None:
    print(f"\nAs a cleric, you have {channel_divinity_uses} use(s) of channel divinity, use it wisely! ")

print("""\n 
===================
Hit Points (HP) 
==================

Hit points show how much damage your character can take before falling unconscious. 

If your character falls below to zero HP or lower then they will be unconscious and have to roll death saving throws to stay alive. 

At level 1, your HP is calculated by your constitution stat-bonus, added to your classes hit die. 

Every additional level gained gives you more HP to reflect your character getting tougher, you roll your character's hit die and add your constitution stat-bonus to determine your new max HP.

Did you know: some DMS consider catastrophic damage a rule, where if your character drops below their HP in the negative value then they instantly die! Be careful, adventurer...

""")

def calculate_hit_points(level, hit_die, constitution_modifier):
    first_level_hp = max(1, hit_die + constitution_modifier)
    print(f'Your starting HP at Level 1 is {first_level_hp}!')
    print(f"Your final constitution modifier is {constitution_modifier:+} - we use this when you level up to add to the HP roll!")
    total_hp = first_level_hp

    for current_level in range(2, level + 1):
        print(f"\nGenerating HP for level {current_level}...")
        hp_roll = roll_dice(hit_die)
        print(f"\nrolled {hp_roll} on a d{hit_die}")


        new_level_hp_bonus = max(1, hp_roll + constitution_modifier)
        print(f"Your level {current_level} HP increase is +{new_level_hp_bonus}!")


        total_hp += new_level_hp_bonus
        print(f"Your total HP at Level {current_level} is now {total_hp}!")

    if character_subrace == "Hill Dwarf":
        total_hp += level
        print(f"\nDwarven Toughness grants you {level} more HP!")

    print(f"\nYour final maximum HP at level {level} is {total_hp}!")
    return total_hp

character_hp = calculate_hit_points(character_level, hit_die, character_modifiers["constitution"])

initiative_bonus = character_modifiers["dexterity"]

if remarkable_athlete_bonus is not None:
    initiative_bonus += remarkable_athlete_bonus


print(f"""\n To determine how quickly your character reacts to combat, you will need to roll initiative when your DM asks! 

Your initiative bonus is {initiative_bonus:+}! 
Add this to your roll for that sweet added bonus!""")

for race_details in character_races.values():
    if race_details["name"] == character_race:
        movement_speed = race_details["speed"]

        if character_subrace == "Wood Elf":
            movement_speed = race_details["subraces"][2]["speed"]

        break


if character_race == "Dragonborn":
    display_race = f"{character_subrace} Dragonborn"
elif character_subrace:
    display_race = character_subrace
else:
    display_race = character_race

if display_race[0].lower() in "aeiou":
    article = "an"
else:
    article = "a"


for languages in character_races.values():
    if languages["name"] == character_race:
        known_character_languages = languages["languages"].copy()
        extra_languages = languages.get("extra_languages", 0)

        extra_languages += character_background.get("extra_languages", 0)

        if character_subclass is not None:
            extra_languages += character_subclass.get("extra_languages", 0)

        for subrace in languages["subraces"].values():
            if subrace["name"] == character_subrace:
                extra_languages += subrace.get("extra_languages", 0)
                break

        if extra_languages > 0:
            print(f"\nYou can choose {extra_languages} additional language(s)!")



            for language_choice in range(extra_languages):
                print(f"\nChoose language {language_choice + 1} of {extra_languages}:")
                print("Here is a list of available languages:")

                selectable_languages = []

                for language in available_languages:
                    if language not in known_character_languages:
                        selectable_languages.append(language)

                for number, language in enumerate(selectable_languages, start=1):
                    print(f"{number}. {language}")
                while True:
                    try:
                        choice = int(input(f"Choose a language by its number: "))

                        if 1 <= choice <= len(selectable_languages):
                            selected_language = selectable_languages[choice - 1]
                            known_character_languages.append(selected_language)

                            print(f"You have chosen to learn {selected_language}!")
                            break
                        else:
                            print("Please choose a valid number!")

                    except ValueError:
                        print("Please enter a NUMBER!")


        break

if character_class == "Rogue":
    known_character_languages.append("Thieves' Cant")

print("\nYour character knows the following languages:")

for language in known_character_languages:
    print(f"- {language}")

known_character_skills = []
expertise_skills = []
expertise_tools = []
known_character_tools = []

character_equipment = {}
equipped_armour = None
equipped_shield = False
equipped_weapons = []

for race in character_races.values():
    if race["name"] == character_race:
        known_character_skills.extend(race.get("skill_proficiencies", []))
        break

known_character_skills.extend(character_background.get("skill_proficiencies", []))

print("\n Your starting skill proficiencies:")
for skill in known_character_skills:
    print(f"- {skill}")

available_skill_choices = []
for classes in character_classes.values():
    if classes["name"] == character_class:
        for skill in classes["skill_choices"]["options"]:
            if skill not in known_character_skills:
                available_skill_choices.append(skill)

        skill_choice_amount = classes["skill_choices"]["amount"]
        for skill_choice in range(skill_choice_amount):
            print(f"\nChoose skill {skill_choice + 1} of {skill_choice_amount}:")
            for number, skill in enumerate(available_skill_choices, start=1):
                print(f"{number}. {skill}")
            while True:
                try:
                    choice = int(input(f"Choose a skill by its number to be proficient in: "))
                except ValueError:
                    print("please enter a NUMBER!")
                    continue

                if 1 <= choice <= len(available_skill_choices):
                   break
                else:
                   print("Please choose a number listed in the menu!")

            selected_skill = available_skill_choices[choice - 1]
            known_character_skills.append(selected_skill)
            available_skill_choices.remove(selected_skill)

        break
if character_class == "Cleric":
    if character_subclass is not None:
        if character_subclass["name"] == "Knowledge Domain":
            if character_level >= 1:

                knowledge_skill_options = ["Arcana", "History", "Nature", "Religion"]

                available_knowledge_skills = knowledge_skill_options.copy()

                for skill_choice in range(2):
                    print(f"\nChoose Knowledge Skill {skill_choice + 1} of 2:")

                    for number, skill in enumerate(available_knowledge_skills, start=1):
                        print(f"{number}. {skill}")

                    while True:
                        try:
                            choice = int(input(f"Choose a skill by its number to be proficient in: "))
                        except ValueError:
                            print("please enter a NUMBER!")
                            continue

                        if 1 <= choice <= len(available_knowledge_skills):
                            break
                        else:
                            print("Please choose a number listed in the menu!")

                    selected_skill = available_knowledge_skills[choice - 1]


                    if selected_skill not in known_character_skills:
                        known_character_skills.append(selected_skill)

                    if selected_skill not in expertise_skills:
                        expertise_skills.append(selected_skill)

                    available_knowledge_skills.remove(selected_skill)


if character_class == "Cleric":
    if character_subclass is not None:
        if character_subclass["name"] == "Nature Domain":
            if character_level >= 1:
                available_nature_skills = []
                nature_skill_options = ["Animal Handling", "Nature", "Survival"]

                for skill in nature_skill_options:
                    if skill not in known_character_skills:
                        available_nature_skills.append(skill)

                if not available_nature_skills:
                    print("\nYou are already proficient in all three Nature Domain Skills!")
                    print("Choose a different skill:")

                    for skill in all_skill_options:
                        if skill not in known_character_skills:
                            available_nature_skills.append(skill)

                if available_nature_skills:
                    print("\nChoose 1 Skill proficiency:")

                    for number, skill in enumerate(available_nature_skills, start=1):
                        print(f"{number}. {skill}")

                    while True:
                        try:
                            choice = int(input(f"Choose a skill by its number to be proficient in: "))
                        except ValueError:
                            print("please enter a NUMBER!")
                            continue

                        if 1 <= choice <= len(available_nature_skills):
                            break
                        else:
                            print("Please choose a number listed in the menu!")

                    selected_skill = available_nature_skills[choice - 1]

                    if selected_skill not in known_character_skills:
                        known_character_skills.append(selected_skill)

                else:
                    print("You have every skill proficiency in the game, fucking nerd...")


def choose_tools(tool_options, amount):
    available_tool_choices = tool_options.copy()

    for tool in known_character_tools:
        if tool in available_tool_choices:
            available_tool_choices.remove(tool)

    for tool_choice in range(amount):
        print(f"\nChoose Tool {tool_choice + 1} of {amount}:")

        for number, tool in enumerate(available_tool_choices, start=1):
            print(f"{number}. {tool}")

        while True:
            try:
                choice = int(input("Choose a tool by its number to be proficient in: "))
            except ValueError:
                print("Please enter a NUMBER!")
                continue

            if 1 <= choice <= len(available_tool_choices):
                break
            else:
                print("Please choose a number listed in the menu!")

        selected_tool = available_tool_choices[choice - 1]

        known_character_tools.append(selected_tool)
        available_tool_choices.remove(selected_tool)


for race in character_races.values():
    if race["name"] == character_race:
        for tool in race.get("tool_proficiencies", []):
            if tool not in known_character_tools:
                known_character_tools.append(tool)
        break

for tool in character_background.get("tool_proficiencies", []):
    if tool not in known_character_tools:
        known_character_tools.append(tool)

for classes in character_classes.values():
    if classes["name"] == character_class:
        for tool in classes["tool_proficiencies"]:
            if tool not in known_character_tools:
                known_character_tools.append(tool)
        break


background_tools_choices = character_background.get("tool_choices", {})

for tool_category, tool_choice_amount in background_tools_choices.items():
    choose_tools(available_tool_types[tool_category], tool_choice_amount)

if character_race == "Dwarf":
    dwarf_tools = [
        "Smith's Tools",
        "Brewer's Supplies",
        "Mason's Tools"
    ]

    choose_tools(dwarf_tools, 1)

if character_class == "Fighter":
    if character_subclass is not None:
        if character_subclass["name"] == "Battle Master":
            if character_level >= 3:
                choose_tools(available_tool_types["Artisan's Tools"], 1)


if character_class == "Rogue":
    if character_subclass is not None:
        if character_subclass["name"] == "Assassin":
            if character_level >= 3:
                for tool in ["Disguise Kit", "Poisoner's Kit"]:
                    if tool not in known_character_tools:
                        known_character_tools.append(tool)


print("\nKnown tool proficiencies:", known_character_tools)

if character_class == "Rogue":
    if character_level >= 1:
        print("\nAs a rogue, you gain expertise at Level 1!")

        available_expertise_skills = []

        for skill in known_character_skills:
            if skill not in expertise_skills:
                available_expertise_skills.append(skill)

        if "Thieves' Tools" in known_character_tools:
            if "Thieves' Tools" not in expertise_tools:
                available_expertise_skills.append("Thieves' Tools")


        expertise_choices_made = 0
        while expertise_choices_made < 2:
            print("\nChoose your Rogue Expertise Proficiencies:")

            for number, option in enumerate(available_expertise_skills, start=1):
                print(f"{number}. {option}")

            choice = input("\nChoose an expertise proficiency with the numbers in the list: ")
            if not choice.isdigit():
                print("Please enter a NUMBER!")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(available_expertise_skills):
                print("Please choose an expertise proficiency with the NUMBERS in the LIST!")
                continue

            selected_expertise = available_expertise_skills[choice - 1]

            if selected_expertise == "Thieves' Tools":
                expertise_tools.append(selected_expertise)
            else:
                expertise_skills.append(selected_expertise)

            available_expertise_skills.remove(selected_expertise)

            expertise_choices_made += 1
            print(f"Expertise gained: {selected_expertise}")

        print("\nExpertise skills:", expertise_skills)
        print("Expertise tools:", expertise_tools)

    if character_level >=6:
        print("\nAs a rogue, you gain two more expertise at Level 6!")
        available_expertise_skills = []

        for skill in known_character_skills:
            if skill not in expertise_skills:
                available_expertise_skills.append(skill)

        expertise_choices_made = 0

        while expertise_choices_made < 2:
            print("\nChoose your Level 6 Rogue Expertise Proficiencies:")

            for number, option in enumerate(available_expertise_skills, start=1):
                print(f"{number}. {option}")

            choice = input("\nChoose an expertise proficiency with the numbers in the list: ")

            if not choice.isdigit():
                print("Please enter a NUMBER!")
                continue

            choice = int(choice)

            if choice < 1 or choice > len(available_expertise_skills):
                print("Please choose an expertise proficiency with the NUMBERS in the LIST!")
                continue

            selected_expertise = available_expertise_skills[choice - 1]

            expertise_skills.append(selected_expertise)

            available_expertise_skills.remove(selected_expertise)

            expertise_choices_made += 1
            print(f"Expertise gained: {selected_expertise}")

skill_bonuses = {}

for skill_name, ability_name in skill_abilities.items():
    modifier = character_modifiers[ability_name]
    skill_bonuses[skill_name] = modifier

    if skill_name in expertise_skills:
        skill_bonuses[skill_name] = modifier + (proficiency_bonus * 2)

    elif skill_name in known_character_skills:
        skill_bonuses[skill_name] = modifier + proficiency_bonus

    elif remarkable_athlete_bonus is not None and ability_name in ("strength", "dexterity", "constitution"):
        skill_bonuses[skill_name] = modifier + remarkable_athlete_bonus

print("\nYour Skill proficiencies and bonuses:")
for skill,bonus in skill_bonuses.items():
    if skill in expertise_skills:
        print(f"- {skill}: {bonus:+} (Expertise)")
    elif skill in known_character_skills:
        print(f"- {skill}: {bonus:+} (Proficient)")
    elif remarkable_athlete_bonus is not None and skill_abilities[skill] in ("strength", "dexterity", "constitution"):
        print(f"- {skill}: {bonus:+} (Remarkable Athlete)")
    else:
        print(f"- {skill}: {bonus:+}")



print('\nYour tools proficiencies:')
for tool in known_character_tools:
    if tool in expertise_tools:
        print(f"- {tool} (Expertise)")
    else:
        print(f"- {tool} (Proficient)")


known_armour_proficiencies = []
known_weapon_proficiencies = []

for class_details in character_classes.values():
    if class_details["name"] == character_class:
        known_armour_proficiencies.extend(class_details.get("armour_proficiencies", []))
        known_weapon_proficiencies.extend(class_details.get("weapon_proficiencies", []))
        break

for race_details in character_races.values():
    if race_details["name"] == character_race:

        for armour in race_details.get("armour_proficiencies", []):
            if armour not in known_armour_proficiencies:
                known_armour_proficiencies.append(armour)

        for weapon in race_details.get("weapon_proficiencies", []):
            if weapon not in known_weapon_proficiencies:
                known_weapon_proficiencies.append(weapon)

        for subrace_details in race_details["subraces"].values():
            if subrace_details["name"] == character_subrace:

                for armour in subrace_details.get("armour_proficiencies", []):
                    if armour not in known_armour_proficiencies:
                        known_armour_proficiencies.append(armour)

                for weapon in subrace_details.get("weapon_proficiencies", []):
                    if weapon not in known_weapon_proficiencies:
                        known_weapon_proficiencies.append(weapon)

                break

if character_subclass is not None:
    for armour in character_subclass.get("armour_proficiencies", []):
        if armour not in known_armour_proficiencies:
            known_armour_proficiencies.append(armour)

    for weapon in character_subclass.get("weapon_proficiencies", []):
        if weapon not in known_weapon_proficiencies:
            known_weapon_proficiencies.append(weapon)



filtered_weapon_proficiencies = []
for weapon in known_weapon_proficiencies:
    category = weapon_data.get(weapon, {}).get("category")
    if category not in known_weapon_proficiencies:
        filtered_weapon_proficiencies.append(weapon)

known_weapon_proficiencies = filtered_weapon_proficiencies

print("\nArmour proficiencies:", known_armour_proficiencies)
print("Weapon proficiencies:", known_weapon_proficiencies)

if character_class == "Barbarian":
    barbarian_starting_equipment()
if character_class == "Wizard":
    wizard_starting_equipment()
if character_class == "Rogue":
    rogue_starting_equipment()
if character_class == "Fighter":
    fighter_starting_equipment()
if character_class == "Cleric":
    cleric_starting_equipment()

print("\nCurrent inventory", character_equipment)

equipped_armour = choose_equipped_armour(character_equipment)
movement_speed = calculate_movement_speed(movement_speed, character_class, character_level, equipped_armour)
equipped_shield = choose_equipped_shield(character_equipment)

equipped_weapons, equipped_shield = choose_equipped_weapon(character_equipment, equipped_shield)

print(f"\nEquipped weapons: {equipped_weapons}")
print(f"Shield equipped: {equipped_shield}")

armour_class = calculate_armour_class(equipped_armour, equipped_shield, character_modifiers["dexterity"], character_class, character_modifiers["constitution"])

armour_class = apply_defense_fighting_style(armour_class, chosen_fighting_styles, equipped_armour)

print(f"Armour class: {armour_class}")

for equipped_weapon in equipped_weapons:
    weapon_name = equipped_weapon["weapon"]
    attack_bonus = calculate_weapon_attack_bonus(weapon_name, character_modifiers["strength"], character_modifiers["dexterity"], proficiency_bonus, known_weapon_proficiencies)

    attack_bonus = apply_archery_fighting_style(attack_bonus, chosen_fighting_styles, weapon_name)

    print(f"{weapon_name} attack bonus: {attack_bonus:+d}")

for index, equipped_weapon in enumerate(equipped_weapons):
    weapon_name = equipped_weapon["weapon"]
    hands = equipped_weapon["hands"]
    wielded_two_handed = hands == 2
    wielding_another_weapon = len(equipped_weapons) > 1

    off_hand = len(equipped_weapons) == 2 and index == 1

    damage_dice, damage_modifier, damage_type = calculate_weapon_damage(weapon_name, hands, character_modifiers["strength"], character_modifiers["dexterity"], off_hand, chosen_fighting_styles=chosen_fighting_styles)

    if damage_dice is None:
        print(f"{weapon_name} damage: No Damage")
        continue

    sneak_attack_damage = calculate_sneak_attack(character_class,character_level)
    if character_class == "Rogue":
        print(f"Sneak Attack: {sneak_attack_damage} damage")

    damage_modifier = apply_dueling_fighting_style(damage_modifier, chosen_fighting_styles, weapon_name, wielded_two_handed, wielding_another_weapon)

    if damage_modifier > 0:
        damage_display = f"{damage_dice} + {damage_modifier}"
    elif damage_modifier < 0:
        damage_display = f"{damage_dice} - {abs(damage_modifier)}"
    else:
        damage_display = damage_dice

    hand_label = " (Off-hand)" if off_hand else ""

    print(f"{weapon_name}{hand_label} damage: {damage_display} {damage_type}")

    if character_class == "Barbarian":
        rage_bonus = calculate_rage_damage_bonus(character_class, character_level, equipped_armour, weapon_name, character_modifiers["strength"], character_modifiers["dexterity"])

        raging_modifier = damage_modifier + rage_bonus

        if raging_modifier > 0:
            raging_damage_display = f"{damage_dice} + {raging_modifier}"
        elif raging_modifier < 0:
            raging_damage_display = f"{damage_dice} - {abs(raging_modifier)}"
        else:
            raging_damage_display = damage_dice

        print(
            f"{weapon_name}{hand_label} damage while Raging: "
            f"{raging_damage_display} {damage_type}"
        )

print(f"\nAs you're {article} {display_race} your movement speed is {movement_speed}!")

if remarkable_athlete_bonus is not None:
    running_long_jump = character_stats["strength"]
    running_long_jump += character_modifiers["strength"]

    print(f"Remarkable Athlete Running Long Jump distance: {running_long_jump} ft")

if chosen_fighting_styles:
    print("\nFIGHTING STYLES:")

    for style in chosen_fighting_styles:
        print(f"\t{style}")

if champion_critical_range is not None:
    print("\nCHAMPION FEATURES:")
    print(f"Critical Hit range: {champion_critical_range}-20")
















































