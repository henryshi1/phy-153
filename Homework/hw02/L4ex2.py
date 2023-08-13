# Henry Shi
# L4ex2.py

# Task: print all elements in a list
vector = [1, 6, 34, 87];    # this is our list
print(vector);              # this prints the list but not each individual element

# the long way - BAD!
print(vector[0]);
print(vector[1]);
print(vector[2]);
print(vector[3]);

print('\n');

# using a loop - good (should print the same as above)
for component in vector:
    print(component);

# store list element as variable
x = vector[1];
print("x=" + str(x));                # should print x=6
