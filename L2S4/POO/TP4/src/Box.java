package example.util;

/**
 *  In this simple version boxes have different weights, there is no other distinction
 * 
 * @author jc 
 * @version 1.0
 */

public class Box {   

    /**
     * creates a Box with given weight 
     * @param weight weight of the created box
     */
    public Box(int weight) {
        this.weight = weight;
    }
    
    // les attributs de la classe Caisse
    /** weight of the box*/
    private int weight;
    
    // les methodes de la classe Caisse 
    /** 
     * returns a weight of created Box
     * @return weight of the created Box
     */
    public int getWeight() {
        return this.weight;
    }
    /**
    * @see java.lang.Object#toString()
    */
    public String toString() {
        return "a box of weight "+this.weight;
    }
}
