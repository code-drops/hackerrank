/*

You are given two classes, Person and Student, where Person is the base class and Student is the derived class. Completed code for Person and a declaration for Student are provided for you in the editor. Observe that Student inherits all the properties of Person.

Complete the Student class by writing the following:

A Student class constructor, which has 4 parameters:
A string, firstName.
A string, lastName.
An integer, id.
An integer array (or vector) of test scores, scores.
A char calculate() method that calculates a Student object's average and returns the grade character representative of their calculated average:
O - 90<=a<=100
E - 80<=a<90
A - 70<=a<80
P - 55<=a<70
D - 40<=a<55
T - 40<a

*/
import java.util.*;
class Person {
	protected String firstName;
	protected String lastName;
	protected int idNumber;
	
	// Constructor
	Person(String firstName, String lastName, int identification){
		this.firstName = firstName;
		this.lastName = lastName;
		this.idNumber = identification;
	}
	
	// Print person data
	public void printPerson(){
		 System.out.println(
				"Name: " + lastName + ", " + firstName 
			+ 	"\nID: " + idNumber); 
	}
	 
}

class Student extends Person{
	private int[] testscores;
    Student(String firstName,String lastName,int id,int[] scores){
        super(firstName,lastName,id);
        testscores = new int[scores.length];
        for(int i=0;i<scores.length;i++){
            testscores[i] = scores[i];
        }
    }
    char calculate(){
        int average = 0;
        int sum = 0;
        for(int i=0;i<testscores.length;i++){
            sum += testscores[i];
        }
        average = sum/testscores.length;
        if(average<=100 && average>=90){
            return 'O';
        }
        else if(average<90 && average>=80){
            return 'E';
        }
        else if(average<80 && average>=70){
            return 'A';
        }
        else if(average<70 && average>=55){
            return 'P';
        }
        else if(average<55 && average>=40){
            return 'D';
        }
        else{
            return 'T';
        }
    }
}

class Solution {
	public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		String firstName = scan.next();
		String lastName = scan.next();
		int id = scan.nextInt();
		int numScores = scan.nextInt();
		int[] testScores = new int[numScores];
		for(int i = 0; i < numScores; i++){
			testScores[i] = scan.nextInt();
		}
		scan.close();
		
		Student s = new Student(firstName, lastName, id, testScores);
		s.printPerson();
		System.out.println("Grade: " + s.calculate());
	}
}
