#fonction de base de Python, permet d'avoir deux à trois scénarii si telle ou telle 
#condtion est remplie
#note: toute valeur non booléenne sera convertie en valeur booléenne
#if 0:
 #   print("ce message s'affichera tout le temps(if 1 pour 1=True)")
#else:
    #print("ce message ne s'affichera pas(if 0 pour 0=False")

#if 1:
    #print("ce message s'affichera tout le temps(if 1 pour 1=True)")
#else:
    #print("ce message ne s'affichera pas (if 0 pour 0=False")

# cars=['shelby gt350', 'nissan GTR', 'lancia Stratos']
# if 'indian' in cars:
#     print("indian est une marque de voitures")
# else:
#     print("indian est une marque de motos")
# if 'nissan GTR' in cars:
#     print("la nissan GTR est une fantastique voiture")
# else:
#     print("la nissan GTR n'est pas une fantastique voiture")

# is_user_authenticated = False
# if is_user_authenticated == True:
#     print("l'utilisateur peut se connecter au back")
# else:
#     print("oups! il faut qu'il se connecte pour accéder au back")
form_pwd = "123"
pwd_db = "abc"
# if form_pwd == pwd_db:
#     print("recu 5 sur 5, connexion établie")
# else:
#     print("houston, on a a un problème! la connexion ne se fait pas")

# users_pwd = ['bobo', 'baba', 'binbin'] #ceci est une liste, on voit les []
# pwd_db= "abc"
# user_in_form = 'bobou'
# pwd_in_form = 'tuveuxvoirmabite?'

# if user_in_form in users_pwd and pwd_in_form == pwd_db:
#     print("connexion établie")
# else:
#     print("il y a de la friture sur la ligne, etes-vous sur d'avoir mis les bonnes infos?")
#note: on peut mettre des parenthèses au niveau des "if" pour plus de clarté ex: if()
#note: du a l'architecture en couches des navigateurs, on ne peut pas mettre de boucles, sinon le 
#fetch ne se fait pas
#note: la priorité desopérateurs peut etre iportant, penser à lire ceci https://learntutorials.net/fr/python/topic/5040/priorite-de-l-operateur


from cgi import print_arguments
import random

# electricity_availability = bool(random.randint(0, 1))
# water_availability = bool(random.randint(0, 1))
# gas_availability = bool(random.randint(0, 1))
# print('is there electricity? ', electricity_availability)
# print('is there water?', water_availability)
# print('is there gas? ', gas_availability)

# if electricity_availability == False and water_availability == False and gas_availability == False:
#     print('vous pouvez partir en WE sans problème')
# else:
#     print("y a un truc à couper")

# print(not False)

# if not electricity_availability and not water_availability and not gas_availability:
#     print("on peut partir en WE")
# else:
#     if electricity_availability == True and gas_availability == True and water_availability == True:
#         print("tout est à couper")
#     elif electricity_availability == True:
#         print('il faut couper l electricite')
#     elif gas_availability == True:
#         print('il faut couper le gaz')
#     elif electricity_availability  == True and water_availability == True:
#         print('il faut couper l eau et l electricite' )
#     elif electricity_availability and gas_availability == True:
#         print("il faut couper le gaz et l'électricité")
#     else:
#         print('l eau est à couper')

# has_cash = bool(random.randint(0, 1))
# has_check =bool(random.randint(0, 1))
# has_card = bool(random.randint(0, 1))
# print("avez-vous du cash?", has_cash)
# print("avez-vous un chéquier?", has_check)
# print("avez-vous la carte bleue? ", has_card)
# if has_cash or has_check  or has_card :# ceci
#     if has_check:
#         print("vous avez le chéquier")
#     elif has_card:
#         print("vous avez la carte")
#     elif has_cash:
#         print("vous avez du cash")
#     elif has_cash and has_check:
#         print("vous avez du cash et un chèque")
#     elif has_cash and has_card:
#         print("vous avez du cash et un chéquier")
#     elif has_card and has_check:
#         print("vous avez la carte et le chèque")
#     else: 
#         print("vous avez tous les moyens")
# else:
#     print("vous n'avez pas de moyen de paiement")
age = random.randint(0,100)
print(age)
if age <= 5:
    print("bébé")
elif 5 <= age <= 11:
    print("enfant")
elif 12 <= age <= 25:
    print("ado, jeune adulte")
elif 26 <= age <= 59:
    print("adulte")
else:
    print("vieux")