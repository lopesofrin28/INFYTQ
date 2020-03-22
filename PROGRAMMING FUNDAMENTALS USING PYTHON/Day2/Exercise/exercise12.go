// Write a Go program to find and display the maximum of three given numbers.
//
//
// Test your code by using the given sample inputs.
// Verify your code by using the 2nd sample input(highlighted) given below:
//
// Sample Input	       Expected Output
// Num1	Num2	Num3
// 1	    2	    3	       3
// 3	    4	    1	       ?
//




//PF-Exer-12
//This verification is based on string match.

package main
import ("fmt")
func main(){
    //Write your program logic here
    var num1 int=3
    var num2 int=4
    var num3 int=1
    if(num1>num2 && num1>num3){
        fmt.Println(num1)
    }else if(num2>num1 && num2>num3){
        fmt.Println(num2)
    }else{
        fmt.Println(num3)
    }
}
