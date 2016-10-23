#!/usr/bin/python3
# -*- coding: utf-8 -*-

# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#                                                                             #
#    minesweeper.py: source code of minesweeper game                          #
#    TP3 AP2 : jeu du démineur                                                #
#                                                                             #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #

"""
The minesweeper game module who creates the minesweeper grid and set number of bombs in this grid.
It uses cell.py module to create cells for the game grid.
It uses graphicalboard.py module to create UI for the game using Tkinter.
"""
import cell
import random
from enum import Enum


################################################
# Type declaration
################################################

class GameState(Enum):
    """
    A class to define an enumerated type with three values :

    * ``winning``
    * ``losing``
    * ``unfinished``

    for the three state of minesweeper game.
    """
    winning = 1
    losing = 2
    unfinished = 3


##############################################
# Functions for game's setup and management
##############################################


def neighborhood(x, y, width, height):
    """
    return the list of coordinates of the neighbors de cell (x,y) in a
    grid of size width*height

    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :return:
    :rtype: list of tuple
    :UC: 0 <= x < width and 0 <= y < height
    :Examples:

    >>> neighborhood(3, 3, 10, 10)
    [(2, 2), (2, 3), (2, 4), (3, 2), (3, 4), (4, 2), (4, 3), (4, 4)]
    >>> neighborhood(0, 3, 10, 10)
    [(0, 2), (0, 4), (1, 2), (1, 3), (1, 4)]
    >>> neighborhood(0, 0, 10, 10)
    [(0, 1), (1, 0), (1, 1)]
    >>> neighborhood(9, 9, 10, 10)
    [(8, 8), (8, 9), (9, 8)]
    >>> neighborhood(3, 9, 10, 10)
    [(2, 8), (2, 9), (3, 8), (4, 8), (4, 9)]
    """
    x_beg= x-1
    x_end= x+2
    y_beg= y-1
    y_end= y+2

    if x_beg< 0:
        x_beg=0
    if x_end> width-1:
        x_end= width
    if y_beg<0:
        y_beg= 0
    if y_end> height-1:
        y_end= height
        
    l= [(i,j) for i in range(x_beg, x_end) for j in range (y_beg, y_end)]
    l.remove((x,y))
    return l 


def __make_grid(width, height, nbombs):
    """
    return a minesweeper grid of size width*height cells
    with nbombs bombs.

    :param width: horizontal size of game (default = 30)
    :type width: int
    :param height:  vertical size of game (default = 20)
    :type height: int
    :param nbombs:  number of bombs (default = 99)
    :type nbombs: int
    :return: a fresh grid of  width*height cells
    :rtype: list of list of cells
    """
    assert 0 < width, 'width must be a positive integer'
    assert 0 < height, 'height must be a positive integer'
    assert 0 <= nbombs <= width * height, "nbombs must don't exceed width*height"
    coords = [(x, y) for y in range(height) for x in range(width)]
    random.shuffle(coords)
    grid = [[cell.make() for y in range(height)] for x in range(width)]
    for i in range(nbombs):
        x, y = coords[i]
        cell.set_bomb(grid[x][y])
        for neighbor in neighborhood(x, y, width, height):
            x1, y1 = neighbor
            nb_bombs = cell.number_of_bombs_in_neighborhood(grid[x1][y1]) + 1
            cell.set_number_of_bombs_in_neighborhood(grid[x1][y1], nb_bombs) 
    return grid


def make_game(width=30, height=20, nbombs=99):
    """
    return a minesweeper game  of size width*height cells
    with nbombs bombs.

    :param width: [optional] horizontal size of game (default = 30)
    :type width: int
    :param height: [optional] vertical size of game (default = 20)
    :type height: int
    :param nbombs: [optional] number of bombs (default = 99)
    :type nbombs: int
    :return: a fresh grid of  width*height cells
    :UC: 0 < width, height and 0 <= nbombs <= width*height
    """
    return {'width' : width,
            'height' : height,
            'nbombs' : nbombs,
            'grid' : __make_grid(width, height, nbombs)}

def get_height(game):
    """
    :param game: a minesweeper game
    :type game: game
    :return: height of the grid in game
    :rtype: int
    :UC: none
    """
    return game['height']

def get_width(game):
    """
    :param game: a minesweeper game
    :type game: game
    :return: width of the grid in game
    :rtype: int
    :UC: none
    """
    return game['width']

def get_cell(game, x, y):
    """
    :param game: a minesweeper game
    :type game: game
    :param x: x-coordinate of a cell
    :type x: int
    :param y: y-coordinate of a cell
    :type y: int
    :return: the cell of coordinates (x,y) in the game's grid
    :type: cell
    :UC: 0 <= x < width of game and O <= y < height of game
    """
    return game['grid'][x][y]

def get_state(game):
    """
    :param game: a minesweeper game
    :type game: game
    :return: the state of the game (winning, losing or unfinished)
    :rtype: GameState
    :UC: none
    """
    ### if number of selected hypothetical bombs(and theirs coords) is equal to number of
    ### bombs passed as parameter in function __make_grid
    ### return winning state

    
    for i in range(get_width(game)):
        for j in range(get_height(game)):
            
            cells = get_cell(game,i,j)
            if cell.reveal(cells) == cell.is_bomb(cells):
                return GameState.losing
            elif cell.is_hypothetic_bomb(cells) == cell.is_bomb(cells):
                return GameState.winning
            else:
                return GameState.unfinished


def reveal_all_cells_from(game, x, y):
    """
    :param game:
    :type game: game
    :param x: x-coordinate
    :param y: y-coordinate
    :return: none
    :Side effect: reveal all cells of game game from the initial cell (x,y).
    :UC: 0 <= x < width of game and O <= y < height of game
    """
      
    

if __name__ == '__main__':
    import doctest
    doctest.testmod()



