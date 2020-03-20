// #The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
// #Rate per Adult: Rs. 37550.0
// #Rate per Child: 1/3rd of the rate per adult
// #Service Tax: 7% of the ticket amount (including all passengers)
// #As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
// #Find and display the total ticket cost for a group which had adults and children.
//PF-Exer-8
//This verification is based on string match.

package main
import ("fmt")
func main(){
    var finalFee float32
    //Write your program logic here
    //Populate the variable: finalFee
    var course_fee float32=25000
    var extra_fee float32=1500
    var marks float32=50
    var percentage float32=(marks/2)/100
    var scholarship_amount float32= percentage*course_fee
    finalFee=course_fee-scholarship_amount+extra_fee
     //Do not modify the below print statement for verification to work
     fmt.Println(finalFee)
}
