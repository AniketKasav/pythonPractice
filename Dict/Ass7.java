/*7. Write a Java program to demonstrate Multiple Inheritance using Interfaces. 
Create two interfaces Printable and Showable and implement both in a single class. */

interface Printable{
	void display();
}

interface Showable{
	void display();
}

class Demo implements Printable,Showable{
	public void display(){
		System.out.println("This is inheritated display method...");
	}
}

public class Ass7{
	public static void main(){
		Demo d=new Demo();
		d.display();
	}
}