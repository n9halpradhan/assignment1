print("Enter marks of two subjects: ")
S1=float(input())
S2=float(input())
S3=float(input())
S4=float(input())
S5=float(input())
avg=(S1+S2+S3+S4+S5)/5;
print("Average marks = ", avg)
if avg>=90:
    print("Grade O")
elif avg>=80:
    print("Grade E")
elif avg>=70:
    print("Grade A")
else:
    print("Grade B")