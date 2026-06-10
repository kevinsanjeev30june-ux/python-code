# Zip , list comphrehension, dict comprehension
# Zip elements of two lists

s1 = {1,2,3}
s2 = {'b','a','c'}
s3 = list(zip(s1,s2))
print(s3,"\n")

# Zip elements of two lists 
# print elements one by one ,but elements of 2nd list will be in reverse order

list1 = [10,20,30,40]
list2 = [100,200,300,400]

for x,y in zip(list1,list2[::-1]):
    print(x,y)

# Zip into dictionary
stocks = ['Reliance', ' Infosys', 'BSNL']
prices = [2145,4300,1678]

new_dict = {stocks: prices for stocks,
            prices in zip(stocks,prices)}
print(new_dict)

# find out name of students who got more than 50 using dict comprehension
scores ={
    "ALICE": 49,
    "DAVID": 43,
    "KEVIN": 56
}
result_pass ={
    name:("Pass" if score >= 50 else"fail")for name ,score in scores.items()

}
print(result_pass)