/*2. Write a Java program to demonstrate Inheritance using the extends keyword. 
Create a Parent class with a method display() and a Child class that inherits and calls the method. */

class parent{
	public void display(){
		System.out.println("This is parent display method");
	}
}

class child extends parent{
	
}

public class Ass2{
	public static void main(String[] args){
		//Scanner sc=new Scanner(System.in);
		child ch=new child();
		ch.display();
	}
}