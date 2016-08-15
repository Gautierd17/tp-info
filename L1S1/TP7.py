#SHCHERBAKOVA Iuliia --- SESI 53 --- 2015/16
#TP 7 http://www.fil.univ-lille1.fr/~L1S1Info/Doc/HTML/tp_suite_lsystem.html
#TP 7 : Dessiner avec la tortue (episode 2)

def dessine(ordres, l, α):
    """
    Trace sur turtle la séquence d'ordre donnée, avec la longueur l et l'angle α
    donné.
    CU : ordres str, l numérique, α numérique → ∅ 
    """
    assert(type(ordres) is str), "ordres doit être du type str"
    assert(type(l) is float or type(l) is int), "l doit être numérique"
    assert(type(α) is float or type(α) is int), "α doit être numérique"

    for i in ordres:
        if i == 'F' or i == 'G':
            forward(l)
        elif i == '+':
            left(α)
        elif i == '-':
            right(α)
        else:
            assert (False), "ordres doit être composé des caractères 'F', 'G', '+' \
ou '-'"

def derive(so, r):
    """
    Revoie la dérivation de la première chaîne passée en paramètre par la
    seconde par rapport à 'F'.
    Remplace dans une chaîne donnée toutes les occurences d’un caracère donné
    par une autre chaîne de caractères.
    CU : so str et r str → str
    >>> derive('', '++')
    ''
    >>> derive('F+F', 'F-F')
    'F-F+F-F'
    """
    assert(type(so) is str), "so doit être du type str"
    assert(type(r) is str), "r doit être du type str"

    retour = ''
    for i in so:
        if i == 'F':
            retour += r
        else:
            retour += i
    return retour

def derive_n(so, r, n):
    """
    Renvoie la dérivation n-ième de la première chaîne par la seconde par
    rapport à 'F'
    CU : CU : so str et r str et n int → str
    >>> derive_n('F+F', 'F-F', 3)
    'F-F-F-F-F-F-F-F+F-F-F-F-F-F-F-F'
    >>> derive_n('FFF', 'F+F+F', 0)
    'FFF'
    """
    assert(type(n) is int), "n doit être du type int"
    # derive() s'occupe des autres assertions, inutile de vérifier so deux fois

    retour = so
    for i in range(0, n):
        retour = derive(retour, r)
    return retour
    
def cherche_regle(ordre, liste_vars, liste_regles):
    """
    Renvoie ordre si ordre n’appartient pas à liste_vars ou liste_regles[i] si
    il existe un indice i vérifiant ordre == liste_vars[i].
    CU : ordre str de taille 1, liste_vars une liste contenant exclusivement des
    types str, liste_regles une liste contenant exclusivement des types str de
    même taille que liste_vars → str
    >>> cherche_regle('F', ['F', 'G'], ['F-F', 'G+G'])
    'F-F'
    >>> cherche_regle('A', ['F', 'G'], ['F-F', 'G+G'])
    'A'
    """
    assert(type(ordre) is str and len(ordre) == 1), "ordre doit être du type \
    str et être de taille 1"
    assert(type(liste_vars) is list), "liste_vars doit être du type list"
    for i in liste_vars:
        assert(type(i) is str), "liste_vars doit contenir exclusivement des \
        types str"
    assert(type(liste_regles) is list), "liste_regles doit être du type list"
    for i in liste_regles:
        assert(type(i) is str), "liste_regles doit contenir exclusivement des \
        types str"
    assert(len(liste_vars) == len(liste_regles)), "liste_regles doit être de \
    même taille que liste_vars"

    if (ordre in liste_vars):
        return liste_regles[liste_vars.index(ordre)]
    else:
        return ordre
        
def derive_mult(so, liste_regles, liste_vars):
    """
    Renvoie la dérivation de so par liste_regles par rapport à liste_vars.
    CU : so str, liste_vars une liste contenant exclusivement des types str,
    liste_regles une liste contenant exclusivement des types str de même taille
    que liste_vars → str
    >>> derive_mult('FGF', ['F', 'G'], ['GG', 'FFF'])
    'GGFFFGG'
    """
    assert(type(so) is str), "so doit être de type str"
    # cherche_regle s'occupe des autres assertions

    retour = ''
    for i in so:
        retour += cherche_regle(i, liste_regles, liste_vars)
    return retour

# Écrivez une fonction derive_mult_n


def derive_mult_n(so, liste_regles, liste_vars, n):
    """
    Renvoie la dérivée de la séquence d’ordres par la liste de règles par
    rapport à la liste des variables.
    CU : so str, liste_vars une liste contenant exclusivement des types str,
    liste_regles une liste contenant exclusivement des types str de même taille
    que liste_vars, n int → str
    >>> derive_mult_n('FGF', ['F', 'G'], ['GG', 'FFF'], 3)
    'GGGGGGGGGGGGFFFFFFFFFFFFFFFFFFGGGGGGGGGGGG'
    """
    assert(type(n) is int), "n doit être du type int"
    # deriv_mult() s'occupe des autres assertions

    retour = so
    for i in range(0, n):
        retour = derive_mult(retour, liste_regles, liste_vars)
    return retour
    
def sauvegarder_etat():
    """
    Sauvegarde l’état de la tortue dans la variable globale etat
    CU : ∅ → ∅
    """

    global etat
    etat[0] = xcor()
    etat[1] = ycor()
    etat[2] = heading()
    
def restaurer_etat():
    """
    Restaure l’état de la tortue depuis la variable globale etat
    CU : ∅ → ∅
    """

    global etat
    penup()
    goto(etat[0], etat[1])
    setheading(etat[2])
    pendown()
    
def dessine2(ordres, l, α):
    """
    Trace sur turtle la séquence d'ordre donnée, avec la longueur l et l'angle α
    donné.
    CU : ordres str, l numérique, α numérique → ∅ 
    """
    assert(type(ordres) is str), "ordres doit être du type str"
    assert(type(l) is float or type(l) is int), "l doit être numérique"
    assert(type(α) is float or type(α) is int), "α doit être numérique"

    for i in ordres:
        if i == 'F' or i == 'G':
            forward(l)
        elif i == '+':
            left(α)
        elif i == '-':
            right(α)
        elif i == '(':
            sauvegarder_etat()
        elif i == ')':
            restaurer_etat()
        else:
            assert (False), "ordres doit être composé des caractères 'F', 'G', '+' \
'-', '(' ou ')'"
    
