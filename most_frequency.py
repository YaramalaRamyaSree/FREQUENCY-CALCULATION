def My_frequency(st):
    s=dict()
    for kt in set(st):
        count=0
        for loop in range(len(st)):
            if kt in st:
                st.remove(kt)
                count+=1
        s[count,kt]=kt+" = "+str(count)
    for l in sorted(s.keys(),reverse=True):
        print(s[l])
st=list(input("Enter the string : "))
My_frequency(st)


output:
Enter the string : mississippi
s = 4
i = 4
p = 2
m = 1
