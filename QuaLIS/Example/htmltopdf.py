kk=[1,2,4,6,-1]
kkk=[1,3]
j=0
kkk_len=len(kkk)
diff=len(kk)-len(kkk)
print(diff)
for i in range(len(kk)):
    # print(kk[i])
    if kk[i]==kkk[j]:
        print("The common characters are:",kk[i])
        j=j+1
        if j==len(kkk):
            print("kkk max count reached")
            j=kkk_len-1
            # break
    else:
        print("The Missing number is",kk[i])