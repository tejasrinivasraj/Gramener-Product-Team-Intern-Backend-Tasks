list1 = list(map(int, input().strip().split()))
list2 = list(map(int, input().strip().split()))
list1 = set(list1)
list2 = set(list2)
ans=[]
for i in list1:
    if(i in list2):
        continue;
    else:
        ans.append(i);
print("Element in List 1 that are not present in List 2:", ans);
