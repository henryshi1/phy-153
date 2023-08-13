# Henry Shi
# L4ex4.py

vector_idx = [0,1,2,3,4];        # list of vector indices
vector = [10,20,30,40,50];       # the vector itself
new_vector = [];                 # creates an empty list

for element in vector_idx:       # current index element is a variable
    print(element);              # print the current value of element
    print(vector[element]);      # print vector component corresp. to value of element
    new_vector.append(element+vector[element]); # append element+vector[element] to list new_vector
    new_vector.append(vector_idx[element]+vector[element]); # should append the same value since element == vector_idx[element]
    #append - method that adds element to end of list
    print(new_vector[element]);  # print the entry that was just added to new_vector

print(new_vector);               # print the array new_vector
