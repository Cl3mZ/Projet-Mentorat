"""Application web dynamique Bonjour

Ce tutoriel présente le framework (cadriciel) Flask qui permet de réaliser
des applications web dynamiques relativement simplement.
"""

import sqlite3


class Bdd:
    """Classe pour faire le lien entre la base de données SQLite et le programme"""

    def __init__(self, chemin_bdd):
        """Initialise la base de données

        Parameters:
            chemin_bdd (string) : chemin vers le fichier SQLite
        """
        self.chemin_bdd = chemin_bdd


    def recuperer_email(self):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = """
            SELECT email
            FROM Personnes;"""
        resultat = curseur.execute(requete_sql)
        email = resultat.fetchall()
        connexion.close()
        return email
    

    def ajouter_personne(self, nom, prenom, email, password):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            INSERT INTO Personnes (Nom, Prenom, Email, Password)
            VALUES("{nom}","{prenom}","{email}","{password}");"""
        curseur.execute(requete_sql)
        connexion.commit()
        connexion.close()
    

    def tester_email(self,email_tester):
        email = bdd.recuperer_email()
        for element in email:
            print(element)
            if email_tester == element:
                return True
        return False


bdd = Bdd("bdd/BDD_Mentorat")
