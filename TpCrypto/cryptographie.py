# Importation du module permettant de crypter
from cryptography.fernet import Fernet

def chiffrement(f, fichier_originel, fichier_chiffre):

    # Ouverture du fichier à chiffrer
    fichier_a_chiffrer = open(fichier_originel, "rb")
    aChiffrer = fichier_a_chiffrer.read()
    fichier_a_chiffrer.close()

    # Chiffrement des données de notre fichier
    chiffrement = f.encrypt(aChiffrer)

    # Sauvegarde des données chiffrées
    fichier_chiffre= open(fichier_chiffre, "wb")
    fichier_chiffre.write(chiffrement)
    fichier_chiffre.close()


def dechiffrement(f, fichier_chiffre, fichier_dechiffre):

    # Ouvrir fichier chiffré
    fichierChiffre = open(fichier_chiffre, "rb")
    infosChiffres = fichierChiffre.read()
    fichierChiffre.close()

    dechiffrement = f.decrypt(infosChiffres)

    # Stockage du fichier déchiffré
    fichierDechiffre = open(fichier_dechiffre, "wb")
    fichierDechiffre.write(dechiffrement)
    fichierDechiffre.close()



# Création de la clé
cle = Fernet.generate_key()
fichier_cle = open("cle.key", "wb")
fichier_cle.write(cle)
fichier_cle.close()


# Ouverture du fichier contenant la clé
fichier_cle = open("cle.key", "rb")
cle = fichier_cle.read()
f = Fernet(cle)

###### Test ######

# Methode prenant le fichier que l'on veut chiffrer et 
# le fichier dans le quel l'on veut stocker celui chiffré
chiffrement(f, "fichier.txt", "fichierChiffre.txt") 

# Methode prenant le fichier chiffré et 
# le fichier dans le quel l'on veut stocker celui déchiffré
dechiffrement(f, "fichierChiffre.txt", "fichierDechiffre.txt")
