/*
 * Steven DeMartini
 * OOP MW 6-8
 * assignment 2
 */

public class	ComputerLand	{
	public	static	void	main(String[]	args)	{
		Computer mac =	new	AppleMacbook("MyMac", 1000);
		Computer dell =	new	DellDesktop("MyDell", 500);
		Printer epson = new EpsonPrinter("MyEpson",	2);
				
		PowerSource	source = new PowerSource();
				
		source.attach(mac);
		source.attach(dell);
		source.attach(epson);
				
		mac.addPrinter(epson);
		dell.addPrinter(epson);
				
		mac.scan("Passport application", 10);
		mac.print("Story", 5);
				
		dell.scan("Taxes", 25);
		dell.print("License areement", 2);
			
		source.printInventory();						
				
	}
}