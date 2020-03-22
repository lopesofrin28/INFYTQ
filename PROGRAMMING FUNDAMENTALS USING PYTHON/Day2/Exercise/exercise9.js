//PF-Exer-9

noOfFlightsTakeOff=100
noOfFlightsLanded=110
seatingCapacityTakeOff=150
seatingCapacityLanded=185
totalCookies=0

//Write your code here
//Populate the variable: totalCookies
total_cookies_sold_takeOff=noOfFlightsTakeOff*(seatingCapacityTakeOff*2)
// console.log(total_cookies_sold_takeOff)

total_cookies_sold_landing=noOfFlightsLanded*(seatingCapacityLanded/2)*2
// console.log(total_cookies_sold_landing)

totalCookies=total_cookies_sold_takeOff+total_cookies_sold_landing
//Do not modify the below print statement for verification to work
console.log(totalCookies)
