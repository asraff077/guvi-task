start_point=int(input("entert the start point = "))
ending_point=int(input("enter the end point = "))
if start_point <0 or start_point>ending_point:
    print("enter a valid range")
elif ending_point<start_point or ending_point>6:
    print("enter a valid range")
else:
    veichle=input("enter the veichle auto or cab = ")
    distance={1:0,2:7,3:10,4:15,5:18,6:25}
    d=distance[ending_point]- distance[start_point]
    if veichle=='auto':
        f=d*20
        print("the total fair is ",f)
    else:
        f=d*30
        print("the total fair is ",f)
    
