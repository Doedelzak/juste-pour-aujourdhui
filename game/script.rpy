# Vous pouvez placer le script de votre jeu dans ce fichier.

# Déclarez sous cette ligne les images, avec l'instruction 'image'
image bg black = "#000000"
image bg grande salle jour = "grande_salle_jour.png"
image bg bureau = "bureau.png"
image bg chambre214 nuit = "chambre214_nuit.png"
image bg appartement melodie = "appartement_melodie.png"
image bg cour clinique jour = "cour_clinique_jour.png"
image bg devant cantine nuit = "devant_cantine_nuit.png"
image bg cantine nuit = "cantine_nuit.png"
image bg bureau jovia jour = "bureau_jovia_jour.png"
image bg fumoir jour = "fumoir_jour.png"
image bg couloir jour = "couloir_jour.png"
image bg chambre214 jour = "chambre214_jour.png"
image bg salle depression jour = "salle_depression_jour.png"
image bg devant cantine jour = "devant_cantine_jour.png"
image bg cantine jour = "cantine_jour.png"
image bg salle jour = "salle_jour.png"
image bg ecole vide = "ecole_vide.png"
image bg stand litterature aa = "stand_litterature_aa.png"
image bg reunion aa = "reunion_aa.png"
image bg fumoir nuit = "fumoir_nuit.png"


image melodie = "melodie.png"
image inconnue = "woman6.png"
image elodie = "woman8.png"
image amanda = "woman5.png"
image chris = "man1.png"
image sarah = "woman7.png"
image mohamed = "man6.png"
image clovis = "man4.png"
image amelie = "woman9.png"
image laurent = "man5.png"
image anne = "woman2.png"
image florine = "woman3.png"
image frederic = "man4.png"
image ludovic = "man2.png"
image julie = "woman5.png"
image edouard = "man7.png"
image zu = "man6.png"
image bachar = "man1.png"
image sophie = "woman5.png"
image sylvie = "woman7.png"
image aurelie = "woman6.png"
image valentine = "woman4.png"
image gentilpsy = "man1.png"
image mechantpsy = "man2.png"
image infirmiere = "woman5.png"
image infirmier = "man7.png"
image drjovia = "woman2.png"
image mrselivo = "man4.png"
image drcaline = "woman4.png"
image drmignonbrenet = "man3.png"
image mmenguyen = "woman9.png"
image danielle = "woman1.png"
image sabrina = "woman7.png"
image corentin = "man7.png"
image jeanne = "woman4.png"


# Déclarez les personnages utilisés dans le jeu.
define melodie = Character('Mélodie', color="#c8ffc8")
define inconnue = Character('Inconnue', color="#c8ffc8")
define elodie = Character('Elodie', color="#c8ffc8")
define amanda = Character('Amanda', color="#c8ffc8")
define chris = Character('Chris', color="#c8ffc8")
define sarah = Character('Sarah', color="#c8ffc8")
define mohamed = Character('Mohamed', color="#c8ffc8")
define clovis = Character('Clovis', color="#c8ffc8")
define amelie = Character('Amélie', color="#c8ffc8")
define laurent = Character('Laurent', color="#c8ffc8")
define anne = Character('Anne', color="#c8ffc8")
define florine = Character('Florine', color="#c8ffc8")
define frederic = Character('Frédéric', color="#c8ffc8")
define ludovic = Character('Ludovic', color="#c8ffc8")
define julie = Character('Julie', color="#c8ffc8")
define edouard = Character('Edouard', color="#c8ffc8")
define zu = Character('Zu', color="#c8ffc8")
define bachar = Character('Bachar', color="#c8ffc8")
define sophie = Character('Sophie', color="#c8ffc8")
define sylvie = Character('Sylvie', color="#c8ffc8")
define aurelie = Character('Aurélie', color="#c8ffc8")
define valentine = Character('Valentine', color="#c8ffc8")
define gentilpsy = Character('Psy gentil', color="#c8ffc8")
define mechantpsy = Character('Psy méchant', color="#c8ffc8")
define infirmiere = Character('Infirmière', color="#c8ffc8")
define infirmier = Character('Infirmier', color="#c8ffc8")
define drjovia = Character('Dr. Jovia', color="#c8ffc8")
define mrselivo = Character('Mr Selivo', color="#c8ffc8")
define drcaline = Character('Dr. Caline', color="#c8ffc8")
define drmignonbrenet = Character('Dr. Mignon-Brenet', color="#c8ffc8")
define mmenguyen = Character('Mme Nguyen', color="#c8ffc8")
define danielle = Character('Danielle', color="#c8ffc8")
define sabrina = Character('Sabrina', color="#c8ffc8")
define toutlemonde = Character('Tout le monde', color="#c8ffc8")
define corentin = Character('Corentin', color="#c8ffc8")


define nvlmelodie = Character('Mélodie', kind=nvl,  what_prefix="{cps=100}", color="#c8ffc8")
define nvlelodie = Character('Elodie', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlamanda = Character('Amanda', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlchris = Character('Chris', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlsarah = Character('Sarah', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlmohamed = Character('Mohamed', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlclovis = Character('Clovis', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlamelie = Character('Amélie', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvllaurent = Character('Laurent', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlanne = Character('Anne', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlflorine = Character('Florine', kind=nvl, what_prefix="{cps=100}",color="#c8ffc8")
define nvlludovic = Character('Ludovic', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvljulie = Character('Julie', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvledouard = Character('Edouard', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlzu = Character('Zu', kind=nvl, what_prefix="{cps=v0}", color="#c8ffc8")
define nvlbachar = Character('Bachar', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlsophie = Character('Sophie', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlsylvie = Character('Sylvie', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlaurelie = Character('Aurélie', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlvalentine = Character('Valentine', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlgentilpsy = Character('Psy gentil', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlmechantpsy = Character('Psy méchant', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlinfirmiere = Character('Infirmière', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlinfirmier = Character('Infirmier', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvldrjovia = Character('Dr. Jovia', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlmrselivo = Character('Mr Selivo', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvldrcaline = Character('Dr. Caline', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvldrmignonbrenet = Character('Dr. Mignon-Brenet', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlmmenguyen = Character('Mme Nguyen', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvldanielle = Character('Sabrina', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")
define nvlcorentin = Character('Corentin', kind=nvl, what_prefix="{cps=100}", color="#c8ffc8")

define melodiechuchote = Character('Mélodie', what_prefix="{size=20}", color="#c8ffc8")
define inconnuechuchote = Character('Inconnue', what_prefix="{size=20}", color="#c8ffc8")
define elodiechuchote = Character('Elodie', what_prefix="{size=20}", color="#c8ffc8")
define amandachuchote = Character('Amanda', what_prefix="{size=20}", color="#c8ffc8")
define chrischuchote = Character('Chris', what_prefix="{size=20}", color="#c8ffc8")
define sarahchuchote = Character('Sarah', what_prefix="{size=20}", color="#c8ffc8")
define mohamedchuchote = Character('Mohamed', what_prefix="{size=20}", color="#c8ffc8")
define clovischuchote = Character('Clovis', what_prefix="{size=20}", color="#c8ffc8")
define ameliechuchote = Character('Aurélie', what_prefix="{size=20}", color="#c8ffc8")
define laurentchuchote = Character('Laurent', what_prefix="{size=20}", color="#c8ffc8")
define annechuchote = Character('Anne', what_prefix="{size=20}", color="#c8ffc8")
define florinechuchote = Character('Florine', what_prefix="{size=20}", color="#c8ffc8")
define ludovicchuchote = Character('Ludovic', what_prefix="{size=20}", color="#c8ffc8")
define juliechuchote = Character('Julie', what_prefix="{size=20}", color="#c8ffc8")
define edouardchuchote = Character('Edouard', what_prefix="{size=20}", color="#c8ffc8")
define zuchuchote = Character('Zu', what_prefix="{size=20}", color="#c8ffc8")
define bacharchuchote = Character('Bachar', what_prefix="{size=20}", color="#c8ffc8")
define sophiechuchote = Character('Sophie', what_prefix="{size=20}", color="#c8ffc8")
define sylviechuchote = Character('Sylvie', what_prefix="{size=20}", color="#c8ffc8")
define ameliechuchote = Character('Amélie', what_prefix="{size=20}", color="#c8ffc8")
define valentinechuchote = Character('Valentine', what_prefix="{size=20}", color="#c8ffc8")
define gentilpsychuchote = Character('Psy gentil', what_prefix="{size=20}", color="#c8ffc8")
define mechantpsycuchote = Character('Psy méchant', what_prefix="{size=20}", color="#c8ffc8")
define infirmierechuchote = Character('Infirmière', what_prefix="{size=20}", color="#c8ffc8")
define infirmierchuchote = Character('Infirmier', what_prefix="{size=20}", color="#c8ffc8")
define drjoviachuchote = Character('Dr. Jovia', what_prefix="{size=20}", color="#c8ffc8")
define mrselivochuchote = Character('Mr Selivo', what_prefix="{size=20}", color="#c8ffc8")
define drcalinechuchote = Character('Dr. Caline', what_prefix="{size=20}", color="#c8ffc8")
define drmignonbrenetchuchote = Character('Dr. Mignon-Brenet', what_prefix="{size=20}", color="#c8ffc8")
define mmenguyenchuchote = Character('Mme Nguyen', what_prefix="{size=20}", color="#c8ffc8")
define daniellechuchote = Character('Danielle', what_prefix="{size=20}", color="#c8ffc8")
define sabrinachuchote = Character('Sabrina', what_prefix="{size=20}", color="#c8ffc8")
define toutlemondechuchote = Character('Tout le monde', what_prefix="{size=20}", color="#c8ffc8")
define corentinchuchote = Character('Corentin', what_prefix="{size=20}", color="#c8ffc8")




# Le jeu commence ici
label start:

stop music
stop sound
stop audio
scene bg black

$ current_day = "14"
$ current_month = "octobre"
$ compteur_abstinence = 120

show screen phone_button

#jump bypassGOTO

python:
    testString = renpy.input("Go to", length=32)
    testString = testString.lower()
    testString = testString.replace(" ", "")

    if not testString:
         testString = "intro"

if testString == "intro":
        jump intro
if testString == "14oct":
        jump oct_14
if testString == "15oct":
        jump oct_15
if testString == "16oct":
        jump oct_16
if testString == "17oct":
        jump oct_17
if testString == "18oct":
        jump oct_18
if testString == "19oct":
        jump oct_19
if testString == "20oct":
        jump oct_20
if testString == "21oct":
        jump oct_21
if testString == "22oct":
        jump oct_22
if testString == "23oct":
        jump oct_23
if testString == "24oct":
        jump oct_24
if testString == "25oct":
        jump oct_25
if testString == "26oct":
        jump oct_26
if testString == "27oct":
        jump oct_27
if testString == "28oct":
        jump oct_28
if testString == "29oct":
        jump oct_29
if testString == "30oct":
        jump oct_30
if testString == "31oct":
        jump oct_31
if testString == "1nov":
        jump nov_01
if testString == "2nov":
        jump nov_02
if testString == "3nov":
        jump nov_03
if testString == "4nov":
        jump nov_04
if testString == "5nov":
        jump nov_05
if testString == "6nov":
        jump nov_06
if testString == "7nov":
        jump nov_07
if testString == "8nov":
        jump nov_08
if testString == "9nov":
        jump nov_09
if testString == "10nov":
        jump nov_10
if testString == "11nov":
        jump nov_11
if testString == "12nov":
        jump nov_12
if testString == "13nov":
        jump nov_13
if testString == "14nov":
        jump nov_14
if testString == "15nov":
        jump nov_15
if testString == "16nov":
        jump nov_16
if testString == "17nov":
        jump nov_17
if testString == "18nov":
        jump nov_18
if testString == "19nov":
        jump nov_19
if testString == "20nov":
        jump nov_20
if testString == "21nov":
        jump nov_21
if testString == "22nov":
        jump nov_22
if testString == "23nov":
        jump nov_23
if testString == "24nov":
        jump nov_24
if testString == "25nov":
        jump nov_25
if testString == "26nov":
        jump nov_26
if testString == "27nov":
        jump nov_27
if testString == "28nov":
        jump nov_28
if testString == "29nov":
        jump nov_29
if testString == "30nov":
        jump nov_30
if testString == "1dec":
        jump dec_01 
if testString == "2dec":
        jump dec_02
if testString == "3dec":
        jump dec_03 
if testString == "4dec":
        jump dec_04
if testString == "5dec":
        jump dec_05
if testString == "6dec":
        jump dec_06 
if testString == "7dec":
        jump dec_07
if testString == "8dec":
        jump dec_08
if testString == "9dec":
        jump dec_09
if testString == "10dec":
        jump dec_10
if testString == "11dec":
        jump dec_11
if testString == "12dec":
        jump dec_12
if testString == "13dec":
        jump dec_13
if testString == "14dec":
        jump dec_14
if testString == "15dec":
        jump dec_15
if testString == "16dec":
        jump dec_16
if testString == "17dec":
        jump dec_17
if testString == "18dec":
        jump dec_18
if testString == "19dec":
        jump dec_19
if testString == "20dec":  
        jump dec_20
if testString == "21dec":
        jump dec_21
if testString == "22dec":
        jump dec_22
if testString == "23dec":
        jump dec_23
if testString == "24dec":
        jump dec_24
if testString == "25dec":
        jump dec_25
if testString == "26dec":
        jump dec_26
if testString == "27dec":
        jump dec_27
if testString == "28dec":
        jump dec_28
if testString == "29dec":
        jump dec_29
if testString == "30dec":
        jump dec_30
if testString == "31dec":
        jump dec_31
if testString == "1jan":
        jump jan_01
if testString == "2jan":
        jump jan_02
if testString == "3jan":
        jump jan_03
if testString == "4jan":
        jump jan_04
if testString == "5jan":
        jump jan_05
if testString == "6jan":
        jump jan_06
if testString == "7jan":
        jump jan_07
if testString == "8jan":
        jump jan_08
if testString == "9jan":
        jump jan_09
if testString == "10jan":
        jump jan_10
if testString == "11jan":
        jump jan_11
if testString == "12jan":
        jump jan_12
if testString == "13jan":
        jump jan_13
if testString == "14jan":
        jump jan_14
if testString == "15jan":
        jump jan_15
if testString == "16jan":
        jump jan_16
if testString == "17jan":  
        jump jan_17
if testString == "18jan":  
        jump jan_18
if testString == "19jan":
        jump jan_19
if testString == "20jan":  
        jump jan_20         
if testString == "21jan":
        jump jan_21
if testString == "22jan":
        jump jan_22
if testString == "23jan":
        jump jan_23
if testString == "24jan":
        jump jan_24
if testString == "25jan":
        jump jan_25
if testString == "26jan":
        jump jan_26
if testString == "27jan":
        jump jan_27
if testString == "28jan":  
        jump jan_28
if testString == "29jan":
        jump jan_29
if testString == "30jan":
        jump jan_30
if testString == "31jan":  
        jump jan_31



label bypassGOTO:

call intro from _intro

return