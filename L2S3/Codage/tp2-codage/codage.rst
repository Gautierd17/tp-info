def table():
    for i in range(21):
        print('{:2d} : {:5s} {:2s} {:2s}'.format(i, integer_to_string(i, 2), integer_to_string(i,8), integer_to_string(i, 16))
              
4  Lecture et écriture de fichiers
4.2  Lecture de fichier

Question 20.

>>> stream_bin = open('data.txt', 'rb')
>>> stream_text = open('data.txt', 'r')

Question 21.

>>> stream_bin.read()
b'\xf0\x9f\x99\x8b'
>>> stream_text.read()
'\U0001f64b'

>>> content_bin = stream_bin.read()
>>> content_text = stream_text.read()



5  Représentation des caractères ISO-859-1 et UTF-8

Question 26.
1. convertir le fichier cigale-ISO-8859-1.txt en un fichier équivalent codé en UTF-8 ; 
> iconv --from-code ISO-8859-1 --to-code UTF-8 --output new_cigale_utf8.txt cigale-ISO-8859-1.txt
2. convertir le fichier cigale-UTF-8.txt en un fichier équivalent codé en ISO-8859-1. 
> iconv --from-code ISO-8859-1 --to-code UTF-8 --output new_cigale_iso.txt cigale-UTF-8.txt

> diff cigale-ISO-8859-1.txt new_cigale_iso.txt
Il n'y a pas de difference entre des documents cigale-ISO-8859-1.txt et new_cigale_iso.txt

Question 27.
> cigale-UTF-8.txt 639 oct.
> cigale-ISO-8859-1.txt 624 oct.

cigale-UTF-8.txt > cigale-ISO-8859-1.txt

5.2  Conversion d’un fichier du format ISO-8859-1 au format UTF-8

Question 28.
