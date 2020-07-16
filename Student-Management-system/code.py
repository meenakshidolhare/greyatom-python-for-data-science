# --------------
class_1=['Geoffrey Hinton','Andrew Ng','Sebastian Raschka','Yoshua Bengio']
class_2=['Hilary Mason','Carla Gentry','Corinna Cortes']
new_class=class_1+class_2
new_class
new_class.append('Peter Warden')
new_class
new_class.remove('Carla Gentry')
new_class
courses={'Maths':65,'English':70,'History':80,'French':70,'Science':60}
courses_values=courses.values()
courses_values
Total=sum(courses_values)
Total
percentage=Total/500*100
percentage
Mathematics={'Geoffrey Hinton':78,'Andrew Ng':95,'Sebastian Raschka':65,'Yoshua Benjio':50
,'Hilary Mason':70,'Corinna Cortes':66,'Peter Warden':75}
max_marks=max(Mathematics.values())
max_marks 
for key, value in Mathematics.items(): 
    if value == max_marks: 
        topper=key 

print(topper)
split_topper=topper.split()
split_topper
First_Name=split_topper[0]
First_Name
Last_Name=split_topper[1]
Last_Name
Full_Name=(Last_Name+' '+First_Name)
certificate_name=Full_Name.upper()
certificate_name




