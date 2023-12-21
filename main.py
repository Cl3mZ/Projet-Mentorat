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
# Affiche la page accueil publique sans besoin de connexion.

########################################################
#Page web sans compte
########################################################
@app.route("/")
def accueil():
    print(session)
    return render_template("accueil.html")

@app.route("/information")
def information():
    return render_template("information.html")

@app.route("/demandeAide")
def demande_aide():
    return render_template("demandeAide.html")

@app.route("/devenirMentor")
def devenir_mentor():
    return render_template("devenirMentor.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")


########################################################
#Page web Eleve
########################################################


#Affiche la page accueil privée sur connexion d'un élève
@app.route("/eleve/accueil")
def eleve_accueil():
    return render_template("eleve_accueil.html")


#Affiche la page info 
@app.route("/eleve/infos")
def eleve_infos():
    return render_template("eleve_infos.html")


#Affiche la page aide pour pouvoir demander de l'aide 
@app.route("/eleve/aide")
def eleve_aide():
    return render_template("eleve_aide.html")


#Affiche la page de demande pour devenir mentort
@app.route("/eleve/devenirMentor")
def eleve_devenirMentor():
    return render_template("eleve_devenirMentor.html")

#Affiche la page de demande pour devenir mentort
@app.route("/eleve/contact")
def eleve_contact():
    return render_template("eleve_contact.html")



#########################################################
#Page web Mentor
#########################################################


#Affiche la page accueil privée sur connexion d'un élève
@app.route("/mentor/accueil")
def mentor_accueil():
    return render_template("mentor_accueil.html")


#Affiche la page info 
@app.route("/mentor/infos")
def mentor_infos():
    pass


#Affiche la page aide pour pouvoir demander de l'aide 
@app.route("/mentor/aide")
def mentor_aide():
    pass


#Affiche la page de demande pour devenir mentor
@app.route("/mentor/aiderEleve")
def mentor_aiderEleve():
    pass

#########################################################
#Page web Admin
#########################################################

#Affiche la page de demande pour devenir mentort
@app.route("/admin/listeMentor")
def listeMentor():
    return render_template("admin_liste_mentor.html")

#######################################
#Systeme de connexion, login/register.#
#######################################


#Fonctionnalité pour pouvoir ce login
@app.route("/login")
def login():
    return render_template("login.html")


#Route non visible pour réaliser les tests.
@app.route("/login2", methods = ["POST"])
def login2():
    email = request.form["email"]
    mot_de_passe = request.form["password"]
    #test pour l'email
    if bdd.tester_email((email,)) == True : 
        #test pour le mdp 
        if bdd.tester_mdp((mot_de_passe,), email) == True:
            
            if bdd.recuperer_perm(email) == [(1,)]:
                return redirect("/eleve/accueil")
            if bdd.recuperer_perm(email) == [(2,)]:
                return redirect("/mentor/accueil")
            if bdd.recuperer_perm(email) == [(3,)]:
                return redirect("/admin/accueil")
            
    flash("Erreur lors de l'enregistrement")
    return redirect("/login")



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
        print(bdd.tester_email((email,)))
        flash("Erreur : L'email est déjà utiliser pour un compte.")
        return redirect("/register")

    #Lors de la création du compte les mot de passe doivent etre identique
    if mot_de_passe != c_mot_de_passe:
        flash("Erreur : Les mots de passe ne correspondent pas.")
        return redirect("/register")
    
    #Si tous les tests sont bon, ajoute une personne dans la bdd et renvoie vers la page /eleve/accueil, 
    #on considere qu'une personne qui creer sont compte est eleve
    bdd.ajouter_personne(nom_utilisateur, prenom_utilisateur, email, mot_de_passe)
    return redirect("/eleve/accueil")

@app.route("/egg")
def egg():
    #easter egg
    return render_template("easter_egg.html")


# Lancement de l'application web et son serveur
# accessible à l'URL : http://127.0.0.1:1664 (url privé)
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=1664, threaded=True, debug=True)