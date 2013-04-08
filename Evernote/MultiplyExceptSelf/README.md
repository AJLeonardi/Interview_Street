Given a list of integers, your task is to write a program to output an integer-valued list of equal length such that the output element at index 'i' is the product of all input elements except for the input element at 'i'.
 
In other words, let inputArray by an integer array of length 'n'.  The solution,computed into outputArray, would be:
 
for each j from 1 to n-2:
               outputArr[ j ] = inputArray[0] * inputArray[1] * inputArray[2] * ... * inputArray[j-1] * inputArray[j+1] * inputArray[j+2] *...* inputArray[n-1]
for j = 0
               outputArray[0] = inputArray[1] * outputArray[2] * ... * outputArray[n-1]
for j = n-1
               outputArray[n-1] = outputArray[0] * outputArray[1] * outputArray[2] * ... * outputArray[n-2]        
 
As an example, if inputArray = { 1, 2, 3, 4 }, then
 
outputArray = { 2*3*4, 1*3*4, 1*2*4, 1*2*3 }.
 
Your program should run in O(n) time and should be space efficient.
 
Input format :
 
First line of input contains N , number of elements in list.
Next N lines will each contain an element (a signed integer)
 
Output format :
 
Print the output list of numbers.