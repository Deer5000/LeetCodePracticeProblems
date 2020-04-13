""" Problem #2

Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2

"""




""" COMMUNICATION STEPS

Step 1 (Restate the problem)

    # Find the element in an array that appears the most.

Step 2 (Ask clarifying questions)

    # can the array have multiple datatypes?

Step 3 (State assumptions)

    # The array uses one datatype(numbers)
    #we are returning the element that appears the most.
    # There will always be a majority element in the array.

Step 4 (Brainstorm/ Think out loud)

    #Add a counter to count each element and return the element with the highest count.
    
Step 5 (Explain rationale)
    #The counter will count how many times each element occurs in an array.
    #The element with the highest count will be returned(printed)
Step 6 (Tradeoffs)

    #Great code quality and simple for users to understand and follow.

Step 7 (improvements)
    #Find a way to optimize the code and make it run faster.
"""


"""SOLUTION"""

def findMajority(arr, n): 
  
    maxCount = 0; 
    index = -1
    for i in range(n): 
      
        count = 0
        for j in range(n): 
          
            if(arr[i] == arr[j]): 
                count += 1

        if(count > maxCount): 
          
            maxCount = count 
            index = i 

    if (maxCount > n//2): 
        print(arr[index]) 
      
    else: 
        print("No Majority Element") 
  
if __name__ == "__main__": 
    arr = [2, 2, 3, 2, 4, 6, 2] 
    n = len(arr) 
      
    findMajority(arr, n) 


