/*
 * Steven DeMartini
 * OOP MW 6-8
 * assignment 2
 */


public class EpsonPrinter extends Computer implements Printer{
	
	
	EpsonPrinter(String n, int s) {
		super(n, s);
		this.setOS("Linux");
	}

	@Override
	public void scan(String jn, int p, Computer c) {
		c.save(p*5);
		System.out.println("scanning "+ jn+ " to " + c.getName());
	}
	
	@Override
	public void print(String jn, int p)
	{
		for (int i = 0;i<p; i++ )
		{
			System.out.println("printing page " + i + " of " + jn);
		}
		
	}
}