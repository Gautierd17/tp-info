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

