# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define l = Character("Lemon Block")

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
    scene greeting 
    with fade
    show lb at smallright
    with dissolve
    l "You are new so maybe you aren't aware, but we NPCs in {i}this game{/i} actually all have our own consciousness!"
    l "But... we can't show it. We can {b}never let the players notice{/b}!"


    

    return
