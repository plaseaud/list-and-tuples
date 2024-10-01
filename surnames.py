#Create a list using 10 usernames
surnames = ['canlas', 'pantaleon', 'cervania', 'cajis', 'chiu', 'capinpin', 'balaba', 'fangonil', 'dela cruz', 'rabino']
print (surnames)

#Add another 5 surnames
surnames.extend(['lalangan', 'corros', 'deveza', 'lim', 'manuel']) 
print (surnames)

#Add my surname
surnames.insert(0, 'enriquez')
print (surnames)

#Remove the last surname on the list
surnames.pop()
print (surnames)

#Sort the list alphanumerically
surnames.sort()
print (surnames)

#Sort the list in reverse
surnames.sort(reverse=True)
print (surnames)

#Convert the list into tuple
surnames_tuple = tuple(surnames)
print(type(surnames_tuple))

#Delete all items in the list
surnames.clear()
print(surnames)