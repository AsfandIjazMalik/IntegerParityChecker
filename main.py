# Function to take input from the user and determine if the number is even or odd
def taking_input():
    while True:
        try:
            # Prompting the user for input
            number = int(input('Enter a number to determine if it is "EVEN" or "ODD": '))
            
            # Check if the number is greater than 0
            if number == 0:
                print('Sorry, please enter a number greater than 0.\n')
            elif number > 0:
                # Determine if the number is even or odd
                if number % 2 == 0:
                    print(f'{number} is an "EVEN" number.')
                else:
                    print(f'{number} is an "ODD" number.')
                break  # Exit the loop if valid input is provided
        except ValueError:
            # Handle invalid inputs (e.g., non-integer inputs)
            print('\n1. Please enter a positive integer.\n'
                  '2. For example: 2, 5, or any other number greater than 0.\n'
                  '3. Please avoid entering letters or words.\n')

# Call the input function for the first time
taking_input()

# Loop to allow the user to check more numbers or exit the program
while True:
    # Prompting the user for further action
    more_task = input('\nEnter "Yes" to check another number or "No" to exit (Yes or No): ').lower()
    
    if more_task in ('yes', 'y'):
        # Call the function again to check another number
        taking_input()
    elif more_task in ('no', 'n'):
        # Exit the program
        print('\nYou have exited the program.\nSee you next time!\nTHANK YOU!')
        break
    else:
        # Handle invalid responses
        print('\nSorry Compiler Can not Understand Please enter "Yes" or "No".')