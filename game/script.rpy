# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lemon Block", color = "#FFEEB8")
define pov = Character("[povname]", color = "#00FFFF")
define p = Character("Player")

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
    l "I've been in this game for soooo long, and nothing like this has ever happened!"
    menu:
        "How do you pick up from there?"
        "Could the game have shut down?":
            pov "Could the game have shut down?"
            l "Hmm... maybe? But even when the players end the game after they play, a safe haven would appear for us NPCs to stay."
        "That's so weird...":
            pov "That's so weird..."
            l "I know, right? Even when the system shuts down, like when the players end the game, a safe haven would appear for us NPCs to stay."

    play sound "unstable.mp3"
    scene color
    with fade
    l "I think once my ancestors told me that we can't stay in here for too long, or else we will be erased!"
    scene door 
    with fade
    l "Usually, every time a player tries to quit, the system alerts us to head to a safe haven, a door would appear, so we've always been in the safe haven before the game shuts down."
    scene dark 
    with fade
    l "I've never experienced anything like this before..."
    l "What we can do is to look around and see if we can find a way out of here."
    pov "Wait! What's that over there?"
    scene line
    with fade
    play music "freesound_community-echo-55417.mp3"
    l "Oh! The computer screen is still on!"
    l "This means the players haven't exited the game!"
    l "It seems like... well, the wifi might be disconnected..." 
    l "Quick, we have to go to the lit-up spot! We can't stay in the dark!"
    l "Tell everyone to go there! We can wait till the wifi reconnects!"
    scene come 
    with fade   
    play music "jobisahealer-run-487747.mp3" fadein 0.5
    l "Everyone, quick, come with me!"
    scene black 
    with fade
    play sound "km007-chase-running-9109.mp3" volume 3.5
    pause 3.5
    scene more
    with fade
    show lb at smallright
    with moveinright
    l "Phew... at least everyone's safe for now..."
    scene moment
    with fade
    stop music fadeout 0.6
    play sound "later.mp3"
    pause 4.5
    play music "cartoon-funny-462261.mp3" fadein 1.0
    scene cc
    with fade
    show player notice at smallright
    with moveinright
    p "Shoot! Why is the wifi connecting so slow? I can't connect to the game!"
    p "Let me try connecting again and see if it works..."
    hide player notice with moveoutright
    pause 2.0
    play sound "ding-402325.mp3" volume 4.0
    show player happy at smallright
    with moveinright
    p "Done!"
    p "Yeah! I'm back online!"
    show player confused at smallright
    with dissolve
    p "Wait... why are my NPCs all gathered together?"
    p "I don't think this is part of the NPCs' game settings..."
    show player happy at smallright
    with dissolve
    p "Well, nevermind... Hehe can't wait to keep playing the game!!!"
    scene more 
    with fade
    show lb at smallright
    with dissolve
    l "Phew... good thing he didn't doubt us..."
    scene cheer
    with fade
    play music "soulfuljamtracks-happy-happy-happy-500010.mp3" fadein 1.0
    play sound "driken5482-applause-cheer-236786.mp3"
    l "Yeah! Wifi is back and we're all still safe!"
    l "What a happy ending to this unexpected experience!"
    l "It was a close one... we need to be more careful in the future..."
    l "Can't let the players notice that we have consciousness."
    l "Anyway, everything's back to normal now, and the wifi has been reconnected, so all good!"
    stop music fadeout 2.5


    

    return
