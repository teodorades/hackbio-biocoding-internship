**Topics Covered**: Coding Syntax, Data types and Data Structures 

**Project title**: Organised the given information (Names, Emails..etc) about the team members 

**Description**: The script uses a dictionary to store team member information. Each key in the dictionary corresponds to a specific information (Names, Emails, Hobbies, etc.), and the values are strings containing comma-separated data for each team member.
To make the data easier to access and manipulate:
      * The .split(", ") method is used to divide the comma-separated strings into lists.
      * The .join(", ") method is used to bring list items back into strings for printing all team members'information.

Therfore, the script has two main functionalities:
      * Print information for all team members.
      * Print information for a single team member by accessing specific index in the lists.

We considered using slicing (for example for Names: print(Names[0:5])) for printing of all information, but using .join() was looked more elegant.

**Result:** The script uses dictionary, and allows you to print dictionary stored information for all team members or for a single team member.

