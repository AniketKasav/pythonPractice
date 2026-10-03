//Take n numbers from the user and count how many are positive, negative, and zero. Also print the
//largest positive number and smallest negative number.

import java.util.*;

public class Ass1{
	public static void main(String[] args){
		Scanner sc=new Scanner(System.in);
		System.out.println("Enter 10 numbers :");
		int[] nums=new int[10];
		for(int i=0;i<10;i++){
			nums[i]=sc.nextInt();
		}
		int zcount=0;
		int ecount=0;
		int ocount=0;
		for(int n:nums){
			if(n==0){
				zcount++;
			}
			else if(n%2==0){
				ecount++;
			}else{
				ocount++;
			}
		}
		System.out.println("Count of zero : "+zcount);
		System.out.println("Count of even : "+ecount);
		System.out.println("Count of odd : "+ocount);
	}
	
	
}