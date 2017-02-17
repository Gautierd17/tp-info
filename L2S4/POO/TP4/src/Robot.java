package example;

import example.util.*;
/**
 * A robot can carry one box at a time and can put it on a bellt
 *
 * @author jc
 * @version 1.0
 */

public class Robot {
	/**
	 * Initially a robot carrys no box
	 */


	public Robot() {
		this.carriedBox = null;
	}

	// les attributs de la classe Robot
	/** box carried by the box (null if none) */
	private Box carriedBox;

	// les methodes de la classe Robot
	/**
	 * this robot takes a box of it is not already acrrying one
	 *
	 * @param box
	 *            the taken box
	 * @exception IllegalStateException if this robot is already carrying a box
	 */
	public void take(Box box) {
		if (!this.carryBox()) { // already carrying a box ?
			this.carriedBox = box;
		}
		else {
		    throw new IllegalStateException("already carrying a box");
		}
	}

	/**
	 * this robot puts the box it is carrying on the belt, message is displaid if it is not possible to put the box on the belt
	 *
	 * @param belt
	 *            the belt where to put the carrying belt
	 */
	public void putOn(ConveyerBelt belt) {
		if (this.carryBox() && belt.accept(carriedBox) && !belt.isFull()) {
		    // put box on belt
			belt.receive(carriedBox);
			// no more box is carried
			this.carriedBox = null;
		} else {
			if (!this.carryBox()) {
				System.out.println("no box carried");
			} else if (belt.isFull()) {
				System.out.println("belt is full");
			} else {
				System.out.println("box is too heavy for this belt : " + this.carriedBox.getWeight() + " but "
						+ belt.getMaxWeight() + " max authorized");
			}
		}
	}

	/**
	 * returns <tt>true</tt> iff this robot is carrying a box
	 *
	 * @return <tt>true</tt> iff this robot is carrying a box
	 */
	public boolean carryBox() {
		return this.carriedBox != null;
	}

	public static void main(String[] args) {

		System.out.println("beginning of main from robot.Robot");

		Robot robbie = new Robot();
		ConveyerBelt belt1 = new ConveyerBelt(50);
		ConveyerBelt belt2 = new ConveyerBelt(150);
		Box box10 = new Box(10);
		Box box15 = new Box(15);
		Box box100 = new Box(100);
		Box box60 = new Box(60);

		robbie.take(box10);
		robbie.putOn(belt1);
		robbie.take(box15);
		robbie.putOn(belt1);
		robbie.take(box100);
		robbie.putOn(belt2);

		belt1.display();

		System.out.println("end of main from robot.Robot");
}

}
