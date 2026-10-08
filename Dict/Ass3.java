/*3. Write a Java program to demonstrate Method Overriding and 
Runtime Polymorphism using a parent class Animal and child classes Dog and Cat. */

class Animal{
	void display(){
		System.out.println("This display method of animal parent class");
	}
}

class Dog extends Animal{
	void display(){
		System.out.println("This display method of Dog child class");
	}
}

class Cat extends Animal{
	void display(){
		System.out.println("This display method of Cat child class");
	}
}

public class Ass3{
	public static void main(String[] args){
		Animal a=new Dog();
		a.display();
		a=new Cat();
		a.display();
	}
}