string1 = "Hello "
string2 = "Aparna"
string3 = ", welcome to Python programming"

# Concatenate all three strings using the + operator
result = string1 + string2 + string3

print(result)
#2  H e l l o   A p a  r  n  a  ,  w e l c  o m e t o P y t h o n   p r o g r a m m i n g
print(result[0])
print(result[-1])
print(result[0:6])
print(result[-1])
print(result[-11::])
print(result[::-1])
print(result[-18:-12])
#3
strM="Python Beginner tutorial"
print(strM.upper())
print(strM.lower())
print(strM.capitalize())
count_t = strM.count('t')
print("Total occurrences of 't':", count_t)
print(strM.replace("Python", "Machine Learning"))
#Tuples
tuple1=(10,20,30)
tuple2=(40,50,60)
t_combine = tuple1 + tuple2
print(t_combine)
t_repeated = t_combine * 3
print("Repeated 3 times:", t_repeated)
third_element = t_combine[2]
print("3rd element:", third_element)
first_three = t_combine[:3]
print("First 3 elements:", first_three)
last_three = t_combine[-3:]
print("Last 3 elements:", last_three)



