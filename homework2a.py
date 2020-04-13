"""Homework
    #Find 2 new problems on LeetCode and follow the communication steps covered in last class to guide your thinking and problem solving.
    #Write down and commit your communication steps (in code comments) and solution code to a GitHub repository.
    #Submit your GitHub repository to Gradescope.

PROBLEM #1

    Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
    An input string is valid if:
        Open brackets must be closed by the same type of brackets.
        Open brackets must be closed in the correct order.
        Note that an empty string is also considered valid.
"""


""" COMMUNICATION STEPS

Step 1 (Restate the problem)
    determine if the input strings match and are valid.

Step 2 (Ask clarifying questions)

    # Are nested inputs valid? for example: (({[]})) and ([])

Step 3 (State assumptions)

    # parenthesis that match are balanced.
    # If the parentheses dont match then they are unbalanced
    # Empty lists are Balanced

Step 4 (Brainstorm/ Think out loud)

    # Use a if/else statement nested inside of a for loop.
    # Use stack
    # Use a dictionary

Step 5 (Explain rationale)
    #Use Stack to keep track of opening brackets
    #Hash map to keep track of mappings and to improve code quality
    #Pop the top element from the stack it its not empty
    #else...assign dummy value
    #if elements dont match return false
    #if stack is empty then expression is valid

Step 6 (Tradeoffs)
    #fast and easy to understand code.

Step 7 (improvements)

    # Introduce different ways to solve the code and try to optimize the time complexity of it.

"""

"""CODE"""

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        # The stack to keep track of opening brackets.
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean.
        # Also makes adding more types of parenthesis easier
        mapping = {")": "(", "}": "{", "]": "["}

        # For every bracket in the expression.
        for char in s:

            # If the character is an closing bracket
            if char in mapping:

                # Pop the topmost element from the stack, if it is non empty
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket in our hash and the top
                # element of the stack don't match, return False
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket, simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, then we have a valid expression.
        # The stack won't be empty for cases like ((()
        return not stack






