# TP 1 : Algorithmes et programmation

### 1. Prorgammation Modulaire 
### 1.3 Le module Card

[![Download Python](https://pp.vk.me/c836333/v836333766/10af/Uxs7hx8-fOU.jpg)](https://www.python.org/downloads/release/python-344/)
[![Documentation Python](https://pp.vk.me/c836333/v836333766/10b6/r1KTGitaPQA.jpg)](https://docs.python.org/3.4/)
[![Documentation Python Random Module](https://pp.vk.me/c836333/v836333766/10bd/3z7FrKFyssE.jpg)](https://docs.python.org/2/library/random.html)
[![Sphinx](https://pp.vk.me/c836333/v836333766/10c4/1N2SYXB6bXg.jpg)](http://www.sphinx-doc.org/en/stable/install.html)
[![Unix Commands](https://pp.vk.me/c836333/v836333766/10cb/mE9nIDqKWIo.jpg)](https://en.wikipedia.org/wiki/List_of_Unix_commands)

The module Card is a module used for programming a game 'Jeu de la bataille'. It contains nine different functions as:
* **create** : *creates a card with value and color*
* **get_value** : *returns the value of the card*
* **get_color** : *returns the color of the card*
* **to_string** : *returns a string representation of the card*
* **random_card** : *create a card whose value and color are randomly chosen*
* **print** : *print the card*
* **compare_value** : *compares cards values*
* **compare_color** : *compares cards colors*
* **compare** : *compares cards: values and colors*

### 1.3.1 Constants
For this module two constants has been used.
```javascript
VALUES = ["7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]
COLORS = ["club", "diamond", "heart", "spade"]
```
### 1.3.2. Interface du module
#### Function `create`
The construction of this function without documentation looks next way.
```python
1.  def create(value, color):
2.      assert value in VALUES and color in COLORS
3.      card = (value, color)
4.      return card
```
For this function we have to choose between list and tuple because they both can be used in this part of TP1.
Let's check if there's any performance difference between tuples and lists when it comes to instantiation and retrieval of elements.

The `dis` module disassembles the byte code for a function and is useful to see the difference between tuples and lists.

In this case, we can see that accessing an element generates identical code, but that assigning a tuple is much faster than assigning a list.

```python
>>> def a():
...     x=[1,2,3,4,5]
...     y=x[2]
...
>>> def b():
...     x=(1,2,3,4,5)
...     y=x[2]
...
>>> import dis
>>> dis.dis(a)
  2           0 LOAD_CONST               1 (1)
              3 LOAD_CONST               2 (2)
              6 LOAD_CONST               3 (3)
              9 LOAD_CONST               4 (4)
             12 LOAD_CONST               5 (5)
             15 BUILD_LIST               5
             18 STORE_FAST               0 (x)

  3          21 LOAD_FAST                0 (x)
             24 LOAD_CONST               2 (2)
             27 BINARY_SUBSCR
             28 STORE_FAST               1 (y)
             31 LOAD_CONST               0 (None)
             34 RETURN_VALUE
>>> dis.dis(b)
  2           0 LOAD_CONST               6 ((1, 2, 3, 4, 5))
              3 STORE_FAST               0 (x)

  3           6 LOAD_FAST                0 (x)
              9 LOAD_CONST               2 (2)
             12 BINARY_SUBSCR
             13 STORE_FAST               1 (y)
             16 LOAD_CONST               0 (None)
             19 RETURN_VALUE
```

Also, we can check it using Python module `timeit`.

![Terminal](https://pp.vk.me/c836333/v836333766/110b/9VOdwJw_AZ4.jpg)
**...and**
![Terminal](https://pp.vk.me/c836333/v836333766/1112/iDZqJj7YWt8.jpg)
So in this case, instantiation is almost an order of magnitude faster for the tuple, but item access is actually somewhat faster for the list.
*So, in our case tuple is the better decision.*

#### Function `get_value`

```python
def get_value(card):
"""
Exemple:
    >>> c = create('Ace', 'heart')
    >>> get_value(c)
    'Ace'
"""
    return card[0]
  ```
 
  Parameters of this function are defined in the following table.
  
  Paramètres | Retourne
------------ | -------------
card - the card | the value of the card
