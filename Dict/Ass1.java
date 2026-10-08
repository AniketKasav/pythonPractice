/*1. Write a Java program to demonstrate Encapsulation by creating a Student class with 
private data members name and age, and public getter and setter methods. */

import java.util.Scanner;

class Student{
	private String name;
	private int age;

	public void setName(String name){
		this.name=name;
	}
	
	public String getName(){
		return name;
	}
	
	public void setAge(int age){
		this.age=age;
	}
	
	public int getAge(){
		return age;
	}
}

public class Ass1{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		Student s=new Student();
		System.out.println("Enter the name of student : ");
		String name=sc.nextLine();
		
		System.out.println("Enter the age of student : ");
		int age=sc.nextInt();
		s.setName(name);
		s.setAge(age);
		
		System.out.println("Name : "+s.getName()+"  age: "+s.getAge());
	}
}