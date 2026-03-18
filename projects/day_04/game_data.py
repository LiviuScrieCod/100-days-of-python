outcome = {
    "first_victory": "Glory to the winner! His reign has started!",
    "sustained_victory": "Glory to the winner! His reign continues!",
    "first_defeat": "Some are born to remain peasants...",
    "sustained_defeat": "Aaaaaand the king has fallen! Shaaaaaaaaaaame!",
    "draw": "This is TENSE! But it's also a draw...",
}

confusion = [
    "Wait, is that a thumb?!",
    "Overflowing dam...?!",
    "A foot? Really?",
    "Is that... a gang sign?!",
    "Stop touching your opponent!",
    "That's not a move, that's a seizure!",
    "Instructions were clear, yet here we are...",
    "Don't you dare undress on the stage!"
]

valid_moves = ["rock", "paper", "scissors"]

random_opponents = [
    ["Vasile 'The Anvil' Popescu", "The Hammer"],
    ["Iron Mike from Detroit", "Metal Scaper"],
    ["Sergei the Stoic", "The Chaos Engine"],
    ["Gelu 'Deget-de-Otel'", "Knuckles"],
    ["The 1977 Champion (Retired)", "401k"],
    ["A Very Self-Aware Fridge", "The Defroster"],
    ["Cornel from Accounting", "The Tax Avoider"],
    ["The Ghost of Rock-Paper-Past", "The exorcist"],
    ["Ivan 'The Thumb' Drago", "NKVGG!"],
    ["Smaranda the Swift", "Speed Limit"],
    ["Tibi 'The Human Calculator'", "Carry the one"],
    ["An Actual Bag of Rocks", "Heavy lifter"],
    ["Chuck 'The Fist' Norris", "Cancel Culture"],
    ["Zinaida the Relentless", "Take a seat"],
    ["The Janitor (Who Saw Everything)", "Eye gouger"]
]

# --------------------------------------------------------------------- #
# Tournament related data

group_standings = [
    [6,4,2,0],
    [5,4,3,0],
    [4,4,3,1],
    [5,3,3,1],
    [5,3,2,2],
    [5,5,2,0],
]

# --------------------------------------------------------------------- #
# Hunter related data

achievements_metadata = {
    "specialist": {
        "title": "The Specialist",
        "description": "win {%} rounds, using {^}",
    },
    "survivor": {
        "title": "The Survivor",
        "description": "don't lose for {%} consecutive rounds"
    },
    "over_9000": {
        "title": "Over 9000!",
        "description": "win using one special move"
    },
    "mirror": {
        "title": "Mirror",
        "description": "win a round using the prey's previous choice"
    },
    "balancer": {
        "title": "Balancer",
        "description": "during the next {&} hands get 2 draws"
    }
}