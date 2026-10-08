/*6. Write a Java program to demonstrate Method Overriding where a child class 
provides its own implementation of a method defined in the parent class. */

class parent{
	public void display(){
		System.out.println("This is parent display method");
	}
}

class child extends parent{
	public void display(){
		System.out.println("This is child method");
	}
}

public class Ass6{
	public static void main(String[] args){
		//Scanner sc=new Scanner(System.in);
		child ch=new child();
		ch.display();
	}
}