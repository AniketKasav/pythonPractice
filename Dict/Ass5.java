/*5. Write a Java program using an Abstract class. 
Create an abstract class Shape with an abstract method area(), and implement it in a Circle class. */

abstract class Shape{
	public abstract void area();
}

class Circle extends Shape{
	int r=5;
	public void area(){
		double a=3.14*r*r;
		System.out.println("Area : "+a);
	}
}

public class Ass5{
	public static void main(String[] args){
		Circle c=new Circle();
		c.area();
	}
}