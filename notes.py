"""
Objectif :
Écrire un programme Python qui :
1.demander combien de notes seront saisies ;
2.pour chaque élève, demander le prénom (sans validation particulière) puis la note
3. enregistrer chaque élève sur une ligne dans un fichier texte au format :
Prénom <note>/20 (ex.Alice 10.0/20)
4. calculer la
moyenne de la classe (arrondie à 2 décimales) et ajouter à la fin du fichier :
La moyenne est: <moyenne>/20.

Contraintes et validations :
Exiger que le nombre d’élèves soit un entier strictement positif ; en cas d’entrée invalide, afficher un message d’erreur et redemander la saisie.
Valider la note en :convertissant l’entrée en float avec try/except ; vérifiant qu’elle est comprise entre 0 et 20 inclus
En cas d’entrée invalide (non numérique ou hors [0,20]), afficher un message d’erreur et redemander la saisie.
Accepter le prénom tel quel (toute chaîne non vide).
Format de sortie (fichier)
Choisir un nom de fichier (par ex.notes_classe.txt).
Écrire une ligne par élève au format exact : Prénom <note>/20
Ajouter en dernière ligne :La moyenne est: <moyenne>/20, avec
<moyenne> arrondie à 2 décimales.
"""
def ask_name(student_id):
    return str(input(f"{student_id} : Saisir un prénom : "))

def ask_note(student_id):
    return float(input(f"{student_id} : Saisir une note : "))

open("classe.txt", "w").close()

def save_note(name, note):
    with open("classe.txt", "a") as file:
        file.write(f"{name} {note}/20\n")

def save_moyenne(moyenne):
    with open("classe.txt", "a") as file:
        file.write(f"Moyenne de la classe : {moyenne}/20\n")

ask_quantity = int(input("combien de note(s) voulez vous saisir ? : "))

notes_classe = []

for i in range(ask_quantity):

    note = ask_note(i)
    prenom = ask_name(i)

    if note < 0 or note > 20.0:
        print("erreur, la note doit être strictement positive et inférieure à 20 !")
        note = ask_note(i)
    else:
        print("")
        notes_classe.append(note)

    if prenom.strip() == "":
        print("erreur, le prénom doit être une chaîne de caractère !")
        prenom = ask_name(i)
    else:
        print("")

    print(f"{prenom} a eu {note}/20 !")
    save_note(prenom, note)

moyenne = sum(notes_classe) / len(notes_classe)
print(f"La moyenne est de {moyenne}/20 !")

save_moyenne(moyenne)






