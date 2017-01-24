<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
    <head>
        <title>Premier exercice PHP</title>
        <meta charset="UTF-8" />
        <link rel="stylesheet" href="iniPHP.css" />
    </head>
    <body>
        <header>
            <h1>Premier exercice PHP</h1>
            <h2>Réalisé par <span class="nom">Iuliia Shcherbakova</span></h2>
        </header>
        <section>
            <h2>Question 1</h2>
            <?php
              date_default_timezone_set('Europe/Paris');
              echo "Nous sommes le " . date('d/m/Y h:i:s A');
            ?>
        </section>
        <section>
            <h2>Question 2</h2>
            <?php
              echo "Current PHP version is : " . PHP_VERSION;
              echo "Current OS is : " . PHP_OS;
            ?>
        </section>
        <section>
            <h2>Question 3</h2>
            <?php
              $n=6;

              $text="chaine";
              echo "\$n vaut " . $n . " et \$text vaut " . $text;
            ?>
        </section>
        <section>
            <h2>Question 4</h2>
            <?php
              $n=6;

              $text = '<p>chaine</p>';
              echo str_repeat($text, $n);
            ?>
            <h2>Question 4 (version 2)</h2>
            <?php
              $n=6;
              $text = 'chaine';
              for($z=0;$z<$n;$z++){
                echo "<p>".$text."</p>";
              }
            ?>
        </section>
        <section>
            <h2>Question 5</h2>
            <?php
              $text = "chaine";
              $long=strlen($text);

              echo "<p>".$text."</p>";
                for($z=1;$z<$long;$z++){
                  echo "<p>".substr($text,0,-$z)."</p>";
              }
            ?>
        </section>
        <section>
            <h2>Question 6</h2>
            <ul>
              <?php
                $text = "chaine";
                $long=strlen($text);

                echo "<li>".$text."</li>";
                  for($z=1;$z<$long;$z++){
                    echo "<li>".substr($text,0,-$z)."</li>";
                }
              ?>
            </ul>
        </section>
        <section>
            <h2>Question 7</h2>
            <?php
              $max=9;
              $result = 2;
                for($i=1; $i<=$max; $i++){
                    echo  "2 * $i = ".($i * $result) .', ';

              }
              //echo "2 * 10 = 20"
            ?>
        </section>
        <section>
            <h2>Question 8</h2>
            <?php
              $max=9;
              $result = array(2,3,4,5,6,7,8,9);

              foreach($result as $value){
                for($i=1; $i<=$max; $i++){
                  echo  "$value * $i = ".($i * $value) .', ';
                 }
                  }
            ?>
        </section>
        <section>
            <h2>Question 9</h2>
            <?php
              $cols=10;
              $rows=10;
              echo "<table border=\"1\">";
                      for ($r =1; $r < $rows; $r++){
                          echo'<tr>';
                          for ($c = 1; $c < $cols; $c++)
                              echo '<td>' .$c*$r.'</td>';
                         echo '</tr>';
                      }
                echo"</table>";
            ?>
        </section>
    </body>
</html>
