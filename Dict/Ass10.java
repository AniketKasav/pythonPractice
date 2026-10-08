/*10. Write a Java program to demonstrate the use of the super keyword. 
Create a parent class with a variable and method, and access both from the child class using super. */

class Parent{
	int num;
	Parent(int num){
		this.num=num;
	}
	
	void display(){
		System.out.println("This is diplay method of parent and num :"+num);
	}
}

class child extends Parent{
	int num;
	child(int num){
		super(num);
		this.num=num;
	}
	
	void display(){
		
		super.display();
		System.out.print("This is display method of child and num : "+num);
	}
}

public class Ass10{
	public static void main(String[] args){
		
		child c =new child(15);
		c.display();
		
	}
}