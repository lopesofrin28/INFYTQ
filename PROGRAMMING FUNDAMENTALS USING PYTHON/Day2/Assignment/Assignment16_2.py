

def makeamount(rupees_to_make,no_of_five,no_of_one):
    five_needed=0
    one_needed=0
    five_needed=int(rupees_to_make/5)
    # print(five_needed)
    one_needed=rupees_to_make%5
    # print(one_needed)
    if five_needed<=no_of_five and one_needed<=no_of_one:
        print("No. of five needed:",five_needed)
        print("No. of one needed:",one_needed)
    elif five_needed>no_of_five:
        total=no_of_five*5
        one_needed=rupees_to_make-total
        if one_needed<=no_of_one:
            print("No. of five needed:",no_of_five)
            print("No. of one needed:",one_needed)
        else:
            print(-1)
    else:
        print(-1)


makeamount(20,3,5)
