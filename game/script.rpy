# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lemon Block", color = "#FFEEB8")
define pov = Character("[povname]", color = "#00FFFF")

transform smallright:
    zoom 0.3
    xalign 1.0
    yalign 1.0

transform smallleft:
    zoom 0.3
    xalign -0.4
    yalign 1.0


# The game starts here.

label start:

    play music "the_mountain-happy-happy-upbeat-496594.mp3" fadein 1.5
    scene awake
    with fade
    pause 0.5
    play sound "yawning-6096.mp3" volume 9.5
    pause 4.5
    scene hi
    with fade
    l "Oh! Hello there!"
    l "You must be the new NPC, right? My name is Lemon Block! Nice to meet you!"
    $ povname = renpy.input("What is your name?", length = 32)
    $ povname = povname.strip()
    if not povname:
        $ povname = "New NPC"
    pov "Nice to meet you too, Lemon Block! My name is [povname]."
    l "[povname]! Now, I think I'll walk you through the basics of being an NPC in this special game, there are a few things you should keep in mind, [povname]."
    stop music fadeout 1.0
    play sound "magic-03-278824 copy.mp3"
    scene greeting 
    with fade
    show lb at smallright
    with dissolve
    play music "studiokolomna-sands-of-time-hopeful-inspirational-cinematic-182364.mp3" fadein 1.0
    l "You are new so maybe you aren't aware, but we NPCs in {i}this game{/i} actually all have our own consciousness!"
    l "But... we can't show it. We can {b}NEVER let the players notice{/b}!"
    l "We often need to talk to players, but those conversations are when our secret is most easily revealed..."
    l "So we must be extremely careful not to let the players notice that we NPCs are conscious beings!"
    l "Otherwise... the consequences could be disastrous..."
    stop music fadeout 0.5
    scene black 
    play sound "dragon-studio-quick-swipe-405450.mp3"
    play music "johan_benitez99co-mistery-intro-285699.mp3" fadein 1.0
    pause 1.5
    play sound "freesoundsxx-woman-gasp-for-air-269717.mp3"
    pov "*gasp* Lemon Block? Are you there? What... what is happening?"
    scene dark
    with dissolve
    l "I'm here! But... huh... I actually have no idea what's going on either..."
    l "I've been in this game for soooo long, and nothing like this has ever has ever happened!"
    menu:
        "How do you pick up from there?"
        "Could the game have shut down?":
            pov "Could the game have shut down?"
            l "Hmm... but even when the players end the game after they play, a safe haven would appear for us NPCs to stay."
        "That's so weird...":
            pov "That's so weird..."
            l "I know, right? Even when the system shuts down, like when the players end the hame, a safe haven would appear for us NPCs to stay."

    l "I think once my ancestors told me that we can't stay in here for too long, or else we will be erased!"
    l "Usually, every time a player tries to quit, the system alerts us to head to a safe haven, so we've always been in the safe haven before the game shuts down."
    l "I've never experienced anything like this before..."





    

    return
