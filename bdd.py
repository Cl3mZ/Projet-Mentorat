import sqlite3


class Bdd:
    """Classe pour faire le lien entre la base de données SQLite et le programme"""

    def __init__(self, chemin_bdd):
        """Initialise la base de données

        Parameters:
            chemin_bdd (string) : chemin vers le fichier SQLite
        """
        self.chemin_bdd = chemin_bdd


    #Récuperer tout les email de la bdd
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
    

    #Pour s'enregistrer on regarde si l'email est deja presente dans la base de donnée, return True si l'email est deja presente ou False sinon
    def tester_email(self, email_tester):
        email = bdd.recuperer_email()
        for element in email:
            if email_tester == element:
                return True
        return False


    #Methode pour tester un mdp 
    def tester_mdp(self, mdp_tester, email):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            SELECT Password
            FROM Personnes
            WHERE Email = "{email}";"""
        resultat = curseur.execute(requete_sql)
        mdp = resultat.fetchall()
        connexion.close()
        if mdp[0] == mdp_tester:
            return True
        return None


    #Méthode pour ajouter une personne dans la bdd
    def ajouter_personne(self, nom, prenom, email, password):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            INSERT INTO Personnes (Nom, Prenom, Email, Password, id_permission)
            VALUES("{nom}","{prenom}","{email}","{password}", "1");"""
        curseur.execute(requete_sql)
        connexion.commit()
        connexion.close()
    

    def recuperer_perm(self, email):
        print(email)
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
                    SELECT id_permission
                    FROM Personnes
                    WHERE Email = "{email}";"""
        
        resultat = curseur.execute(requete_sql)
        perms = resultat.fetchall()
        connexion.close()
        print(perms)
        return perms

    def passer_mentor(self):
        connexion = sqlite3.connect(self.chemin_bdd)
        pass
    




bdd = Bdd("bdd/BDD_Mentorat")
