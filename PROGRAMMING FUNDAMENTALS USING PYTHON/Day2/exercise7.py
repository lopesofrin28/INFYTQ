#The flight ticket rates for a round-trip (Mumbai->Dubai) were as follows:
#Rate per Adult: Rs. 37550.0
#Rate per Child: 1/3rd of the rate per adult
#Service Tax: 7% of the ticket amount (including all passengers)
#As it was a holiday season, the airline also offered 10% discount on the final ticket cost (after inclusion of the service tax).
#Find and display the total ticket cost for a group which had adults and children.

#PF-Exer-7

def calculate_total_ticket_cost(no_of_adults, no_of_children):
    total_ticket_cost=0
    #Write your logic here
    ticket_cost=(37550.0*no_of_adults)+(no_of_children*(1/3*37550))
    service_tax=ticket_cost*7/100
    cost_after_taxes=ticket_cost+service_tax
    discount=cost_after_taxes*10/100

    total_ticket_cost=(ticket_cost+service_tax)-discount

    return total_ticket_cost


#Provide different values for no_of_adults, no_of_children and test your program
total_ticket_cost=calculate_total_ticket_cost(1,2)
print("Total Ticket Cost:",total_ticket_cost)
