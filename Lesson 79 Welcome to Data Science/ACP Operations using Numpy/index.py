import numpy as np

#Create an array consisting of linearly spaced elements between 0 to 9
original_array = np.linspace(0, 9, 10)
print("Original Array:", original_array)

#Replace all odd numbers in this array with -1 without modifying the original array
modified_array = np.where(original_array % 2 != 0, -1, original_array)
print("Modified Array (odd numbers replaced with -1):", modified_array)

#Create a new array that contains the original 1-dimensional array converted into a 2-dimensional array, with two rows
reshaped_array = original_array.reshape(2, -1)
print("Reshaped 2D Array:\n", reshaped_array)

#Iterate through the original array and find out the sum of all even numbers
sum_even = np.sum(original_array[original_array % 2 == 0])
print("Sum of all even numbers:", sum_even)