def test(lst):
    result={}
    for item in lst:
        result[item[0]]=item[1:]
    return result

student=[[1,'zaidi','z'],[2,'syed','z'],[3,'ali','zI'],[4,'ronaldo']]

print("\noriginal list of list:")
print(student)
print("\nconverted list to a distionary:")
print(test(student))