capital_city={"Nepal":"Kathmandu","Italy":"Rome"}#create dictionary
print(capital_city)
capital_city={"Nepal":"Kathmandu","English":"London"}#Add elements
print("Initial Dictionary:",capital_city)
capital_city["Japan"]="Tokyo"
print("Updated Dictionary:",capital_city)
student_id={111:"Eric",112:"Kyle",113:"Butters"}#change value
print("initial dictionary:",student_id)
student_id[112]="stan"
print("Updated Dictionary",student_id)
student_id={111:"Eric",112:"Kyle",113:"Butters"}#Access Elements
print(student_id[111])
print(student_id[113])
student_id={111:"Eric",112:"Kyle",113:"Butters"}
print("initial dictionary:",student_id)#Remove Elements
del student_id[111]
print("Updated Dictionary",student_id)
squares={1:1,3:9,5:25,7:49,9:81}#iterating through dictionary
for  i in squares:
    print(squares[i])
thisdict={ #copy a Dictionary
    "brand":"Ford","model":"Mustang","year":1964
}
mydict=thisdict.copy
print(mydict)




