<?php
require_once('Article.class.php');
require_once('Decompte.class.php');

class Facture{

   const TVA = 0.2;
   const PRIX_FIGURINE = 15;
   const PRIX_ADHESION = 5;
   const FRAIS_PORT = 7.5;


   private $nom, $prenom, $civilite;
   private $voie, $complAd;
   private $cp, $ville;
   private $listeFigurines = array();
   private $estAdherent = FALSE;
   private $adhesion = FALSE;

   /*
    * La facture est initialisée avec les coordonnées complètes
    **/
   public function __construct($nom, $prenom, $civilite, $voie, $complAd, $cp ,$ville){
      $this->nom = $nom;
      $this->prenom = $prenom;
      $this->civilite = $civilite;
      $this->voie = $voie;
      $this->complAd = $complAd;
      $this->cp = $cp;
      $this->ville = $ville;
   }

   /*
    * Indique si le client est déjà adhérent
    */
   public function setAdherent(){
      $this->estAdherent = TRUE;
   }

   /*
    * On enregistre les figurines une par une
    */
   public function ajouterFigurine($nomFigurine){
      $this->listeFigurines[] = $nomFigurine;
   }

   /*
    * Enregistrement de l'adhésion lors de la commande
    */
   public function ajouterAdhesion(){
      if (!$this->estAdherent){
          $this->adhesion = TRUE;
          $this->estAdherent = TRUE;
      }
   }

   /*
    * Chaîne HTML représentant la facture.
    */
   public function toHTML(){
      return
          '<div class="facture"><h1>Facture</h1>'
         . $this->blocDestinataireHTML()
         . $this->blocFigurinesHTML()
         . $this->blocDecompteHTML()
         . "</div>\n";
   }

   /*
    * User Info
    */
   private function blocDestinataireHTML(){
      $identite = "<p>{$this->civilite} {$this->nom} {$this->prenom}<p>\n";
      $adresse = "<address>";
      $adresse .= "<p>{$this->voie}</p><p>{$this->complAd}</p>\n";
      $adresse .= "<p>{$this->cp} {$this->ville}</p>\n";
      $adresse .= "</address>";
      return "<section class=\"destinataire\"><h2>Client</h2>\n $identite $adresse </section>\n";
   }

   /*
    * Creates list of figurines.
    */

   private function blocFigurinesHTML(){
      $figurinesHTML =
                 '<span class="figurines">'
               . implode($this->listeFigurines, '</span>, <span class="figurines">')
               .'</span>'
               ;
      return "<section class=\"figurines\"><h2>Figurines commandées</h2>$figurinesHTML</section>\n";
   }

   /*
    * Pricing.
    */

   private function blocDecompteHTML(){
      $decompte = new Decompte();
      $decompte->add(new Article('Figurine',self::PRIX_FIGURINE,count($this->listeFigurines)));
      if (count($this->listeFigurines)>=5)
            $decompte->add(new Article('Remise sur quantité',- $decompte->getTotal()*0.15));
      if ($this->estAdherent)
            $decompte->add(new Article('Remise adhérent',- $decompte->getTotal()*0.10));
      if ($this->adhesion)
            $decompte->add(new Article('Adhésion',self::PRIX_ADHESION));
      $decompte->add(new Article('Frais de port',self::FRAIS_PORT));

      return '<section id="apayer"><h2>À payer</h2>'. $decompte->toHTML() . "</section>\n";
   }


}
?>
