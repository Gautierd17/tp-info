<?php
  require_once('Article.class.php');
  class Decompte {
    private $liste = array();
    private $prixTotal = 0;

    public function add($article){
      $this->liste[] = $article;
      $this->prixTotal += $article->getTotal();
    }
    public function getTotal(){
      return $this->prixTotal;
    }

    public function toHTML(){
       $tva = number_format($this->prixTotal * Facture::TVA,2);
       $ttc = number_format($this->prixTotal + $tva,2);
       $total= number_format($this->prixTotal,2);
       $res = '<table class="decompte">'
        . '<thead><tr><td>désignation</td><td>p.unitaire HT</td><td>quantité</td><td>prix HT</td></tr></thead>'
        . '<tbody>';
       foreach ($this->liste as $i=>$article) {
         $res .= $article->toHTML();
       }
       $res .= "</tbody><tfoot>\n";
       $res .= "<tr><td colspan=\"3\">Total HT</td><td>{$total} €</td></tr>\n";
       $res .= "<tr><td colspan=\"3\">TVA</td><td>{$tva} €</td></tr>\n";
       $res .= "<tr><td colspan=\"3\">Total TTC</td><td>{$ttc} €</td></tr>\n";
       $res .= "</tfoot></table>\n";
       return $res;
    }
  }
?>
  
