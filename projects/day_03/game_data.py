# -*- coding: utf-8 -*-

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
                "\nThe tunnel widens into a jagged limestone throat. To the 'LEFT', the air is freezing, "
                "and that rhythmic scraping sound has turned into a heavy, wet thud. To the 'RIGHT', "
                "the passage is narrow and reeks of old bone, but it seems to lead upward. "
            ),
        "tunnel_split_left": (
            "\nYou venture left, drawn by the sound. As you step into the darkness, the noise stops. "
            "A cold, oppressive shadow detaches itself from the ceiling above. You look up just "
            "in time to see a mass of obsidian claws descending. Everything goes black. "
            "You've found the source of the noise... and it was hungry."
            "GAME OVER!"
        ),
        "tunnel_split_right": (
            "\nYou scramble to the right, squeezing through the tight passage. Just as you move "
            "out of sight, a blood-curdling shriek echoes behind you, "
            "followed by the sickening sound of stone being shredded. Whatever was lurking "
            "back there has found its dinner. You keep moving, heart hammering against your ribs."
        ),
    },
    "third_encounter": {
        "trap": (
            "\nAs you step forward, a heavy **CLICK** echoes through the narrow tunnel. "
            "The stone slab beneath your boot sinks slightly, and everything goes silent. "
            "You feel a sudden rush of air from the walls. You have a split second to react! "
        ),
        "hesitation": (
            "\nYour heart hammers against your ribs, and for a moment, terror freezes your blood. "
            "The split-second required to choose passes in a blur of panic. Because of your "
            "indecision, you are forced to react purely on instinct!"
        ),
        "trap_success": (
            "\nYour reflexes save your life! You move with a burst of speed just as a "
            "deadly spray of stone shards whistles through the air where you stood "
            "moments ago. You land hard on the dusty floor, gasping, but untouched. "
            "The trap is spent. You pick yourself up and keep going."
        ),
        "trap_failure": (
            "\nYou stumble for a fraction of a second,"
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
                "\nAs you reach for the belt, your armor clinks against the chair. The Goblin's "
                "eyes snap open, bloodshot and wide. He lets out a shrill alarm whistle and "
                "swipes at you with a jagged dagger! You barely dodge, but you have to flee "
                "empty-handed. No keys for you this time!"
            ),
        },
        "ahead": {
            "tunnel": (
                "\nYou make your way through to the central hallway. The temperature drops "
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
        "visited": {
            "goblin": (
                "\nThe goblin's rhythmic snoring echoes through the room." 
                "There’s no point in lingering here and risking an unnecessary wake-up call;" 
                "you've already pushed your luck far enough."
            ),
            "potion": (
                "\nThe stone door stands wide open, exposing the empty alcove." 
                "You've already taken the only thing of value; only dust and fading magic remain."
            )
        }
    },
    "bbeg":{
        "boss_chamber": (
            "\nThe hallway ends abruptly, spilling you into a cathedral of jagged stone. "
            "At its heart, a pyre of white ash smolders, casting long, dancing shadows that "
            "reach for the ceiling like desperate claws. Bound upon the altar lies the "
            "Princess, her silk dress torn, a silent prayer frozen on her lips."
        ),
        "monster_desc": (
            "\nTowering over her is a nightmare given flesh — a Bugbear of immense size, "
            "his matted fur stained with the rust of old battles. He raises a jagged "
            "black blade, the steel thirsting for royal blood. The air is thick with "
            "the smell of ozone and impending death."
        ),
        "cta": (
            "\nFor one heartbeat, the beast pauses to savor the terror in her eyes. "
            "In this sliver of time, the shadows offer you a gift: the element of surprise. "
        ),
        "hero_hit": "\nCLANG! Your longsword finds a gap in the beast's armor. The Bugbear roars in pain!",
        "hero_miss": "\nSWISH! The Bugbear is surprisingly fast for its size. Your blade is far from it's target.",
        "bbeg_action": "\nThe Bugbear's muscles ripple as it prepares its counter-attack...",
        "bbeg_special": "\nThe Bugbear enters a bloodthirsty frenzy, unleashing a devastating attack!",
        "bbeg_hit": "\nCRUNCH! The massive blow connects. You feel your ribs groan under the impact!",
        "bbeg_miss": "\nWHIFF! The beast swings its heavy club, but you roll just in time. The floor cracks where you stood.",
        "bbeg_death": "\nThe Iron-Clad Bugbear stumbles, its massive eyes glazed over. With one final, gurgling breath, the mountain of fur collapses. You have triumphed!",
    },
    "epilogue": {
        "victory": (
            "\nAs the beast falls with a final, guttural roar, the oppressive weight "
            "lifts from the room. You untie the silken bonds, and the Princess looks "
            "at you with eyes that have seen the abyss and returned. You have not "
            "just survived the Dungeon of Doom; you have conquered its heart!"
            "\nYou return to the castle where glory awaits you!"
        ),
        "defeat": (
            "\nThe world narrows down to the cold, unforgiving stone of the dungeon floor. "
            "As your strength fades, the last thing you see is the flickering shadows "
            "dancing on the walls, mocking your failed heroism. The Princess's plea "
            "dies out in the distance, swallowed by the encroaching silence. "
            "The Dungeon of Doom has claimed another soul, and your story ends "
            "not with a roar, but with a lingering, lonely echo in the dark."
        ),
        "flee": (
            "\nThe sheer scale of the horror before you freezes the marrow in your bones." 
            "Overwhelmed by a primal, gut-wrenching terror, you turn and bolt back into the shadows like a frightened animal." 
            "You might have saved your skin today, but the stench of your cowardice will follow you longer than any monster ever could." 
            "Eternal shame is now your only companion..."
        )
    }
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
        "trap": "\nDo you 'sprint' forward or 'roll' to the side? >>> ",
    },
    "hub_encounter": {
        "hub": "\nDo you go 'left', 'right' or 'ahead'? >>> ",
        "hub_left_door": {
            "sleeping_goblin": "\nDo you try to 'take' the key or 'leave' before the goblin wakes up? >>>  ",
        },
    },
    "bbeg": {
        "final_decision": "\nWill you 'fight' or 'flee'? >>> ",
        "hero_action": (
            "\nWhat will it be, Sir Knight? "
            "[A]ttack, [h]eal or [i]nventory status? >>> "
        ),
    }
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
''',
    "first_encounter": {
        "old_door": r'''
      ______
   ,-' ;  ! `-.
  / :  !  :  . \
 |_ ;   __:  ;  |
 )| .  :)(.  !  |
 |"    (##)  _  |
 |  :  ;`'  (_) (
 |  :  :  .     |
 )_ !  ,  ;  ;  |
 || .  .  :  :  |
 |" .  |  :  .  |
 |mt-2_;----.___|''',
        "altar": r''' _____
|_/_\_|
 || ||
 || ||
 ||=||
 || ||
''',
        "junk": r'''⠀⠀⠀⠀⠏⠀⠀⠈⠀⠀⠂⠐⠒⢤⠀⠀⠀⠀
⠀⠀⠀⡠⠥⠀⠤⠐⠂⠔⠉⠉⠹⣈⡁⠉⠙⠄
⠀⡤⠮⠤⠤⠷⢠⠤⡸⠅⠀⠼⢹⡁⡅⢀⠅⠀
⠁⡇⠀⠀⠀⠀⢷⢧⠃⠀⠁⠀⠑⠿⡿⣀⡆⠀
⠀⠈⡆⠀⠀⠀⠋⠀⠡⠁⠇⡾⠀⠀⢘⠀⠀⠀
⠀⠀⡎⠀⠀⠀⠀⠀⠘⢤⣇⡆⠀⡄⠌⠀⠀⠀
⠀⠀⠉⠒⠀⠂⠂⠐⠈⠀⠑⠒⠋⠉⠀⠀⠀⠀'''
    },
    "second_encounter": {
        "tunnel_split": r'''                   __________________                             __________________               
                 _/                  \_ _..___`___..__`___`_.._ _/                  \_     
              __/                      \_                      _/                     \__  
             /                           \   `:	          ,   /                          \
            |                             |    `;       ;    |                            |
            |                              \         :      /                             |
            /                               |        ;     |                              \
           |                                |    ;         |                               |
           |                                |    ;      ;  |                               |
          /                                 |           ;  |                                \ 
         |                                  |   ;          |                                 |
        \\\\\,,,\\,//////,\,,\\\///,\,,\\\/.-------.----..--\\\\\,,,\\,//////,\,,\\\///,\,,\\\///
                       --               ----~-__ ---        _--------            ___
            -~-           ___                 ---~-       --~-~ -        --~-             -~-
                                                   -----'''
    },
    "third_encounter": {
        "surprise": r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣤⣴⣶⣶⡒⠤⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠳⠶⣶⡶⠶⣒⣀⣭⣤⣽⣼⠟⣻⠟⠉⠐⠒⠠⠀⠰⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠺⢿⣿⣿⠃⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣶⣿⡿⠟⣿⣿⡟⡁⠐⠁⣠⣶⣿⣿⣿⣶⣤⣬⠁⢠⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⣿⡷⠀⣤
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣴⣾⣿⡿⢛⡥⠒⣩⣴⡞⠐⠀⣠⣿⣿⣿⠿⣿⣿⣿⣿⣿⡇⡆⣎⢳⡜⢿⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣺⣿⣿⡿⠋⠐⠋⣠⣾⣿⣿⠃⠀⣼⣿⣿⠟⣡⣶⣿⣿⣿⣿⡿⢰⠇⣿⣆⢧⠈⠻⣷⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⣾⣿⣿⠏⢄⠀⢀⠘⣿⡿⠋⠀⠀⢠⣿⡿⣡⣾⡿⠻⡿⠿⣿⡿⣡⢏⡀⢻⣿⠸⡆⢀⠘⣿⣇⠠⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⠾⣋⡜⡙⠋⠃⢊⠂⠀⢢⣦⡈⢀⠄⣴⢰⢸⠟⡴⠁⠉⠂⢀⠀⡴⠋⠔⢡⣿⠁⠈⣿⡇⣇⢸⣧⠘⡿⣷⠙⢷⣦⣄⣀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠉⠡⠊⠀⠐⣰⡌⠀⠄⠀⠠⢣⣘⣵⣿⣾⣿⡘⠈⡼⠁⡜⠘⢠⠿⠊⣀⢀⣾⣽⣿⢰⣇⢹⡇⡏⢸⣿⣧⢠⠠⠈⡄⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠂⣄⠆⢰⣿⡇⡘⠘⣸⣴⣿⡿⣻⣿⢏⣼⠇⠘⢿⣾⣥⣶⣤⣴⡾⢣⣿⡿⣽⡿⠈⢿⣿⡇⣧⢸⣿⣿⡎⡇⡀⡿⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣴⠞⠀⣸⣿⢃⣿⣿⠀⠃⠃⣿⣿⠏⣰⡿⢡⣾⠏⣰⠀⢸⣿⢿⣿⣿⡟⣡⡟⣽⡇⣿⠇⠈⠌⢿⡇⡏⣼⣿⣿⡇⢿⣷⠀⣷⢸⣿⣿⣿⣿⣿⣿⣿⣿
⣤⣤⣤⣤⣤⣤⣤⣴⡆⣼⢋⣶⢆⣿⡏⣸⣿⣿⠤⡄⢸⡿⠃⢰⡟⢡⣿⠏⠀⠃⣾⣦⢁⣾⣿⢏⣼⠟⣼⣿⢇⡿⢘⢃⠸⡌⠘⣰⣿⣿⣿⣿⢸⣿⣧⢹⡇⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⢱⢃⣾⣿⢸⣿⠃⣿⣿⡟⠀⡇⠸⢁⢠⠏⢀⣿⡏⠀⠀⣸⣿⠃⣼⡿⢫⡾⢋⣾⣿⡟⢸⢃⣿⣆⢣⠁⢰⢸⣿⣿⣿⣿⡘⡏⣿⡌⣿⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⠈⣼⣿⡇⣿⣿⢸⣿⣿⠃⣆⠅⢀⠃⠂⠀⢸⡟⣠⠇⢀⣿⢃⠠⢟⡵⠋⣰⢻⣿⠟⠀⠈⠘⣛⣛⡂⠀⣆⠸⣿⣿⣿⣿⣿⣇⢸⡇⢹⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡄⢿⣿⡇⢻⣿⢸⣿⣿⢸⠟⠀⠀⡀⢠⠄⡉⠐⠡⠀⣸⠟⠠⢐⢩⠖⡰⡡⠟⢉⠀⠀⣰⣿⣿⣿⣿⡄⢸⠀⣿⣿⡿⣿⣿⣿⠀⠇⡎⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣘⣿⡇⣼⣿⣿⣿⣯⢸⣶⣿⠀⣠⢋⠸⠁⣴⣷⠀⣤⠀⠂⡇⣎⠈⡴⠂⠀⠃⠀⠴⢿⣿⣿⣿⣿⣷⠈⢀⣿⣿⡇⣿⣿⣿⢸⠀⡇⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⣰⣿⠃⣿⢻⣿⠈⢹⡟⠰⠁⢋⢀⣀⣉⠙⠀⡿⠀⢸⠀⡡⠊⣀⡴⠁⠠⠶⠒⠒⠒⠒⠬⢿⣿⡆⢸⡏⣿⡇⢸⣿⣿⢸⢸⡇⢸⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣱⡿⠃⢰⡟⢸⣿⠀⢸⠃⠁⢁⡄⠀⠀⣬⡁⠀⡇⠀⠸⢀⣤⡾⠋⣠⣦⢠⣶⠏⠀⠈⣿⣤⡀⠉⠃⢺⢁⢻⡇⠈⣿⣿⠀⣾⠇⣼⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠟⣫⠞⢋⣠⡤⣸⠁⣼⣿⡀⠀⠀⢶⣿⣏⠀⠀⣼⣿⣷⠀⠀⠐⠘⣁⣴⣾⣿⠿⡘⢿⣦⣐⣠⣿⡿⢏⡴⣰⠏⢸⡘⣷⢈⠘⣿⡀⣏⣰⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣷⣶⣶⣶⣾⣿⣿⢣⠏⡀⣿⢸⣷⠀⢠⠸⣻⠟⣛⠛⢉⠊⣉⡄⢠⣦⠘⣿⣿⣿⣿⣧⣄⡀⢔⣨⣭⣥⣶⡿⢡⢋⡆⡘⢧⠹⡌⡁⡘⣧⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⠎⠀⡇⡟⠀⢿⡆⢀⠀⢻⣿⣿⣿⣿⣿⣿⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁⣡⣿⠡⠃⠈⢆⠃⠃⢻⣌⠂⢻⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣡⣶⡗⠀⠠⠁⡼⡜⣿⡌⢷⣄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣴⣿⣿⠃⢠⡞⡀⡈⢧⡀⠀⠙⢷⣄⡻⢿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⣤⢁⢣⠈⠻⣌⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣥⣶⡟⠘⢁⣋⢀⣙⠦⠙⣶⣦⣭⣤⣽⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡂⠆⢿⣆⠢⡀⢷⣌⡳⢝⠻⣿⣿⣿⣿⠿⠟⣛⣛⣭⣭⣭⣙⡻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠡⠒⠄⢡⣿⣿⣿⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⠘⣿⣷⡄⠘⣿⣿⣷⣶⣬⣿⡅⢐⠋⠉⠉⠉⠀⠀⠉⠉⠉⠀⢹⣿⣿⣿⡏⠙⣿⣿⠃⡌⠀⢶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣾⣿⣿⠀⠹⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣿⣿⣿⣿⣿⠏⠀⠁⠸⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠂⠂⠹⣿⣿⣿⣿⣿⠀⠀⠤⠀⠤⠤⠤⢀⣀⠠⢄⠀⢸⣿⣿⣿⣿⠏⠀⠀⠀⣶⣄⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⢦⠘⢿⣿⣿⣿⠀⠴⣛⣛⣫⣭⣭⣭⣭⣝⡂⢀⢸⣿⣿⠟⠁⠀⠀⠀⣆⠈⠭⢛⣛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠟⠁⠀⠀⠀⠀⢀⡙⠿⣿⣬⣭⣵⣶⠶⠶⠶⢶⣾⣭⣍⣂⡼⢛⣡⡆⠀⠀⠀⠀⠘⢆⠻⣷⣶⣬⣥⣒⠭⣝⠻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣫⢁⣤⣶⣾⣥⣤⣤⣴⣾⣿⡇⠀⠈⠛⢿⣿⣿⣿⣶⣾⣿⣿⡿⠟⣉⣴⣿⣿⠀⠀⠀⢦⣄⣹⣶⣶⣬⣿⣿⣿⣿⣿⣦⡝⢎⠛⢿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⣡⠀⢡⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⢀⠀⠀⢸⣶⣍⠛⠿⣿⠿⠛⢉⣤⣾⣿⣿⣿⣿⠀⢀⣂⠈⠿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢸⢸⣷⡙⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡿⢣⣾⣿⣗⠈⢿⣿⣿⣿⣿⣿⠟⠋⠉⠀⠉⠀⠀⠘⣿⣿⣷⣦⣀⣠⣶⣿⣿⣿⣿⣿⣿⣿⠀⠸⠿⠿⠿⠷⠶⢦⣍⠻⣿⣿⣿⣿⡿⡡⢡⣿⣿⣿⡼⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡿⢡⣿⣿⣿⣿⣎⢎⠻⣿⠿⠋⠀⠀⢀⡤⠖⠒⠒⠦⠆⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠛⣩⡌⠀⠐⠒⠉⠉⠉⠙⢀⡈⠀⠘⣿⡿⢛⠔⣱⣿⣿⣿⣿⡇⣿⣿
⣿⣿⣿⣿⣿⣿⣿⢃⣿⣿⣿⣿⣿⣿⣎⠳⡁⠀⠀⢀⣤⠈⠀⠀⠀⠀⢀⠀⣦⠹⣿⣿⣿⣿⣿⣿⣿⠟⠁⣾⣿⣿⣄⣀⠀⠀⠀⠀⣰⣿⣿⣦⠀⣨⠖⣡⣾⣿⣿⣿⣿⣿⡇⣿⣿
⣿⣿⣿⣿⣿⣿⡿⠌⠿⣿⣿⣿⣿⣿⣿⣷⣝⠦⡰⢿⣿⡄⠀⡀⣤⠾⢋⣾⣿⣇⢙⣛⠿⠿⣛⣫⣴⡿⣰⣿⣿⣿⣿⣿⠷⠈⢀⣐⣛⡋⢉⠠⢚⣵⣿⣿⣿⣿⣿⣿⣿⡿⣰⣿⢿'''
    },
    "hub_encounter": {
        "cave_hub": r'''@@@%@@@@@@@@@@@@@%@%%@%%%@@%@@###@@@@@@
@%@@@@@%@%@@@@%@@##*@@%%*+*%@@**####@@@
+#@%%@%@@@%@%%@%@@**#@@***+*@@%=%%#@@@@
#****%%%@@@*=*@@#%++*=@:=+++%*+=-%*%%@@
=:#:=##*%%#+-*%@#:.=+.@:+++*-===+#+##%%
=#%*+%%#%%#%=*+:-::***:-:==++==-#++++@@
*+*+++##+++*+:=-::.:=::=:-:=+--::--=%@@
*%+++=##+:::::-:::::::-=+:::::=::--#%@@
*+=+#+%#*+:::::::::-::--=:-:::-:::-=++%
**++*#+#::::::::::::-::==:+:::+:::::-+%
**++#***=:::::+:::..:::::=*::+=:::-=+++
***##***++:::::::::::-:==++=*#+#***##%%
#*#*######**==*+++++++***+=--+++==+=*@@
######****+++=+*:+==::::::::......:::@@
####**++=======-:::::-.....:..::::::-##
''',
        "door_left": r'''⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⢀⣀⡠⠤⠴⠚⣿⠃
⠀⠸⣿⡭⣭⣿⣽⣿⣿⣿⣿⣿⣿⣿⣽⣿⡿⠓⠚⠉⣉⣀⣤⡤⣴⠀⣿⠀
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢰⠞⢩⠀⢻⡏⠀⡏⠀⣿⠄
⠀⢠⣟⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⠃⠀⣿⠂
⠀⢘⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⡇⠀⣿⡇
⠀⠈⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⣷⠀⣿⡇
⠀⣠⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⣿⣼⣿⡇
⠀⡃⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠘⠛⠛⠒⠛⠓⠛⠛⣿⣿⡇
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢰⠦⢠⠀⢤⣤⣤⣄⠋⣿⡇
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠈⣿⠀⣿⡇
⠀⢸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⠀⢸⠀⢸⡇⠀⣿⠀⣿⡇
⠀⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢸⣄⢸⠠⣼⡇⠀⣿⠀⣿⡇
⠀⣸⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠉⠉⠀⠛⠚⠯⠿⠀⣿⡇
⠠⢿⣿⣷⣶⣶⣶⠶⢶⡶⢶⣶⣶⣶⣶⢿⣶⣤⣄⣀⣀⠀⠀⠀⢨⠀⣿⡇
⠀⠀⠀⠈⠀⠐⠒⠒⠀⠀⠀⠘⠁⠈⠀⠀⠀⠀⠉⠉⢛⠉⠑⠒⠠⠤⢿⠇'''
    },
    "bbeg": {
        "bbeg": r'''                                            
   %#+@#%                                   
    %**%@%                                  
   %##%@@%%                                 
  **%%##%@ =                                
   #-#@#%%%                                 
   .@#%@@       :     +                     
    %#%@   - =#@+**+#                       
    %+%     %@:+%#-@#%+-=.                  
    +*%    %:#+@@%*++=+==-++.               
    +*      #%%%@#+-=*---*=***              
   *#@   %  =*@%@##+------*%##+             
   %%% % .%#%@#@%#**+--++##@%##% :          
  *--:* -@*#%%#@@+@@#%%%@@@%#***#+%#        
 #+-#%# *@#*%%@#==++-=-=**% ####*=*%*       
 %+*%%* #@##%@%%%++*@%#*#@@@  %%*%*#%@:     
  @#@@@*%***#@@@#*%+%#%#%%@@  +%@#%=:%@#    
  @%@@@@%#+###  @@@@#%*@@%@%%   +%#%%#%@*   
 %%@@@@%#*%#%%   @@@%#%%@@%%%*   :%%@@*#@# *
%##@ **#%%##%    %##@%@%%==*%%%     %#%##@  
 *%%   .%#%%%#:  %%*==%##+%==%@@*   --#%#@# 
         : %*.   @%@**%**###===+%%# %%%+%%@ 
                @@@%*%%#%%#%=*=+*+-   *%#:  
                 #%%#%%%%%*#%**=-=*         
                #%%#**%%#@#####*=+**        
                #%%#=*#% #+   %%#+##**      
                 %%#=**#      *#%%##**      
               +%%%%##%+      +**#***#      
              #%##%##%#         **##*#      
              ##%#%%%+           #*###      
              *%##%%             #*#*#      
             %##%##              #*==+:     
           :#%##%##              #=+==++    
          +#%#%%##%-            =#+-=+*#-   
                                *=*%*#*:    '''
    },
    "fight": {
        "hero_attacks": r'''      _,.
    ,` -.)
   ( _/-\\-._
  /,|`--._,-^|            ,
  \_| |`-._/||          ,'|
    |  `-, / |         /  /
    |     || |        /  /
     `r-._||/   __   /  /
 __,-<_     )`-/  `./  /
'  \   `---'   \   /  /
    |           |./  /
    /           //  /
\_/' \         |/  /
 |    |   _,^-'/  /
 |    , ``  (\/  /_
  \,.->._    \X-=/^
  (  /   `-._//^`
   `Y-.____(__}
    |     {__)
          ()
''',
        "hero_dies": r'''                     ______
                  .-"      "-.
                 /            \
                |              |
                |,  .-.  .-.  ,|
                | )(__/  \__)( |
                |/     /\     \|
      (@_       (_     ^^     _)
 _     ) \_______\__|IIIIII|__/__________________________
(_)@8@8{}<________|-\IIIIII/-|___________________________>
       )_/        \          /
      (@           `--------` jgs
''',
        "bbeg_attacks": r'''              ,
          -===>)))o
  /\      .   '| \
  ||     /(__  /~ )
|_/\_|  ,~~  ~~-._|
 \()/  /~   /     \
  ||   >/-/~       |
  ||   " (   .     |
  ||     (=-/      |
 (||\___/' /\_,  __(
 `--...__./  |-\\\\\\
  ||        /~~\||||;
  ||       /   |///|
  ||      /   /\   |
  ||     |__/'  \__\
  ||     ((((   (((((
  ||     )))))   )))))
  ||     (((((   (((((
  ||      | /     | /
  ||  __./' \_ _./' \_ TX
  \/ ////~~~\_)/~~~~\_)
''',
        "bbeg_dead": r'''
             *
          *
        *           ..i'             q.
       *         .poj;                \*.
      .         oKPO                   THk
     .k        {HHk`                    THH,
     dH,       ;YJH.                     YHHk
    {HHk       :lHHk                     jHHH}
     THHk      `NJHH,                   .HHHl'
      THHk,     lHHHHk                 jHHHHP
       THHHi:,  `GHHHHH,.            .'HHHHH
        `THHHHHHi\WHHHHHkoo....ooooojHHHHHHF
          `*THHHH`THHHHHHHHHHHHHHHHHHHHHHHHl
             `*THHHYHHHHHHHHHHHHHHHHHHHHHHHI
                `*THHYHHHHHHHHHHHHHHHHHHHHHH}
                  `*THHHHHHHHHHHHHHHHHHHHHH}
                     `THHHHHHHHHHHHHHHHHHHP
                       `THHHHHHHHHHHHHHHHHH|  Snafu
''',
    },
    "epilogue": {
        "victory": r'''                                o
                            .-'"|
                            |-'"|
                                |   _.-'`.
                               _|-"'_.-'|.`.
                              |:^.-'_.-'`.;.`.
                              |::.'.   ,-'_.-'|
                              |:::+.'-'.-: . J
           __.            .d88|:+:::+-' _-, .|
      _.--'_..`.    .d88888888|:||]:|, | J].J8b.
   +:" ,--'_.|`.`.d88888888888|-' J:| .| J|_|888b.
   |:\ \-'_.--'_.-+888888888+'  _-K:F.+:    `88888bo.
    L:\ +'_.--'. .|88888+"'  _.'.J:J.J:::.    +8888888b.
    |:::+'. ._. . |8+"'  _.-', . |:| |::::+    `+8888888._-'.
  .d8J::L. ./ \\ .J' _.-: . . . ,|:|.|::::::.,   `+888+'^.-|.`.
 d888|::| . F  FL J-'. . , . , . F:F F::::::/`/  _.-"_.-'_.+.`.`.
d88888L::L .|  \L. L. . , . . . J:J J::::::/`/::|. +'_.-'    `_+ `;
888888J::|. K    \.L . , . . _:-+:|.':::::/`/:::F::.`.     .-'_.-:J
8888888|::L.L\    \|. . ._:-'     '   `::/`/:::J:::::.`..-'.-'. . |
8888888PL:| |:\    `._:-'               /`/::::|:|| \::..-'. , . J.b
8888888 |::L L:`.    \     _.-+.       /`/`::::L+`'  |::| . . , .F88b
8888888  L:|.|:::\   _:.--'_.-|.`.    '`/   >-'     .J:J . , . .|8888b
8888888  |::L.L:::+:" _.--'_.-'.`.`.    _.-'    :"|':|:|. . . .JY88888b
8888888   L:| |::::|\ \_.-'     `.`.`.-'    :"|-'. .J:J. . , . F Y88888b
Y888888    \:L L:::L:\ `.      _.-'_.-+ :"|-: . , . |:| , . , |  Y88888b
`888888b    \|.|:::|:::. \ _.-'_.-: . |-', . . , . J:J . . . J    Y88888b
 Y888888     +'\:::J::::\ '_.-'. . . .F . .,-T`\. .|:|. , ,-'     )888888
  Y88888b.      \:::L::::+. . , . . .J . ,/  |:J .J:J. ,-'       .d888888
   Y888888b      \::|::::| . . . , . |. . F  ':|,-'+|-'        .d88888888
    Y888888b      \:J::::|. . . . . .F , J    -:             .od88888888P
     Y888888b      \:L:::| . , . , .J . .| .' ` \d8888888888888888888888P
      Y888888b      \|:::|. , . . , |. ,-'`.  `\ `+88888888888888888888P
       Y888888b.     J:::| . . , . .F-'     \\ ` \ \88888888888888888P'
        Y8888888b     L::|, . . , .J       d8+.`\  \`+8888888888888P'
         Y8888888b    |::| . , . ._+      d8888\  ` .'  `Y888888P'
         `88888888b   J::|. . ._-'     .od888888\.-'
          Y88888888b   \:| ._-'     d888888888P'              ,==. o
          `888888888b   \|-'       d88888888'                 |/ "'/L
           `Y88888888b            d8888888P'                 ,-_) '<_
             Y88888888bo.      .od88888888   hs               /^-._  \=_
             `8888888888888888888888888888                    `   (-'/ ~~
              Y88888888888888888888888888P                    a:f  | \
               `Y8888888888888888888888P'                          `  `
                 `Y8888888888888P'
                      `Y88888P' 
''',
        "defeat": r'''        _
       (_)
       |=|
       |=|
   /|__|_|__|\
  (    ( )    )
   \|\/\"/\/|/
     |  Y  |
     |  |  |
     |  |  |
    _|  |  |
 __/ |  |  |\
/  \ |  |  |  \
   __|  |  |   |
/\/  |  |  |   |\
 <   +\ |  |\ />  \
  >   + \  | LJ    |
        + \|+  \  < \
  (O)      +    |    )
   |             \  /\
 ( | )   (o)      \/  )
_\\|//__( | )______)_/
        \\|//
'''
    },
    "misc": {
        "go": r''' $$$$$$\                                                                                  $$\ 
$$  __$$\                                                                                 $$ |
$$ /  \__| $$$$$$\  $$$$$$\$$$$\   $$$$$$\         $$$$$$\ $$\    $$\  $$$$$$\   $$$$$$\  $$ |
$$ |$$$$\  \____$$\ $$  _$$  _$$\ $$  __$$\       $$  __$$\\$$\  $$  |$$  __$$\ $$  __$$\ $$ |
$$ |\_$$ | $$$$$$$ |$$ / $$ / $$ |$$$$$$$$ |      $$ /  $$ |\$$\$$  / $$$$$$$$ |$$ |  \__|\__|
$$ |  $$ |$$  __$$ |$$ | $$ | $$ |$$   ____|      $$ |  $$ | \$$$  /  $$   ____|$$ |          
\$$$$$$  |\$$$$$$$ |$$ | $$ | $$ |\$$$$$$$\       \$$$$$$  |  \$  /   \$$$$$$$\ $$ |      $$\ 
 \______/  \_______|\__| \__| \__| \_______|       \______/    \_/     \_______|\__|      \__|
                                                                                              
                                                                                              
                                                                                              ''',
        "pathetic": r'''$$$$$$$\   $$$$$$\ $$$$$$$$\ $$\   $$\ $$$$$$$$\ $$$$$$$$\ $$$$$$\  $$$$$$\  $$\ 
$$  __$$\ $$  __$$\\__$$  __|$$ |  $$ |$$  _____|\__$$  __|\_$$  _|$$  __$$\ $$ |
$$ |  $$ |$$ /  $$ |  $$ |   $$ |  $$ |$$ |         $$ |     $$ |  $$ /  \__|$$ |
$$$$$$$  |$$$$$$$$ |  $$ |   $$$$$$$$ |$$$$$\       $$ |     $$ |  $$ |      $$ |
$$  ____/ $$  __$$ |  $$ |   $$  __$$ |$$  __|      $$ |     $$ |  $$ |      \__|
$$ |      $$ |  $$ |  $$ |   $$ |  $$ |$$ |         $$ |     $$ |  $$ |  $$\     
$$ |      $$ |  $$ |  $$ |   $$ |  $$ |$$$$$$$$\    $$ |   $$$$$$\ \$$$$$$  |$$\ 
\__|      \__|  \__|  \__|   \__|  \__|\________|   \__|   \______| \______/ \__|''',
        "final_blow": r'''              .-.
              | |____________________________________________________
 _ _ _ _ _ _ _| |                                                  .'`.
|_|_|_|_|_|_|_| |-mbfh-------------------------------------------.'****>
`.            | |_______________________________________________.'***.'
  `.        .'| |                                               `**'
    `-.___.'  `-'                                              .'*`.
                                                               `._.' .
                                                               .   .'*`.
                                                             .'*`. `._.'
''',
        "caduceus": r''' _____  _  _____
(___  \( )/  ___)
  (___ | | ___)
     /"| ("\
    ( (| |) )
     `.!' .'
      / .'\
      \|/ /
       /.<
      (| |)
       | '
       `-'   VK
'''
    }
}

music = {
    "background_music": '$count=0; while($true){ [console]::beep(60, 100); Start-Sleep -m 100; [console]::beep(55, 250); $count++; if($count -eq 7){ Start-Sleep -m 1000; [console]::beep(110, 1000); [console]::beep(165, 1000); [console]::beep(130, 1000); [console]::beep(146, 1000); $count = 0; } Start-Sleep -m 1000 }',
    "combat_music": 'while($true){for($i=0;$i -lt 7;$i++){[console]::beep(440,143);Start-Sleep -m 30;[console]::beep(494,143);Start-Sleep -m 30;[console]::beep(523,143);Start-Sleep -m 30};[console]::beep(523,143);Start-Sleep -m 30;[console]::beep(494,143);Start-Sleep -m 30;[console]::beep(440,143);Start-Sleep -m 30;[console]::beep(392,143);Start-Sleep -m 30}'
}