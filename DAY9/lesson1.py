# create dictionary {key:value}

programming_dictionary = {
    "Bug":"An error in a program that prevents the program from as expected",
    "Function": "A piece of code that you can easily call over and over again."
    }

#retrieving items from dictionary
#print(programming_dictionary["Bug"])


#adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."

#create empty dictionary
empty_dictionary = {}

#wipe an existing dictionary
##programming_dictionary = {}


#edit an item in a dictionary
programming_dictionary["Bug"] = "A moth in your computer"

#Loop through a dictionary

for key in programming_dictionary:
    print(key+": "+programming_dictionary[key])


