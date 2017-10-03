
public interface Printer extends ElectronicDevice{

	public abstract void scan(String jn, int p,Computer c);
	
	
	public abstract void print(String jn, int p);
}
