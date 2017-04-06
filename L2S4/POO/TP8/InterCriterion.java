package rental;
import java.util.*;
/**
 * An InterCriterion performs the intersection of criterions. It is satisfied if each of its criterion is satisfied.
*/
public class InterCriterion implements Criterion {
    
    private List<Criterion> allCriterions;
    /*private String brand, model;
    private int year;
    private float price;*/
    /** creates an InterCriterion with no criterion */
    public InterCriterion() { //String brand, String model, int year, float price
        //pass
    }

    /** adds a new criterion
    * @param c the added criterion
    */
    public void addCriterion(Criterion c) {
        // TO DO
        allCriterions.add(c);
    }

    /** This is satisfied if each of its criterion is satisfied.
     * @see Criterion#isSatisfiedBy(Vehicle) */
    public boolean isSatisfiedBy(Vehicle v) {
        // TO DO
        
    }
}
