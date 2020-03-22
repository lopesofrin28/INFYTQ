#PF-Tryout

def find_new_salary(current_salary,job_level):
    # write your logic here
    hike=[(3,15),(4,7),(5,5)]

    for i in hike:
        if job_level in i:
            new_salary=(current_salary*(100+i[1]))//100
            return new_salary
        else:
            return current_salary

# provide different values for current_salary and job_level and test yor program
new_salary=find_new_salary(15000,3)
print(new_salary)
