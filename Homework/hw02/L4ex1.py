# Henry Shi
# L4ex1.py

# Lists: most versatile data types
list1 = [2, 3, 5, 7, 11, 13];
# A list can contain elements of different types, unlike vectors or arrays
list2 = ['abcd', 9876, '4', 32];

# Accessing elements
a = list1[2];           # element of list1 at index 0
print(list1[2]);
print(a);               # should both print 5

b = list2[3];           # element of list2 at index 3
print(list2[3]);
print(b);               # should both print 32

# Adding lists
list = list1 + list2;   # joins the lists, with list1 before list2
print(list);
list = [0, 100, 2, 3] + list # update the value of list
print(list);

# Can create and initialize empty lists
new_vector = [];
print(new_vector);      # should print []

# sublists
l1 = list[:2];          # elements from the beginning to index 2
print(l1);              # should print [0, 100]
l2 = list[4:]           # elements from index 4 to the end
print(l2);              # should print everything after [0, 100, 2, 3
print (l1, l2)          # should print l1 and l2 as an ordered pair (l1, l2)
