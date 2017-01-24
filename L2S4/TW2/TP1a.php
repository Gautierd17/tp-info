//Exercice 1.

<?php

date_default_timezone_set('Europe/Paris');
echo "Nous sommes le " . date('d/m/Y h:i:s A');

?>

//Exercice 2.

<?php

echo "Current PHP version is : " . PHP_VERSION; 
echo "Current OS is : " . PHP_OS;

?>

//Exercice 3.

<?php

$n=6;
$text="chaine";

echo "\$n vaut " . $n . " et \$text vaut " . $text;

?>

Exercice 4.
===========
<?php

$n=6;
$text = '<p>chaine</p>';
echo str_repeat($text, $n);

?>

***or***

<?php

$n=6;
$text = 'chaine';
for($z=0;$z<$n;$z++){
  echo "<p>".$text."</p>";
}

?>

Exercice 5.
===========

<?php

$text = "chaine";
$long=strlen($text);

echo "<p>".$text."</p>";
for($z=1;$z<$long;$z++){
  echo "<p>".substr($text,0,-$z)."</p>";
}

?>

Exercice 6.
===========

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

Exercice 7.
===========

<?php

$max=9;

$result = 2;
for($i=1; $i<=$max; $i++){
    echo  "2 * $i = ".($i * $result) .', ';
   
}
//echo "2 * 10 = 20" // pour finir la boucle 
?>

Exercice 8.
===========

<?php

$max=9;

$result = array(2,3,4,5,6,7,8,9);
foreach($result as $value){
for($i=1; $i<=$max; $i++){
    echo  "$value * $i = ".($i * $value) .', ';
   
}
    
   }

?>

Exercice 9.
===========


<?php
$cols=10;
$rows=10;
echo "<table border=\"1\">";

        for ($r =0; $r < $rows; $r++){

            echo'<tr>';

            for ($c = 0; $c < $cols; $c++)
                echo '<td>' .$c*$r.'</td>';
           echo '</tr>'; 

        }

  echo"</table>";

?>
