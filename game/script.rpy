# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define TODO = Character(_("TO DO"), color = "#ff3333")

screen main_imagemap:
    imagemap:
        auto "images/worldmap_%s.png"

        hotspot (736, 274, 41, 50)  action Return("asmara")      alt "Asmara"
        hotspot (605, 642, 93, 71)  action Return("carvera")     alt "Carvera"
        hotspot (480, 272, 51, 42)  action Return("colchus")     alt "Colchus"
        hotspot (577, 235, 84, 65)  action Return("delphi")      alt "Delphi"
        hotspot (802, 314, 84, 70)  action Return("exxtal")      alt "Exxtal"
        hotspot (529, 465, 68, 55)  action Return("folium")      alt "Folium"
        hotspot (1006, 6, 82, 49)   action Return("heimdall")    alt "Heimdall"
        hotspot (632, 17, 126, 36)  action Return("the_maw")        alt "The Maw"
        hotspot (133, 244, 162, 32) action Return("phendrana")      alt "Phendrana"
        hotspot (346, 419, 85, 87)  action Return("shoal")       alt "Shoal"
        hotspot (454, 385, 60, 49)  action Return("sludge_town") alt "Sludge Town"
        hotspot (763, 156, 53, 59)  action Return("sydnia")      alt "Sydnia"
        hotspot (517, 48, 67, 54)   action Return("the_tavern")  alt "The Tavern"
        hotspot (224, 560, 114, 74) action Return("vermillione") alt "Vermillione"


# The game starts here.

label start:

    jump location_choice

label location_choice:
    show black

    # Show an imagemap.
    window hide None
    call screen main_imagemap
    window show None

    # Call screen assignes the chosen result from the imagemap to the
    # _return variable. We can use an if statement to vary what
    # happens based on the user's choice.

    if _return == "asmara":
        jump asmara
    elif _return == "carvera":
        jump carvera
    elif _return == "colchus":
        jump colchus
    elif _return == "delphi":
        jump delphi
    elif _return == "exxtal":
        jump exxtal
    elif _return == "folium":
        jump folium
    elif _return == "heimdall":
        jump heimdall
    elif _return == "the_maw":
        jump the_maw
    elif _return == "phendrana":
        jump phendrana
    elif _return == "shoal":
        jump shoal
    elif _return == "sludge_town":
        jump sludge_town
    elif _return == "sydnia":
        jump sydnia
    elif _return == "the_tavern":
        jump the_tavern
    elif _return == "vermillione":
        jump vermillione

    return

################
#
# Asmara
#
################
label asmara:
    show bg asmara
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# Carvera
#
################
label carvera:
    show bg carvera
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

    

################
#
# Colchus
#
################
label colchus:
    show bg colchus
    with dissolve

    "Although Colchus is one of the smallest city states in diameter, it boasts third largest in population."

    "The dense and bustling city claims face just on the Southern brim of a thick and musty swamp, which is one of the only ways the Northern part of the realm can connect to the North Western territory."

    "The only local product Colchus has to offer foreigners is transportation through the treacherous waters, and exotic foods and voodoo items."

    "However, what Colchus lacks in natural resources it makes up for in international trade."

    "Trappers, wizards, and collectors travel from the entire Northern region to gather, sell, and barter in Colchus."

    jump location_choice


################
#
# Delphi
#
################
label delphi:
    show bg delphi
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    menu:
        "Trade":
            jump delphi_trade
        "Government":
            jump delphi_government
        "Done":
            jump location_choice

label delphi_trade:
    
    TODO "LORE GOES HERE YOU DINGUS"

    jump delphi

label delphi_government:

    TODO "LORE GOES HERE YOU DINGUS"

    jump delphi

################
#
# Exxtal
#
################
label exxtal:
    show bg exxtal
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# Folium
#
################
label folium:
    show bg folium
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# Heimdall
#
################
label heimdall:
    show bg heimdall
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# The Maw
#
################
label the_maw:
    show bg the_maw
    with dissolve

    "Some call The Maw a horrible pit that descends down into hell itself, while others explain the phenomenon as just an extraordinary sink hole."

    "The lore of the land tells a tale about the demon-god Vaxxak and Ter’Ral being engaged in a decade long conflict."

    "This conflict raged so long and so brutal that it began to tear civilization apart as they began to side with one of the two gods."

    "Xemex foresaw civilization's end from the void of space above, and joined in power with the other deities to send a star crashing down onto the two beings as they locked in a physical bout."

    "The result sent the two dissipating into the air as star dust. The deities reanimated themselves over several centuries, and the star left behind the enormous pit known as The Maw."

    jump location_choice



################
#
# Phendrana
#
################
label phendrana:
    show bg phendrana
    with dissolve

    "Phendrana is the North Western most city state, claiming a profitable and safe area of domain fixed between the Vast Sea and The Shattered Earth."

    "Although the majority of the city is small and lives simple lives, the area is very wealthy."

    "The city remains so successful due to the bountiful fish market that traders take part in at the Phendranan docks, which are the only docks in the Northern sea for hundreds of miles."
    
    "The city remains so safe in such a hazardous area due to the highly defensive and formidable Blood Scale Guard, which resides in a keep on the Northern outskirts of Phendrana."
    
    "Along with the Guard, the king and royal appointees also dwell inside the keep."

    jump location_choice

################
#
# Shoal
#
################
label shoal:
    show bg shoal
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# Sludge Town
#
################
label sludge_town:
    show bg sludge_town
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# Sydnia
#
################
label sydnia:
    show bg sydnia
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# The Tavern
#
################
label the_tavern:
    show bg the_tavern
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

################
#
# Vermillione
#
################
label vermillione:
    show bg vermillione
    with dissolve

    TODO "LORE GOES HERE YOU DINGUS"

    jump location_choice

