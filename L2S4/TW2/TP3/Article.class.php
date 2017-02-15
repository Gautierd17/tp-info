<?php
  class Article {
    private $designation;
    private $prix;
    private $quantite;
    
    function __construct($designation, $prix, $quantite = 1){
      $this->designation = $designation;
      $this->prix = round($prix,2);
      $this->quantite = $quantite;
    }
    public function getTotal(){
      return $this->prix * $this->quantite;
    }
    public function toHTML(){
      $prixAffiche = number_format($this->prix,2);
      $prixTotalAffiche = number_format($this->getTotal(), 2);
      return "<tr>"
            . "<td>{$this->designation}</td>"
            . "<td>$prixAffiche €</td>"
            . "<td>$this->quantite</td>"
            . "<td>$prixTotalAffiche €</td>"
            . "</tr>";
    }
  }
?>
