# -*- coding: utf-8 -*-

"""
:mod:`test` module : test module for experiences assignment

:author: `FIL - IEEA - Univ. Lille1.fr <http://portail.fil.univ-lille1.fr>`_

:date: 2015, december
"""

import sys
import experience
import sorting

def compare (m1,m2):
    return experience.compare(m1,m2)

def my_compare (m1,m2):
    global cpt
    cpt+=1
    return compare(m1,m2)

# STRATEGY 1
def negative_markers1(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the list of positive markers.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []
    for marker in markers:
        found = False
        j=0
        while j<len(positive) and not found:
            if my_compare(marker, positive [j])==0:
                found= True 
            j+=1
        if not found:
            negative.append(marker)
    return negative



# STRATEGY 2
def negative_markers2(markers,positive):
    """
    Computes the list of negative markers from the list of markers and
    the sorted list of positive markers.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    negative = []
    positive_sorted=sorting.merge_sort(positive,compare)
    
    for marker in markers:
        found = False
        a=0
        b=len(positive_sorted)-1
        while a<b and not found:
            j=(a+b)//2
            if my_compare(marker, positive_sorted[j])==0:
                found=True
            elif my_compare(marker, positive_sorted[j])==-1:
                b=j
            else:
                a=j+1
        if not found:
            negative.append(marker)
    return negative

# STRATEGY 3
def negative_markers3(markers,positive):
    """
    Computes the list of negative markers from the sorted list of markers and
    the sorted list of positive markers.

    :param markers: The list of markers
    :type markers: List of String
    :param positive: The list of positive markers
    :type positive: List of String
    :return: The list of negative markers
    :rtype: List of String
    """
    positive_sorted=sorting.merge_sort(positive,compare)
    markers_sorted=sorting.merge_sort(markers,compare)
    negative = []
    j=0
    for marker in markers_sorted:
        found = False
        while j<len(positive_sorted) and not found:
            if my_compare(marker, positive_sorted [j])==0:
                found= True
                j+=1
            elif my_compare(marker, positive_sorted [j])==-1:
                negative.append(marker)
                found=True
            else:
                j+=1
        if not found:
            negative.append(marker)
    return negative

if __name__ == "__main__":
    p=1
    m = int(sys.argv[1])
    CPT=[]
    while p<=m:
        CPT=[]
        markers = experience.markers(m)
        positive = experience.experience(p,markers)
        CPT.append(m)
        CPT.append(p)
    
        # test stategy 1
        cpt = 0
        negative_markers1(markers,positive)
        cpt
        CPT.append(cpt)
        # test stategy 2
        cpt = 0
        negative_markers2(markers,positive)
        cpt
        CPT.append(cpt)
        # test stategy 3
        cpt = 0
        negative_markers3(markers,positive)
        cpt
        CPT.append(cpt)
        print(CPT)
        p+=1
        
