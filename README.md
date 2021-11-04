Lab 7

Problem
Write a program which, given a number, simulates rolling a pair of six-sided dice that number of times. The program should keep track of how many times each possible sum comes up using a list. The list's first element should contain how many times a total of 2 was rolled, the second should contain how many times a total of 3 was rolled, and so on all the way through to 12. When all rolls are complete, the program should output the resulting list as well as a chart as shown in the example below, where the number of asterisks represents the number of times that roll came up (results will vary with each run). In this example, the user requested the dice be rolled 100 times:

Resulting list: [2, 8, 11, 11, 15, 15, 17, 9, 7, 4, 1]                                       

Resulting chart: 

2   **                                                                                                           
3   ********                                                                                                     
4   ***********                                                                                                  
5   ***********                                                                                                  
6   ***************                                                                                              
7   ***************                                                                                              
8   *****************                                                                                            
9   *********                                                                                                    
10  *******                                                                                                      
11  ****                                                                                                         
12  *   
Input validation: Do not accept a non-integer input for the number of dice rolls to simulate.

Instructions
Create a new Python file and place intro comments using the template below.
Use comments to write the algorithm your program will follow, including functions.
Write the Python code corresponding to each of your algorithm's steps.
Commit and push changes and check your repository on github.com to confirm your updates before leaving lab (even if not finished).

Note: This lab does not require a flowchart or test cases.

Intro comments template
# Programmers: [your names]
# Course: CS151, Dr. Rajeev 
# Date:
# Lab Number:
# Program Inputs: [What information do you request from the user?]
# Program Outputs: [What information do you display for the user?]
Function decomposition
Your program should have a function for each of the following tasks. Practice iterative development: implement each item according to the instructions section below and then test that your code still works before proceeding onto the next item.

A function get_number_of_rolls that asks the user for the number of rolls and returns it as an integer. If the user enters a non-integer input, the function should output an error and ask again until a valid input is given (hint: use the isdigit string method.)
A function roll_dice that returns an integer representing the result (sum) of rolling two dice. Import the random module at the top of your program and use the call random.randint(1, 6) to simulate a single six-sided dice.
A function create_histogram that, given an integer number of rolls to simulate, returns a histogram represented as a list of 11 elements with the count of each roll result (i.e. the element at index zero contains the number of times 2 came up, the element at index 1 contains the number of times 3 came up, and so on. See the "Resulting list" in the example above.
A function print_histogram that, given a histogram represented as a list of 11 elements, displays the "Resulting chart histogram to the console as in the example above. Use the "\t" character to print a tab after each number in the line so the asterisks appear aligned.
A main function to drive the program.
Submission
One submission per team including all member names.

GitHub: Completed .py file (including intro and algorithm comments).
