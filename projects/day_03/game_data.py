story_texts = {
    "adventure_start": "\nWelcome, brave knight! Are you ready to face the unknown and resque the fair maiden? Glory awaits for a noble soul to step forth! (type start to begin) ",
    "cave_entrance": (
        "The air grows heavy, smelling of damp earth and ancient decay. "
        "The cave mouth swallows the daylight, leaving you with only the sound "
        "of your breath and the echo of water droplets hitting the stone. "
        "You are inside. There is no turning back now."
    ),
    "first_door": (
        "After a few steps into the dense gloom, your boot strikes something metallic. "
        "On the left wall, camouflaged by thick layers of moss and dust, stands an oak door "
        "reinforced with rusted iron bands. It doesn't look like it has been opened in centuries. "
    ),
    "first_chamber": (
        "The hinges groan in protest as you push the door open. Inside, the air is stagnant, "
        "filled with the smell of old parchment and dried herbs. Moonlight filters through "
        "a crack in the ceiling, illuminating a single stone pedestal in the center of the room."
    ),
    "healing_potion_1": (
        "Resting upon the pedestal is a small, ornate glass vial filled with a shimmering "
        "crimson liquid. Even in the dim light, it seems to glow with a faint, reassuring warmth. "
        "You have found a Healing Potion!"
    ),
    "hallway_1": (
        "You step back out into the main tunnel, the heavy door thudding shut behind you. "
        "The silence is broken by a rhythmic, scraping sound coming from deeper within the darkness... "
        "It sounds like something heavy being dragged across the stone floor."
    ),
}

prompts = {
    "first_door": "\nDo you 'enter' the chamber or 'ignore' it? >>>  ",
    "two_tunnels": "\nFollow the sound to the 'left' or continue on the 'right' gallery? >>>  "
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