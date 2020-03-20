#PF-Assgn-3
#This verification is based on string match.

# mileage=12
# amount_per_litre=72
# distance_one_way=102
# per_head_cost=0
# divisible_by_five=False


mileage=12
amount_per_litre=65
distance_one_way=96
per_head_cost=0
divisible_by_five=False

#Start writing your code from here
#Populate the variables: per_head_cost and divisible_by_five
distance_two_way=distance_one_way*2
total_fuel_required=distance_two_way/mileage
total_fuel_amount=total_fuel_required*amount_per_litre
if total_fuel_amount%4==0:
    divisible_by_five=True
else:
    divisible_by_five=False

per_head_cost=total_fuel_amount/4

    # TODO: write code...

#Do not modify the below print statements for verification to work
print(per_head_cost)
print(divisible_by_five)
