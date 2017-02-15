<?php
require_once('lib/Facture.class.php');
require_once('lib/lectureArguments0.php');

/*
 * à compléter
*/

?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="fr" lang="fr">
<head>
 <meta charset="UTF-8" />
 <title>Facture du club des fans de Star Wars</title>
 <link rel="stylesheet" type="text/css" href="factureStarWars.css" />
 <style type="text/css">

 </style>
</head>
<body>
  <?php
    echo $facture->toHTML();
  ?>
</body>
<html>
