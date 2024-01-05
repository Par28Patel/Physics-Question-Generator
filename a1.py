# Name : Parth Patel

# The purpose of this program is to ask the user different types of physics questions 
# from 2 different physics units, in order to allow them to get more practice in physics.
# The problem at hand from my life is that I find there is an inadequate amount of practice
# questions given for each unit in physics class. Thus I want to create a program which 
# generates a physics question for the user based on what unit they would like, asks for the
# users answer, and compares the users answer to the answer which it calculates. If the 
# answer is correct, the program congratulates the user on getting it right and ends the 
# program. However, if the user gets it wrong the program will ask the user another 
# question in the same unit, and continue doing this until the user provides a correct answer.
# This ensures the user will get enough practice until they are able to correctly answer that
# type of question. This program will consist of 2 different units and 3 total different types
# of questions. 

# Importing math and random libraries 
import math
import random

# This function is for solving for the magnitude of the distance vector
def dis_mag(vec1x, vec1y, vec1z, vec2x, vec2y, vec2z):
    # Find the net distance between the 2 vectors by subtracting 
    net_vec = vec_sub(vec2x, vec2y, vec2z, vec1x, vec1y, vec1z)
    
    # Add up the squares of all values and squareroot it 
    vec_magnitude = math.sqrt((net_vec[0]**2)+(net_vec[1]**2)+(net_vec[2]**2))
    return vec_magnitude

# This function is for solving for the distance unit vector
def unit_vector (mag, vec1x, vec1y, vec1z, vec2x, vec2y, vec2z):
    # Find the net distance between the 2 vectors by subtracting
    net_vec = vec_sub(vec2x, vec2y, vec2z, vec1x, vec1y, vec1z)

    # Calculate the unit vector component for x, y and z
    unitvecx = (net_vec[0])/mag
    unitvecy = (net_vec[1])/mag
    unitvecz = (net_vec[2])/mag

    return (unitvecx, unitvecy, unitvecz)

# This function is for solving vector addition
def vec_add(x1, y1, z1, x2, y2, z2):
    x_tot = x1 + x2
    y_tot = y1 + y2
    z_tot = z1 + z2
    # Return the total x, y and z components
    return [x_tot, y_tot, z_tot]

# This function is for solving vector subtraction
def vec_sub(x1, y1, z1, x2, y2, z2):
    x_tot = x1 - x2
    y_tot = y1 - y2
    z_tot = z1 - z2
    # Return the total x, y and z components
    return [x_tot, y_tot, z_tot]

# This function is to check if the answer the user gets matches the correct answer
def correct_answer(answer):

    # Checking for the correct answer if the unit was vectors 
    if unit_type == 'vector':
        print ('Format the answer like so:')
        print ('<x, y, z>')
        print ('')
        user_answ = input('What is the answer you got for this question?: ')
        print ('')

        # Right answer will return the Boolean value True and a wrong answer will return False
        if user_answ == answer:
            return True
        else:
            return False 

    # Checking for the correct answer if the unit was gravity
    if unit_type == 'gravity':
        print ('Format the answer in scientific notation like so:')
        print ('The answer: <1000, 0, 0.0001> would be formatted like the following:')
        print ('<1.00e03, 0.00e00, 1.00e-03>')
        print ('Remember to round off to 2 decimal places.')
        print ('')
        user_answ = input('What is the answer you got for this question?: ')
        print ('')

        if user_answ == answer:
            return True
        else:
            return False

# This function is for asking and solving one of 2 questions from the vectors unit  
def u_vectors():

    # Creating empty list which will contain the values of the vector after being added or subtracted
    final_vec = []

    print ('')
    print ('You have chosen to solve a vectors question!')
    
    # Loops if the user gets the question wrong 
    while ut_stopper != 3:

        # While statement which keeps asking for an input on invalid inputs 
        while ut_stopper != 2:
            # Asking user if they want to do vector addition or subtraction
            print ('To solve a vector addition question, please type \'addition\'')
            print ('To solve a vector subtraction question, please type \'subtraction\'')
            vec_type = input('What type of vector question would you like?: ')
            print ('')

            # If the input is 'addition' or 'subtraction', loop stops  
            if (vec_type == 'addition') or (vec_type == 'subtraction'):
                break
            
            # If the input is not 'addition' or 'subtraction', ask for a valid input
            else:
                print (f'{vec_type} is not a valid input, please enter one of the listed inputs.')
                print ('')
        
        # Generating x, y and z components of the first vector 
        xvec_1 = random.randint(-1000000,1000000)
        yvec_1 = random.randint(-1000000,1000000)
        zvec_1 = random.randint(-1000000,1000000)

        # Generating x, y and z components of the second vector
        xvec_2 = random.randint(-1000000,1000000)
        yvec_2 = random.randint(-1000000,1000000)
        zvec_2 = random.randint(-1000000,1000000)

        # Passes the variables above as arguments to the function for vector addition
        if vec_type == 'addition':
            # Presents the user with the question
            print (f'<{xvec_1}, {yvec_1}, {zvec_1}> + <{xvec_2}, {yvec_2}, {zvec_2}>')

            # Places the returned values into a list called final_vec
            final_vec = vec_add(xvec_1, yvec_1, zvec_1, xvec_2, yvec_2, zvec_2)

        # Passes the inputs above as arguments to the function for vector subtraction
        elif vec_type == 'subtraction':
            # Presents the user with the question
            print (f'<{xvec_1}, {yvec_1}, {zvec_1}> - <{xvec_2}, {yvec_2}, {zvec_2}>')

            # Places the returned values into a list called final_vec
            final_vec =  vec_sub(xvec_1, yvec_1, zvec_1, xvec_2, yvec_2, zvec_2)

        # Checking if the user got the same answer
        formatted_ans = f'<{final_vec[0]}, {final_vec[1]}, {final_vec[2]}>' 
        
        # Breaking the loop and printing nice message for correct answer
        if correct_answer(formatted_ans) == True:
            print ('Nice job! Thats the correct answer!')
            break
        
        # Printing message notifying user of incorrect answer 
        else:
            print ('Sorry, thats incorrect!')
            print (f'The answer is: <{final_vec[0]}, {final_vec[1]}, {final_vec[2]}>')
            print ('Here is another question from the same unit!')
            print ('')

# This function is for asking and solving the question from the gravity unit  
def u_gforce():

    print ('')
    print ('You have chosen to solve a gravitational force question!')
    print ('')

    # Loops if the user gets the question wrong 
    while ut_stopper != 3:

        # Generating the mass and location of the object exerting the force 
        mass1 = random.randint(10,1000000)
        xvec_1 = random.randint(-1000000,1000000)
        yvec_1 = random.randint(-1000000,1000000)
        zvec_1 = random.randint(-1000000,1000000)

        # Generating the mass and location of the object the force is being exerted on
        mass2 = random.randint(10,1000000)
        xvec_2 = random.randint(-1000000,1000000)
        yvec_2 = random.randint(-1000000,1000000)
        zvec_2 = random.randint(-1000000,1000000)

        # Printing the question
        print ('There are 2 objects floating in space. Calculate the gravitational force ')
        print (f'an object with the mass of {mass1}kg at location <{xvec_1},{yvec_1},{zvec_1}> ')
        print (f'exerts on an object with the mass of {mass2}kg at location <{xvec_2},{yvec_2},{zvec_2}>')
        print ('')

        # Calculating the magnitude of the distance vector 
        r_mag = dis_mag(xvec_1, yvec_1, zvec_1, xvec_2, yvec_2, zvec_2)

        # Calculating the distance unit vector
        r_hat = unit_vector(r_mag, xvec_1, yvec_1, zvec_1, xvec_2, yvec_2, zvec_2)

        # Calculating for the gravitational force 
        F_grav_part1 = (-6.7*10**-11)*(mass1)*(mass2)/(r_mag**2)
        F_grav_x = F_grav_part1*(r_hat[0])
        F_grav_y = F_grav_part1*(r_hat[1])
        F_grav_z = F_grav_part1*(r_hat[2])

        # Formatting final x, y and z vectors into scientific notation 
        gravx_final = "{:.2e}".format(F_grav_x)
        gravy_final = "{:.2e}".format(F_grav_y)
        gravz_final = "{:.2e}".format(F_grav_z)

        # Checking if the user got the same answer 
        formatted_ans = f'<{gravx_final}, {gravy_final}, {gravz_final}>'

        # Breaking the loop and printing nice message for correct answer
        if correct_answer(formatted_ans) == True:
            print ('Nice job! Thats the correct answer!')
            break
        
        # Printing message notifying user of incorrect answer
        else:
            print ('Sorry, thats incorrect!')
            print (f'The answer is: <{gravx_final}, {gravy_final}, {gravz_final}>')
            print ('Here is another question from the same unit!')
            print ('') 

# Main block
if __name__ == "__main__":
    # Variable stopping the while loop asking for user input 
    ut_stopper = 0

    # Print statement welcoming the user to the program
    print ('*****************************************************************************')
    print ('Hello, welcome to the 6th generation Physics Help Yeilder, or PHY6 for short!')
    print ('')

    # While condition which keeps asking the user for an input until a valid input is given
    while ut_stopper != 1:

        # Print statements displaying the users options 
        print ('To solve a question in the vectors unit, please type: \'vector\'')
        print ('To solve a question in the gravitational force unit, please type: \'gravity\'')

        # Input prompting the user to enter the unit they would like to check a question for  
        unit_type = input("Please enter the desired unit you would like to solve for: ")
        print ('')

        # If statement comparing user input to the string 'vector'
        # If the users input matches 'vector', the program will call on the vector unit function
        if unit_type == 'vector':
            u_vectors()
            # Loop stops 
            ut_stopper = 1

        # If statement comparing user input to the string 'gravity'
        # If the users input matches 'gravity', the program will call on the gravity unit function
        elif unit_type == 'gravity':
            u_gforce()
            # Loop stops
            ut_stopper = 1
        
        # If the input matches none of the desired inputs, the loop will not end
        else:
            # User will recieve a message to enter a valid input 
            print (f'{unit_type} is not a valid input, please enter one of the listed inputs.')
            print ('')