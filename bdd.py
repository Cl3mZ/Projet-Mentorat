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
    
    #Récuperer les permissions d'une personne avec son email
    def recuperer_perm(self, email):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
                    SELECT id_permission
                    FROM Personnes
                    WHERE Email = "{email}";"""
        
        resultat = curseur.execute(requete_sql)
        perms = resultat.fetchall()
        connexion.close()
        return perms
    

##################
#    Méthodes    #
##################
    


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
    

    def passer_mentor(self):
        connexion = sqlite3.connect(self.chemin_bdd)
        pass
    
    #Pour s'enregistrer on regarde si l'email est deja presente dans la base de donnée, return True si l'email est deja presente ou False sinon
    def tester_email(self, email_tester):
        email = bdd.recuperer_email()
        for element in email:
            if email_tester == element:
                return True
        return False    

    def obtenir_id_personne_par_email(self, email_connexion):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()
        requete_sql = f"""
            SELECT id_personne
            FROM Personnes
            WHERE Email = ?;
        """
        resultat = curseur.execute(requete_sql, (email_connexion,))
        ligne_resultat = resultat.fetchone()
        id_personne = ligne_resultat[0] if ligne_resultat else None
        connexion.close()
        return id_personne

    def obtenir_id_classe_selon_nom(self, nom_classe):
        id_classe = 1
        return id_classe



    def nouvelle_demande_aide(self, id_personne, id_classe, matiere, contact, informations):
        connexion = sqlite3.connect(self.chemin_bdd)
        curseur = connexion.cursor()

        # Insérer une nouvelle demande d'aide avec les informations de l'utilisateur
        requete_sql = f"""
            INSERT INTO Aide (id_personne, id_classe, Matiere, Contact, Informations)
            VALUES ({id_personne}, {id_classe}, "{matiere}", "{contact}", "{informations}");
        """
        curseur.execute(requete_sql)

        # Commit et fermeture de la connexion
        connexion.commit()
        connexion.close()






bdd = Bdd("bdd/BDD_Mentorat")
