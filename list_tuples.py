#making of list(stores multiple values seprated by comma)

marks=[12,114,15,54,45]

#print the list
print(marks)

#to check the type
print(type(marks))

#to access the values and check length
print(marks[0])
print(len(marks))

#can also store diffrent type of values in a list(we have to store a student information)

info = ["Aryan" , "Jind" , 111 , 7]
print(info)

#can change the data

info[2] = 222

print(info)

#list_slicing(list_name[starting_idx : ending inx]) ending is not included

num = [1,2,3,4,5]

print(num[1:4])

#if we miss the starting index it starts from the zero, likewise if we miss the last index it will go the end or take last index as ending index

#negative indexing
print(num[-3:-1])

#list methods

list = [1, 2, 3]

list.append(4) #adds one element at the last
print(list)

list.sort() #sort in ascending order

list.sort(reverse = True) #sort in descending order
print(list)

list.reverse() #reverse the array
print(list)

list.insert(4, 5) #insert element at particular index list.insert(idx, el)
print(list)

list.remove(1) #remove the value
list.pop(1) #remove from the index
print(list)


#tuples(same as list but tuples are immutable)

tuple = (1, 2, 3, 4, 3, 2, 1)
print(tuple)
print(type(tuple))
print(tuple[0])

#tuple[0] = 2 , we cant change the values

#empty tuple
tup = ()
print(tup)

#if we have to keep one item in our tupple we have to seprate it with comma
tup = (1,)
print(tup)

#slicing works same as lists

#tuple methods

print(tuple.index(4)) #return the index of first occurance
print(tuple.count(3)) #count total occurance of that element 


#Que : Ask user thier three movies and store them into list
movies = []
mov1 = input("Movie 1 : ")
movies.append(mov1)
mov2 = input("Movie 2 : ")
movies.append(mov2)
mov3 = input("Movie 3 : ")
movies.append(mov3)
print(movies)