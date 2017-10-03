/*
 * Steven DeMartini
 * OOP MW 6-8
 * assignment 2
 */


public class PowerSource {
	
	private int count = 0;
	private ElectronicDevice[] devs = new ElectronicDevice[6];
	public void attach(ElectronicDevice e)
	{
		devs[count] = e;
		count++;
	}
	
	public void printInventory()
	{
		System.out.println("--Invintory--");
		for (int i = 0; i < count; i++ )
		{
		    System.out.println(devs[i].getSummary());
		}
		//calls getSummary() on all its devices
	}

	
}
