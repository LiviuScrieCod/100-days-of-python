story_texts = {
    "adventure_start": "\nWelcome, brave knight! Are you ready to face the unknown and resque the fair maiden? Glory awaits for a noble soul to step forth! (type start to begin) ",
    "first_encounter": {
        "cave_entrance": (
            "\nThe air grows heavy, smelling of damp earth and ancient decay. "
            "The cave mouth swallows the daylight, leaving you with only the sound "
            "of your breath and the echo of water droplets hitting the stone. "
            "You are inside. There is no turning back now."
        ),
        "door": (
            "\nAfter a few steps into the dense gloom, your boot strikes something metallic. "
            "On the left wall, camouflaged by thick layers of moss and dust, stands an oak door "
            "reinforced with rusted iron bands. It doesn't look like it has been opened in centuries. "
        ),
        "chamber": (
            "\nThe hinges groan in protest as you push the door open. Inside, the air is stagnant, "
            "smelling of old parchment and dried herbs. Moonlight filters through a crack in the "
            "ceiling, split between two sights: "
            "\n1. In the 'center', a pristine stone pedestal, untouched by time. "
            "\n2. In the far 'corner', a pile of rotted crates and discarded bone-meal lies in the shadows, "
            "where something small and metallic glints amidst the filth."
        ),
        "healing_potion": (
            "\nYou kneel before the pedestal, letting the silence of the chamber wrap around you. "
            "As your whispered prayer ends, the air seems to hum in response. A sudden, "
            "brilliant spark ignites within a small, ornate glass vial that was hidden in the "
            "shadows of the stone. It is filled with a shimmering crimson liquid that glows with "
            "a faint, reassuring warmth. Your faith has been rewarded with a Healing Potion!"
        ),
        "rat_bite": (
            "\nGreed or curiosity drives your hand into the pile of rot. For a split second, "
            "the metallic glint is within reach, but the shadows breathe first. A massive, "
            "plague-scarred rat lunges with startling speed, its yellowed incisors sinking "
            "deep into your wrist. The bite is foul, tasting of copper and ancient decay. "
            "\nYou recoil, flinging the vermin back into the dark, but the damage is done. "
            "The glint was nothing more than a rusted, worthless nail — a cruel lure for the unwary."
        ),
        "exit_chamber": (
            "\nYou step back out into the main tunnel, the heavy door thudding shut behind you. "
            "The silence is broken by a rhythmic, scraping sound coming from deeper within the darkness... "
            "It sounds like something heavy being dragged across the stone floor."
        ),
        "ignore_door": (
            "\nYou cast a wary glance at the ornate door but decide some secrets "
            "are best left undisturbed. Tightening your grip on your torch, "
            "you march past it, the rhythmic echo of your boots the only sound "
            "in the deepening silence of the corridor."
        )
    },
    "second_encounter": {
        "tunnel_split": (
                "The tunnel widens into a jagged limestone throat. To the 'LEFT', the air is freezing, "
                "and that rhythmic scraping sound has turned into a heavy, wet thud. To the 'RIGHT', "
                "the passage is narrow and reeks of old bone, but it seems to lead upward. "
            ),
        "tunnel_split_left": (
            "You venture left, drawn by the sound. As you step into the darkness, the noise stops. "
            "A cold, oppressive shadow detaches itself from the ceiling above. You look up just "
            "in time to see a mass of obsidian claws descending. Everything goes black. "
            "You've found the source of the noise... and it was hungry."
            "GAME OVER!"
        ),
        "tunnel_split_right": (
            "You scramble to the right, squeezing through the tight passage. Just as you move "
            "out of sight, a blood-curdling shriek echoes behind you, "
            "followed by the sickening sound of stone being shredded. Whatever was lurking "
            "back there has found its dinner. You keep moving, heart hammering against your ribs."
        ),
    },
    "third_encounter": {
        "trap": (
            "As you step forward, a heavy **CLICK** echoes through the narrow tunnel. "
            "The stone slab beneath your boot sinks slightly, and everything goes silent. "
            "You feel a sudden rush of air from the walls. You have a split second to react! "
        ),
        "hesitation": (
            "\nYour heart hammers against your ribs, and for a moment, terror freezes your blood. "
            "The split-second required to choose passes in a blur of panic. Because of your "
            "indecision, you are forced to react purely on instinct!"
        ),
        "trap_success": (
            "Your reflexes save your life! You move with a burst of speed just as a "
            "deadly spray of stone shards whistles through the air where you stood "
            "moments ago. You land hard on the dusty floor, gasping, but untouched. "
            "The trap is spent. You pick yourself up and keep going."
        ),
        "trap_failure": (
            "You stumble for a fraction of a second,"
            "just long enough for the trap to find its mark. "
            "Sharp stone projectiles graze your side, tearing through your armor and "
            "leaving a deep, bloody gash. You lose 30 HP!"
        ),
    },
    "hub_encounter": {
        "hub": (
                "\nAs you walk you end up in a grand, circular hall. The air is stagnant and heavy with the scent of "
                "sulfur. Three paths lie before you, each whispering a different promise of fate."
                "To the 'LEFT', a heavy iron-bound door stands slightly ajar, a faint golden light "
                "flickering through the crack. "
                "To the 'RIGHT', a massive stone door is firmly locked; its surface is etched with "
                "faded runes of warding. "
                "Straight 'AHEAD', an ominous hallway stretches into total darkness, echoing with "
                "a low, guttural vibration that makes your teeth rattle."
            ),
        "left_door": {
            "door": (
                "\nYou push the door open and freeze. In the center of the room, a slumped "
                "figure sits on a rickety wooden chair. It's a Goblin guard, snoring loudly "
                "with his head tilted back. Hanging from his thick leather belt is a heavy "
                "iron key ring. The keys glint in the candlelight, just inches from his hand."
            ),
            "stealth_success": (
                "\nHolding your breath, you reach out with trembling fingers. The iron is cold "
                "and heavy, but you manage to unhook the ring without a sound. The Goblin "
                "scratches his nose in his sleep but doesn't stir. You've got the Skeleton Key!"
            ),
            "stealth_failure": (
                "As you reach for the belt, your armor clinks against the chair. The Goblin's "
                "eyes snap open, bloodshot and wide. He lets out a shrill alarm whistle and "
                "swipes at you with a jagged dagger! You barely dodge, but you have to flee "
                "empty-handed. No keys for you this time!"
            ),
        },
        "ahead": {
            "tunnel": (
                "You make your way through to the central hallway. The temperature drops "
                "instantly. Every instinct tells you to run, but glory lies just a few "
                "more steps ahead, where the shadows seem to be moving on their own. " 
                "There is no turning back now."
            ),
        },
        "right_door": {
            "door_no_key": (
                "\nYou rattle the handle, but the stone door doesn't budge. You'll need a way "
                "to bypass this lock if you want to see what's hidden behind the runes."
            ),
            "door_key": (
                "\nYou press the iron key into the rune-etched stone. " 
                "The blue light fades as the door grinds open, revealing a dusty alcove." 
                "Inside, a shimmering red potion awaits."
            )
        },

    },
    "bbeg":{

    },


    "hub_ahead": (
        "You make your way through to the central hallway. The temperature drops "
        "instantly. Every instinct tells you to run, but glory lies just a few "
        "more steps ahead, where the shadows seem to be moving on their own. " 
        "There is no turning back now."
    ),

    "stealth_failure": (
        "As you reach for the belt, your armor clinks against the chair. The Goblin's "
        "eyes snap open, bloodshot and wide. He lets out a shrill alarm whistle and "
        "swipes at you with a jagged dagger! You barely dodge, but you have to flee "
        "empty-handed. No keys for you this time!"
    ),
    "boss_chamber_desc": (
        "The hallway ends abruptly, spilling you into a cathedral of jagged stone. "
        "At its heart, a pyre of white ash smolders, casting long, dancing shadows that "
        "reach for the ceiling like desperate claws. Bound upon the altar lies the "
        "Princess, her silk dress torn, a silent prayer frozen on her lips."
    ),
    "the_monster_revealed": (
        "Towering over her is a nightmare given flesh—a Bugbear of immense size, "
        "his matted fur stained with the rust of old battles. He raises a jagged "
        "black blade, the steel thirsting for royal blood. The air is thick with "
        "the smell of ozone and impending death."
    ),
    "boss_moment_to_act": (
        "For one heartbeat, the beast pauses to savor the terror in her eyes. "
        "In this sliver of time, the shadows offer you a gift: the element of surprise. "
    ),
    "victory_epilogue": (
        "As the beast falls with a final, guttural roar, the oppressive weight "
        "lifts from the room. You untie the silken bonds, and the Princess looks "
        "at you with eyes that have seen the abyss and returned. You have not "
        "just survived the Dungeon of Doom; you have conquered its heart!"
    ),
    "defeat_epilogue": (
        "The world narrows down to the cold, unforgiving stone of the dungeon floor. "
        "As your strength fades, the last thing you see is the flickering shadows "
        "dancing on the walls, mocking your failed heroism. The Princess's plea "
        "dies out in the distance, swallowed by the encroaching silence. "
        "The Dungeon of Doom has claimed another soul, and your story ends "
        "not with a roar, but with a lingering, lonely echo in the dark."
    )
}

prompts = {
    "first_encounter": {
        "door": "\nDo you 'enter' the chamber or 'ignore' it? >>>  ",
        "explore": "\nWhere do you go, Sir Knight: 'center', 'corner' or 'leave room'? >>> "
    },
    "second_encounter": {
        "two_tunnels": "\nFollow the sound to the 'left' or continue on the 'right' gallery? >>>  ",
    },
    "third_encounter": {
        "trap": "\nDo you 'sprint' forward or 'roll' to the side? >>>",
    },
    "hub_encounter": {
        "hub": "\nDo you go 'left', 'right' or 'ahead'? >>> ",
        "hub_left_door": {
            "sleeping_goblin": "\nDo you try to 'take' the key or 'leave' before the goblin wakes up? >>>  ",
        },
    },

    "final_decision": "\nWill you 'fight' or 'flee'?",
    "invalid_input": "\nInvalid command. Please try again: >>>",
    "continue": "\nPress Enter to continue... ",
    "use_key": "\nYou have the Skeleton Key. Use it to unlock the door? ('yes'/'no') >>> "
}

wounds = {
    "rat": (
        "\nThe puncture marks on your hand throb with a dull, sickening heat.",
        "You feel a bit slower, the poison of the cave stinging your veins."
    ),
    "trap": (
        "\nYou gasp as the arrows find their mark, leaving jagged tears in your armor.",
        "Blood seeps through the fabric, warm and alarmingly persistent."
    ),
    "death": (
        "\nYour strength fails as the world narrow to a cold, dark point. "
        "The echoes of the dungeon fade, leaving only the silence of a "
        "grave that will never be marked. Your journey ends here."
    ),
}

art_assets = {
    "opening_screen_art": r''' ********************************************************************************
*                    /   \              /'\       _                              *
*\_..           /'.,/     \_         .,'   \     / \_                            *
*    \         /            \      _/       \_  /    \     _                     *
*     \__,.   /              \    /           \/.,   _|  _/ \                    *
*          \_/                \  /',.,''\      \_ \_/  \/    \                   *
*                           _  \/   /    ',../',.\    _/      \                  *
*             /           _/m\  \  /    |         \  /.,/'\   _\                 *
*           _/           /MMmm\  \_     |          \/      \_/  \                *
*          /      \     |MMMMmm|   \__   \          \_       \   \_              *
*                  \   /MMMMMMm|      \   \           \       \    \             *
*                   \  |MMMMMMmm\      \___            \_      \_   \            *
*                    \|MMMMMMMMmm|____.'  /\_            \       \   \_          *
*                    /'.,___________...,,'   \            \   \        \         *
*                   /       \          |      \    |__     \   \_       \        *
*                 _/        |           \      \_     \     \    \       \_      *
*                /                               \     \     \_   \        \     *
*                                                 \     \      \   \__      \    *
*                                                  \     \_     \     \      \   *
*                                                   |      \     \     \      \  *
*                                                    \ms          |            \ *
 ********************************************************************************
'''

}