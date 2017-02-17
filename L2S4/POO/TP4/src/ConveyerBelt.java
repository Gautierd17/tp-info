package example.util;

// parce que l'on utilise des listes (sera vu plus tard)
import java.util.*;

/**
 * A ConveyerBelt on which box can be put if the box does not weight
 * more that a maximal wight defined at construction
 * @author jc 
 * @version 1.0
 */

public class ConveyerBelt {

	private int capacity = 2;

	/** maximal possible weight */
	private int maxWeight;
	/** the carried boxes */
	private ArrayList<Box> boxesOnBelt; // on utilise une liste de caisses pour
                                            // gerer le tapis

	/**
	 * builds a conveyer belt carrying boxes of maximal given 
	 * @param maxWeight maximal possible weight for boxes
	 */
	public ConveyerBelt(int maxWeight) {
		this.maxWeight = maxWeight;
		this.boxesOnBelt = new ArrayList<Box>();
	}

	// les methodes de la classe TapisRoulant
	/**
	 * returns maximal possible box weight
	 * @return maximal possible box weight
	 */
	public int getMaxWeight() {
		return this.maxWeight;
	}

	/**
	 * a box is added to the belt
	 * 
	 * @param box the added box
	 */
	public void receive(Box box) {
		if (!this.isFull()) {
			this.boxesOnBelt.add(box);
		} else { // pas de gestion d'exception pour l'instant
			System.out.println("belt full, deposit impossible");
		}
	}

	/**
	 * tells whether belt is full
	 * 
	 * @return <code>true</code> if belt is full
	 */
	public boolean isFull() {
		return this.boxesOnBelt.size() == capacity;
	}

	/**
	 * check if given box is not too heavy for this belt
	 * @param box the checked box
	 * @return <code>true</code> if box can be put on this belt, <code>false</code> else
	 */
	public boolean accept(Box box) {
		return box.getWeight() <= this.maxWeight;
	}

	/**
	 * print this belt content
	 */
	public void display() {
		System.out.println("the conveyer belt carries" + this.boxesOnBelt.size() + " box(es)");
		for (Box box : this.boxesOnBelt) {
			System.out.println(box.toString());
		}
	}

	/**
	 * empty this belt (remove all boxes)
	 */
	public void emptyBelt() {
		// ce code sera explique plus tard dans le cours
		Iterator<Box> boxes_it = this.boxesOnBelt.iterator();
		while (boxes_it.hasNext()) {
			boxes_it.next();
			boxes_it.remove();
		}
	}
}
