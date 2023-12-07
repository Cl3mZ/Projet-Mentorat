###########################
# Librairie(s) utilisée(s)#
###########################
from flask import *
from datetime import datetime
from werkzeug.utils import secure_filename
from bdd import *
###########################


# Création d'un objet application web Flask
app = Flask(__name__)
app.secret_key = b"Phr@s3_5up3R#s3Kr3//"

# Création de l'objet pour accéder à la base de données SQLite du site Mentorat
bdd = Bdd("bdd/BDD_Mentorat")


# Création d'une fonction accueil() associée à l'URL "/"
# Affiche la page acceuil publique sans besoin de connexion.
@app.route("/")
def accueil():
    return render_template("acceuil.html")



########################################################
#Page web Eleve, Info, demande d'aide, devenir mentort.#
########################################################


#Affiche la page accueil privée sur connexion d'un élève
@app.route("/eleve/accueil")
def eleve_accueil():
    return render_template("eleve_accueil.html")


#Affiche la page info 
@app.route("/eleve/infos")
def eleve_infos():
    pass


#Affiche la page aide pour pouvoir demander de l'aide 
@app.route("/eleve/aide")
def eleve_aide():
    pass


#Affiche la page de demande pour devenir mentort
@app.route("/eleve/devenirMentort")
def eleve_devenirMentort():
    pass



#########################################################
#Page web Mentort, Info, demande d'aide, aider un élève.#
#########################################################


#Affiche la page acceuil privée sur connexion d'un élève
@app.route("/mentort/accueil")
def mentort_accueil():
    return render_template("eleve_accueil.html")


#Affiche la page info 
@app.route("/mentort/infos")
def mentort_infos():
    pass


#Affiche la page aide pour pouvoir demander de l'aide 
@app.route("/mentort/aide")
def mentort_aide():
    pass


#Affiche la page de demande pour devenir mentort
@app.route("/mentort/aiderEleve")
def mentort_aiderEleve():
    pass



#######################################
#Systeme de connexion, login/register.#
#######################################


#Fonctionnalité pour pouvoir ce login
@app.route("/login")
def login():
    return render_template("login.html")


#Route non visible pour réaliser les tests.
@app.route("/login2")
def login2():
    pass


#Fonctionnalité pour pouvoir ce register
@app.route("/register")
def register():
    #Formulaire d'enregistrement
    return render_template("register.html")


#Route non visible pour réaliser les tests.
@app.route("/register2", methods=["POST"])
def register2():

    nom_utilisateur = request.form["nom"]
    prenom_utilisateur = request.form["prenom"]
    email = request.form["email"]
    mot_de_passe = request.form["password"]
    c_mot_de_passe = request.form["comfirm_password"]

    #Test pour les mails, il ne faut pas quelle soitr deja presente dans la base de donné lorsq de la création du compte.
    if bdd.tester_email((email,)) == True:
        flash("Erreur : L'email est déjà utiliser pour un compte.")
        return redirect("/register")

    #Lors de la création du compte les mot de passe doivent etre identique
    if mot_de_passe != c_mot_de_passe:
        flash("Erreur : Les mots de passe ne correspondent pas.")
        return redirect("/register")
    
    
    bdd.ajouter_personne(nom_utilisateur,prenom_utilisateur, email, mot_de_passe)
    return redirect("/eleve/accueil")




# Lancement de l'application web et son serveur
# accessible à l'URL : http://127.0.0.1:1664 (url privé)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)