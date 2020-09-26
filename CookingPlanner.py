# Purpose of this program is to be able to plan meals based on saved recipes

import pandas as pd

# Function to create recipes
def CreatingRecipe(name):
    # Getting the name of the recipe
    meal = input('\nOK, what is the name of the meal? \n')
            
    # Adding the ingredients of the recipe
    meal_item = ''
    ingredient = []
    while meal_item != 'end':
        meal_item = input('\nWrite down one ingredient and click enter. \nIf you have finish listing them write down end \n')
        if meal_item == 'end':
            pass
        else:
            ingredient.append(meal_item)

    # Adding the steps of the recipe
    meal_step = ''
    steps = []
    while meal_step != 'end':
        meal_step = input('\nWrite down each step and click enter. \nOnce you finish type end \n')
        if meal_step == 'end':
            pass
        else:
            steps.append(meal_step)
    data2 = [{'Recipe':meal, 'Ingredients':ingredient, 'Step':steps, 'Author':name}]    
    df2 = pd.DataFrame(data2)
    return df2

#Global variables
welcome_bool = True
menu1_bool = False
df = pd.DataFrame()

# Introduction to the program: 
# Users are asked to register their names
while welcome_bool == True :
    print('Welcome to the CookingPlanner')
    user_name = input('What is your name? \n')
    menu1_bool = True
    

    while menu1_bool == True:
        # Display menu1 with options:
        # a. Record a recipe
        # b. Look for a recipe
        # c. Return
        # d. Exit
        print('\nWhat would you like to do today', user_name, '?')
        user_answer = input('a. Record a recipe \nb. Look for a recipe \nc. Return \nd. Exit \n')

        if user_answer == 'a' or user_answer == 'A':
            df3 = CreatingRecipe(user_name)
            df = df.append(df3, ignore_index = True)


        elif user_answer == 'b' or user_answer == 'B':
            print('\nThe saved recipes are:\n')
            print(df.Recipe)
            chosen_rec = input('\nWhich recipe would you like to see?\n')
            for a in df.Recipe:
                if a == chosen_rec:
                    result_df = df.loc[df['Recipe'] == chosen_rec]
                    print(result_df)


        elif user_answer == 'c' or user_answer == 'C':
            print('You have selected c \n')
            menu1_bool = False


        elif user_answer == 'd' or user_answer == 'D':
            print('... Session succesfully ended \n\n')
            menu1_bool = False
            welcome_bool = False


        else:
            print('That is not a valid answer \n')
