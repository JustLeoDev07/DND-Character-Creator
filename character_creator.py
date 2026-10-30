import random

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

weapon_categories = {
    "Club": "Simple Weapons",
    "Dagger": "Simple Weapons",
    "Dart": "Simple Weapons",
    "Handaxe": "Simple Weapons",
    "Light Crossbow": "Simple Weapons",
    "Light Hammer": "Simple Weapons",
    "Quarterstaff": "Simple Weapons",
    "Shortbow": "Simple Weapons",
    "Sling": "Simple Weapons",
    "Greatclub": "Simple Weapons",
    "Javelin": "Simple Weapons",
    "Mace": "Simple Weapons",
    "Sickle": "Simple Weapons",
    "Spear": "Simple Weapons",

    "Battleaxe": "Martial Weapons",
    "Hand Crossbow": "Martial Weapons",
    "Longbow": "Martial Weapons",
    "Longsword": "Martial Weapons",
    "Rapier": "Martial Weapons",
    "Shortsword": "Martial Weapons",
    "Warhammer": "Martial Weapons",
    "Flail": "Martial Weapons",
    "Glaive": "Martial Weapons",
    "Greatsword": "Martial Weapons",
    "Halberd": "Martial Weapons",
    "Lance": "Martial Weapons",
    "Maul": "Martial Weapons",
    "Morningstar": "Martial Weapons",
    "Pike": "Martial Weapons",
    "Scimitar": "Martial Weapons",
    "Trident": "Martial Weapons",
    "War Pick": "Martial Weapons",
    "Whip": "Martial Weapons",
    "Blowgun": "Martial Weapons",
    "Heavy Crossbow": "Martial Weapons",
    "Net": "Martial Weapons",
    "Greataxe": "Martial Weapons"
}

weapon_attack_types = {
    # Melee Weapons
    "Club": "Melee",
    "Dagger": "Melee",
    "Greatclub": "Melee",
    "Handaxe": "Melee",
    "Javelin": "Melee",
    "Light Hammer": "Melee",
    "Mace": "Melee",
    "Quarterstaff": "Melee",
    "Sickle": "Melee",
    "Spear": "Melee",

    "Battleaxe": "Melee",
    "Flail": "Melee",
    "Glaive": "Melee",
    "Greataxe": "Melee",
    "Greatsword": "Melee",
    "Halberd": "Melee",
    "Lance": "Melee",
    "Longsword": "Melee",
    "Maul": "Melee",
    "Morningstar": "Melee",
    "Pike": "Melee",
    "Rapier": "Melee",
    "Scimitar": "Melee",
    "Shortsword": "Melee",
    "Trident": "Melee",
    "War Pick": "Melee",
    "Warhammer": "Melee",
    "Whip": "Melee",

    # ranged

    "Light Crossbow": "Ranged",
    "Dart": "Ranged",
    "Shortbow": "Ranged",
    "Sling": "Ranged",

    "Blowgun": "Ranged",
    "Hand Crossbow": "Ranged",
    "Heavy Crossbow": "Ranged",
    "Longbow": "Ranged",
    "Net": "Ranged",
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

    for weapon_name, weapon_category in weapon_categories.items():
        if weapon_category == category:
            if attack_type is None or weapon_attack_types[weapon_name] == attack_type:
                available_weapons.append(weapon_name)

    return available_weapons

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

print(f"\nAs you're {article} {display_race} your movement speed is {movement_speed}!")

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

print("\nYour Skill proficiencies and bonuses:")
for skill,bonus in skill_bonuses.items():
    if skill in expertise_skills:
        print(f"- {skill}: {bonus:+} (Expertise)")
    elif skill in known_character_skills:
        print(f"- {skill}: {bonus:+} (Proficient)")
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
    category = weapon_categories.get(weapon)
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






















































