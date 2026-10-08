/*8. Write a Java program to demonstrate Data Hiding using the private access modifier. 
Create a BankAccount class with a private balance and methods to deposit and display the balance. */

class BankAccount{
	private int balance;
	BankAccount(){
		
	}
	BankAccount(int balance){
		this.balance=balance;
	}
	
	void deposit(int amount){
		balance=amount;
	}
	
	void display(){
		System.out.println("Account Balance is "+balance);
	}
}

public class Ass8{
	public static void main(String[] args){
		BankAccount b=new BankAccount();
		b.deposit(45000);
		b.display();
	}
}