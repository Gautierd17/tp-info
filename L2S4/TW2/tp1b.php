<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Premier exercice PHP</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="iniPHP.css" />
        <link rel="stylesheet" href="terrain.css" />
    </head>
    <style media="screen">
      span {
        border: 1px solid grey;
        padding: 4px;
        color: red;
      }
      span.noir {
        background-color: black;
        color: white;
      }
      span.blanc {
        background-color: white;
        color: black;
      }
    </style>
    <body>
        <header>
            <h1>Lecture et écriture de fichiers en PHP</h1>
            <h2>Réalisé par <span class="nom">Iuliia Shcherbakova</span></h2>
        </header>
        <section>
            <h2>Exercice 1</h2>
            <?php

              $file = fopen("liste_noms.txt", "r");;
              if ($file) {
                  while (($line = fgets($file)) !== false) {
                      echo "<p>"."$line"."</p>";
                  }

                  fclose($file);
                }
                else {
                  echo "Error while opening file";
                }

              ?>

        </section>
        <section>
            <h2>Exercice 2</h2>
            <h4>Question 1</h4>
            <?php
              $file = fopen("terrain.txt","r");

              while (!feof ($file)){
                   echo "<span>".fgetc($file)."</span>"; //reading char by char and creating span tags
                   if (fgetc($file)=="N"){
                     echo "<span class='noir'>".fgetc($file)."</span>";
                   }
                   elseif (fgetc($file)=="B") {
                     echo "<span class='blanc'>".fgetc($file)."</span>";
                   }
                   else {
                     echo "<span>".fgetc($file)."</span>";.
                   }
                   }

                 fclose($file);

            ?>
        </section>

      </body>
  </html>
