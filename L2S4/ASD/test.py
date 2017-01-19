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
    
    negative=[]
##    for marker in markers:
##        found=False
##        i=0
##        while i<len(positive) and not found:
##            if compare(marker, positive[i])==0:
##                found=True
##            i+=1
##                
##            if found!=True:
##                negative.append(marker)
##           
##             
##    return negative
    
    for marker in markers:
        i=0
        while len(positive)>i:
            if compare(marker, positive[i])==0:
                break
            i+=1
        else:
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

    positive_sorted=sorting.merge_sort(positive,compare) # sorting "positive" list items
    negative = []
    for marker in markers:
        i=0
        while len(positive_sorted)>i:
            if compare(marker, positive_sorted[i])==0:
                break
            i+=1
        else:
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
    
    negative = []
    
    positive_sorted=sorting.merge_sort(positive,compare)
    markers_sorted=sorting.merge_sort(markers,compare)

    for marker in markers_sorted:
        i=0
        while len(positive_sorted)>i:
            if compare(marker, positive_sorted[i])==0:
                break
            i+=1
        else:
            negative.append(marker)

    return negative
        
##if __name__ == "__main__":
##    p = int(sys.argv[1])
##    m = int(sys.argv[2])
##
##    markers = experience.markers(m)
##    positive = experience.experience(p,markers)
##
##    print("Markers: %s" % (markers))
##    print("Positive markers: %s" % (positive))
##    
##    # test stategy 1
##    cpt = 0
##    print("Negative markers: %s" % (negative_markers1(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))
##
##    # test stategy 2
##    cpt = 0
##    print("Negative markers: %s" % (negative_markers2(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))
##
##    # test stategy 3
##    cpt = 0
##    print("Negative markers: %s" % (negative_markers3(markers,positive)))
##    print("Nb. comparisons: %d" % (cpt))
##
