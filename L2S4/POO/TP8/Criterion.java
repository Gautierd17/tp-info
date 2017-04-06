package rental;

public interface Criterion {
	  /**
	   * @param v the vehicle that must verify the criterion
	   * @return true if and only id the vehicle v is in accordance with this criterion.
	   * v is said to satisfy this criterion.
	  */
    public boolean isSatisfiedBy(Vehicle v);
}
