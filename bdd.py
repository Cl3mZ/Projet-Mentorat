import sqlite3

class Bdd:
    """Classe pour faire le lien entre la base de données SQLite et le programme"""

    def __init__(self, chemin_bdd):
        """Initialise la base de données

        Parameters:
            chemin_bdd (string) : chemin vers le fichier SQLite
        """
        self.chemin_bdd = chemin_bdd

#################
#    Getters    #
#################

    # Récupérer tous les emails de la bdd
    def recuperer_email(self):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """
            SELECT mail
            FROM Personnes;"""
        resultat = curseur.execute(requete_sql)
        email = resultat.fetchall()
        connexion.close()
        return email

    # Récupérer les permissions d'une personne avec son email
    def recuperer_perm(self, email):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
                    SELECT nom_permissions
                    FROM Personnes
                    WHERE mail = ?;"""

        resultat = curseur.execute(requete_sql, (email,))
        perms = resultat.fetchall()
        connexion.close()
        return perms

##################
#    Méthodes    #
##################

    # Méthode pour tester un mdp
    def tester_mdp(self, mdp_tester, email):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            SELECT password
            FROM Personnes
            WHERE mail = ?;"""
        resultat = curseur.execute(requete_sql, (email,))
        mdp = resultat.fetchall()
        connexion.close()
        if mdp[0] == mdp_tester:
            return True
        return False 

    # Méthode pour ajouter une personne dans la bdd
    def ajouter_personne(self, nom, prenom, nom_classe, email, password):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            INSERT INTO Personnes (nom, prenom, mail, password, nom_classes, nom_permissions)
            VALUES (?, ?, ?, ?, ?, "eleve");
        """
        curseur.execute(requete_sql, (nom, prenom, email, password, nom_classe))
        connexion.commit()
        connexion.close()

    def passer_mentor(self):
        pass

    # Pour s'enregistrer, on regarde si l'email est déjà présent dans la base de données.
    # Retourne True si l'email est déjà présent, ou False sinon.
    def tester_email(self, email_tester):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """
            SELECT mail
            FROM Personnes
            Where mail = ?;"""
        resultat = curseur.execute(requete_sql,(email_tester))
        email = resultat.fetchone()
        connexion.close()
        if email == email_tester :
            return True
        return False



    def nouvelle_demande_aide(self,email_connexion, nom_matiere, contact, informations):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()

        # Récupérer l'id_personne de la session

        # Insérer une nouvelle demande d'aide avec les informations de l'utilisateur
        requete_sql = f"""
           INSERT INTO Aides (nom_classes, mailD, nom_matieres, contact, informations, id_mentor, dateD, dateF)
            VALUES (
                (SELECT nom_classes FROM Personnes WHERE mail = ?),
                ?,
                ?,
                ?,
                ?,
                NULL,
                DATE('now'),
                NULL
            );
        """
        curseur.execute(requete_sql, (email_connexion, email_connexion, nom_matiere, contact, informations))

        # Commit et fermeture de la connexion
        connexion.commit()
        connexion.close()


bdd = Bdd("bdd/BDD_Mentorat")

#vous voyer le code ou pas