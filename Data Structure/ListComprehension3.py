
#map And Filter Function to Comprehensive list

number = [1,2,3,4,5]
mapResult = [x*x for x in number]
print(mapResult)

filterResult = [x for x in number if x%2!=0]
print(filterResult)