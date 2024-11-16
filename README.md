# IntegerParityChecker
Python Programming 
## Even Odd Number Identifier
This Python program helps the user determine whether a number is even or odd. It also provides functionality to check multiple numbers and handles invalid inputs with appropriate error messages. The program ensures the user enters a valid number greater than 0, with a loop to allow for repeated checks or exit the program. <br>
### Features<br>
•	Even/Odd Check: The program allows the user to enter a number and determines whether it is even or odd. <br>
•	Error Handling: The program gracefully handles invalid inputs (such as letters or non-numeric values). <br>
•	Repeated Checking: The user can check multiple numbers without restarting the program. <br>
•	Exit Option: The user can choose to exit the program after performing a check. <br>
### Usage<br>
1.	Run the Program: The program will prompt the user to input a number. <br>
2.	Even or Odd Check: After entering a valid number greater than 0, the program will output whether the number is even or odd. <br>
3.	Input Validation: If the user enters a non-integer or zero, the program will prompt the user to enter a valid positive integer. <br>
4.	Re-check Option: After checking one number, the user can choose to check another number or exit the program. <br>
### Features & Functionality Breakdown: <br>
•	User Input: Accepts numeric input from the user and checks whether it's even or odd. <br>
•	Validation: Ensures the user input is a positive integer. <br>
•	Repeated Checks: Allows users to perform multiple checks without restarting the program. <br>
•	Exit: Offers an exit option to stop the program at any time. <br>
### Python Concepts Used: <br>
### 1. Functions<br>
•	The program uses the taking_input() function to handle the user input, perform the check, and handle error scenarios. Functions allow for modular, reusable, and organized code. <br>
### 2. Loops<br>
•	The while loop is used to continuously prompt the user for valid input and allow them to perform multiple checks. The loop also allows the program to re-execute the input validation process if the user chooses to check another number. <br>
### 3. Conditional Statements<br>
•	if/elif/else statements are used to check whether the entered number is 0, positive, and even or odd. These conditionals determine the flow of the program based on the user's input. <br>
•	The program also uses conditionals to check if the user inputs "Yes" or "No" to continue or exit the program. <br>
### 4. Error Handling (Exception Handling) <br>
•	The program uses a try/except block to catch and handle invalid input, such as non-numeric values. When the user enters something that isn't an integer, a ValueError is raised, and the program asks the user to input a valid positive integer. <br>
### 5. String Methods<br>
•	The lower() method is used on the user's response (for checking whether they want to continue or exit) to ensure the input is case-insensitive (i.e., "yes", "YES", "y", "Y" will all work). <br>
### 6. List Methods<br>
•	While not explicitly demonstrated in this project, list methods could be used in future enhancements (e.g., storing a history of user inputs or responses). <br>
### 7. Input/Output<br>
•	The program makes extensive use of the input() function to get user input and print() to display results and prompts to the user. <br>
### Code Structure<br>
•	taking_input(): A function that prompts the user to enter a number and determines if it's even or odd. Handles input validation and repeats the process until valid input is provided. <br>
•	Main Loop: After checking a number, the program asks if the user wants to check another number or exit. If the user chooses to continue, the program prompts for the next input. <br>
