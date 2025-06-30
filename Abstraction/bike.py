numbers=[1,2,1,4,3,2,4]
A=[]
dist_num=list(filter(lambda x: x not in A and not A.append(x),numbers))
print(dist_num)
print("hi")