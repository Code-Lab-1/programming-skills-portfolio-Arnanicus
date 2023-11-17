names = ["Buzz Lightyear","Dwayne Johnson","Railey Inductivo"]
print(names[0],",I would like to invite you to dinner.")
print(names[1],",I would like to invite you to dinner.")
print(names[2],",I would like to invite you to dinner.\n")
print("Unfortunately, Buzz Lightyear will not be able to come.\n")

del(names[0])
names.insert(0,"Vin Diesel")

print(names[0],",I would like to invite you to dinner.")
print(names[1],",I would like to invite you to dinner.")
print(names[2],",I would like to invite you to dinner.")

print("\nThere is more space available. We shall invite more people.\n")
names.insert(0,'Carlo Vicente')
names.insert(2,'Barack Obama')
names.append('Queen Elizabeth')

print(names[0],'I would like you to come to dinner.')
print(names[1],'I would like you to come to dinner.')
print(names[2],'I would like you to come to dinner.')
print(names[3],'I would like you to come to dinner.')
print(names[4],'I would like you to come to dinner.')

print("\nNevermind. We'll be short on time and there isn't any space. Strictly two people are permitted.\n")

oops = names.pop()
print(oops.title(),",with deepest regret you are no longer invited.")
oops = names.pop()
print(oops.title(),",with deepest regret you are no longer invited.")
oops = names.pop()
print(oops.title(),",with deepest regret you are no longer invited.")
print(names[0],'I would like you to come to dinner.')
print(names[1],'I would like you to come to dinner.')

del(names[0:3])
print(names)