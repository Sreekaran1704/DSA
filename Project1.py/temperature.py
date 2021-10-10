temperature_Storing_Array=[]
sum=0
count=0
for i in range(int(input("How many Days Temperature : "))):
    temperature_Storing_Array.append(int(input(f"Enter Day {i+1} high temperature : ")))
for i in temperature_Storing_Array:
    sum+=i
result=sum/len(temperature_Storing_Array)
print(f"Average : {result} ")
for i in temperature_Storing_Array:
    if i>result:
        count+=1
print(f"{count} day(s) are above the average ")
