#list
animals = ['monkey','panda','lion']
print(animals)

#access list element
print('\n')
print(animals[1])

#ordered list
print('\n')
animal1 = ['monkey','panda','lion']
animal2 = ['monkey','lion','panda']
print(animals==animal1)
print(animals==animal2)

#list slicing
print('\n')
print(animals[0:])
print(animals[:])
print(animals[1:2])
print(animals[:1])
print(animals[::2])

#list constructor
print('\n')
languages = list(('telugu','hindi','english'))
print(languages)

#list operators
print('\n')
#repetition
repeat = animals*2
print(repeat)
print('\n')
#concatination
concatinate = animals+languages
print(concatinate)
print('\n')
#length
print(len(animals))
print('\n')
#iteration
for animal in animals:
    print(animal)

print('\n')
#membership
print('panda' in animals)
print('tiger' in animals)

#list built-in functions
print('\n')
#min
print(min(animals))
#max 
print(max(animals)) 
#append
languages.append('tamil') 
print(languages)
#extend
animals.extend(languages)
print(animals) 
#insert
animals.insert(1,'tiger') 
print(animals)
#remove
animals.remove('panda') 
print(animals)
#sort
languages.sort() 
print(languages)
languages.sort(reverse=True)
print(languages)
#count
lion_count = animals.count('lion')
print(lion_count)
#copy
languages_copy = languages.copy()
print(languages_copy)
#reverse
languages.reverse()
print(languages)

#Dictionary
doctors = {'Name':'Raju', 'Doctors_ID':438, 'Department':'Cardiology'}
print(doctors)

#access the item
print('\n')
print(doctors['Name'])

#change value
print('\n')
doctors['Doctors_ID'] = 444
print(doctors)

#add item
print('\n')
doctors['cases'] = 3
print(doctors)

#length of dictionary
print('\n')
print(len(doctors))

#dictionary built-in functions
print('\n')
#items
print(doctors.items())
print('\n')
#copy
doctors_copy = doctors.copy()
print(doctors_copy)
print('\n')
#get
name = doctors.get('Name')
print(name)
print('\n')
#key
print(doctors.keys())
print('\n')
#values
print(doctors.values())
print('\n')
#pop
doctors.pop('cases')
print(doctors)
print('\n')
#fromkeys
y = 0
print(doctors_copy.fromkeys(doctors_copy, y))
print('\n')
#clear
print(doctors.clear())