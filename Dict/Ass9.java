/*9. Write a Java program to demonstrate Abstraction using an abstract class Employee with 
an abstract method calculateSalary(), and implement it in a Developer class. */

abstract class Employee{
	abstract void calculateSalary();
}

class Developer extends Employee{
	int basicPay=30000;
	void calculateSalary(){
		int salary=basicPay+5000;
		System.out.println("Developer salary : "+salary);
	}
}

public class Ass9{
	public static void main(String[] args){
		Developer d=new Developer();
		d.calculateSalary();
	}
}