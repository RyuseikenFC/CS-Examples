/*
 * Steven DeMartini
 * OOP MW 6-8
 * assignment 2
 */


public abstract class Computer implements ElectronicDevice{

	private String name;
	private int storage;
	private Printer pr;
	private String operatingSystem;
	Computer(String n, int s)
	{
		name = n;
		storage = s;
	}
	public void addPrinter(Printer p)
	{
		pr = p;
	}
	public void save(int i)
	{
		storage -= i;
	}

	public void setOS(String s){
		operatingSystem = s;
	}
	
	@Override
	public String getSummary(){
		return name + " running " + operatingSystem + " with "+ storage;	
	}
	
	public String getName() {
		return name;
	}
	public String getOperatingSystem() {
		return operatingSystem;
	}
	public void scan(String string, int i) {
		pr.scan(string , i ,this);
		
	}
	public void print(String string, int i) {
		pr.print(string, i);
		
	}
}
