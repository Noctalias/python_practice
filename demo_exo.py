def inverser_chaine(cdc):
    invertedCdc = ''
    for i in range (len(cdc) - 1, -1, -1):
        invertedCdc += cdc[i] 
        return invertedCdc
    
#print(inverser_chaine("Bonjour")) #censé afficher ruojnoB"

# cdc = "Bonjour"
# len(cdc)
# print(cdc[0])

# def inverser_chaine(cdc):
#     invertedCdc = ''
#     cdc = list(cdc)
#     invertedCdc = invertedCdc + cdc[6]
#     invertedCdc = invertedCdc + cdc[5]
#     invertedCdc = invertedCdc + cdc[4]
#     invertedCdc = invertedCdc + cdc[3]
#     invertedCdc = invertedCdc + cdc[2]
#     invertedCdc = invertedCdc + cdc[1]
#     invertedCdc = invertedCdc + cdc[0]
#         return invertedCdc
    
# print(inverser_chaine("Bonjour"))

# print([51, 5, 99 ["bonjour", ["505"]], 10, 4, 5, 6][3])
#         #Lists                                    #The element we're accessing 
#                                                 #(in this context, a list '["bonjour", ["505"]')



#----------------------------------------------------------------------------------------------------------
#Exercice 2 : Somme elements d'une liste
def sum_list(liste):
    somme = 0
    for elements in liste:
        somme += elements
    return somme

#print("Le plus grand element est :")
#print(sum_list([1, 2, 3, 4])) #Affiche 10

#----------------------------------------------------------------------------------------------------------
#Exercice 3 : Recherche plus grand nombre

def bigger_e(liste):
    max = 0
    for element in liste:
        if element > max:
            max = element
    return max
print("Le plus grand element est :")
print(bigger_e([3, 58, 11, 21]))

#----------------------------------------------------------------------------------------------------------
#Exercice 4 : Factorielle

def facto(n):
    res = 0
    if (n == 0):
        return 1
    else:
        return n * (facto(n - 1))

print("La factorielle de ce nombre est de :")
print(facto(5))

#----------------------------------------------------------------------------------------------------------
#Exercice 5 : Palindrome
def palindrome(mot):
    lenght=len(mot)
    for i in range(lenght): 
        if mot[i] != mot[lenght - i - 1]:
            return False
        return True 

print("Radar palindrome ?")
print(palindrome("radar"))

print("train palindrome ?")
print(palindrome("train"))