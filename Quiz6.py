'''Quiz) Make program to get the standard weight.

* standard weight: the proper weight for each individual's height.

(Gender-specific formulas)
 Male: height(m) x height (m) x 22
 Female: height(m) x height (m) x 21

Condition1: Standard weight must be calculate in function.
        * Name of function: std_weight
        * Argument value: height, gender
Condition2: Standard weight is displayed 2nd decimal number.

(Example output)
The male's standard weight is 67.38kg who is 175cm height.
'''
def std_weight(height, gender):
    height_cm = round(height*100)
    if gender == "Male":
        std_weight = round((height**2)*22, 2)
        return std_weight, gender, height_cm

    elif gender == "Female":
        std_weight = round((height**2)*21, 2)
        return std_weight, gender, height_cm
        
    else:
        print("Please check gender!")
    
std_weight, gender, height_cm=std_weight(1.75, "Male")

print("The {0}'s standard weight is {1}kg who is {2}cm height.".format(gender, std_weight, height_cm))