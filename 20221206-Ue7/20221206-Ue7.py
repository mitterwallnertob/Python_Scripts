# Hey, we're going on a camping trip!!

camping_list = ["tent", "sleeping bags", "water", "raspberry pi", "coffee", "knife", "ethernet cable", "flash drive", "beard oil", "marshmallows"]

# In a list we can store all types of data mixed together (not to compare with an array)
camp_site = ["Crystal Lake", 404, 89.3, True]


# There's the possibility of negative indexing, so
# you = camping_list[9] is the same as you = camping_list[-1]
# -1 is the first element of the list seen from the reverse (there's no -0)

me = camping_list[4]
you = camping_list[9]

print(me)
print(you)


# We can add stuff to the list through using the method .append()
# With this method we can only add one piece of data at a time
# camping_list.append("toilet paper")
# camping_list.append("bidet")

# To add more than one item we can use the method .extend()
camping_list.extend(["toilet paper", "bidet"])

# Or we could simply use following code
# camping_list = camping_list + ["toilet paper", "bidet"]

# If we want to add an item to the very beginning (index 0) of the list i can use following method
# camping_list.insert(0, "bidet")

# If we wanted to add "toilet paper" to the second to last position we need to use following method with negative index
# camping_list.insert(-1, "toilet paper")

# there's a difference between the inserting and printing method --> negative 1 (-1) means second to last position when inserting data to a list!

print(camping_list)


# We can delete stuff from the list through using the method .remove()
# With this method we can just delet one piece of data at a time
# camping_list.remove("sleeping bags")
# camping_list.remove("tent")

# Or we could use the method .pop() but we need to use the index of the element in the list
# camping_list.pop(0)
# If we are rerunning the same command the inizes moves further so right now, item at position 0 is "tent"
# after executing camping_list.pop(0) it gets deleted and "sleeping bags" is at position 0
