import xml.dom.minidom as minidom

domtree=minidom.parse("grades.xml")
print(domtree)
group = domtree.documentElement
print(group)
students=group.getElementsByTagName('student')

#Updation
students[0].getElementsByTagName('name')[0].childNodes[0].data='Usman'
for student in students:
    #Printing
    print(f"Student Name is {student.getElementsByTagName('name')[0].childNodes[0].data}")
    print(f"Subject Name is {student.getElementsByTagName('subject')[0].childNodes[0].data}")
    print(f"Grade of this Student is {student.getElementsByTagName('grade')[0].childNodes[0].data}")

#Creating New Element
NewPerson=domtree.createElement('student')
name=domtree.createElement('name')
textnode=domtree.createTextNode('Ali')
name.appendChild(textnode)
NewPerson.appendChild(name)
group.appendChild(NewPerson)
#name = domtree.createElement()
domtree.writexml(open('grades.xml','w'))
