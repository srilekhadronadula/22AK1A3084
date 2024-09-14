a_real=float(input("enter the real part of the first complex number:"))
a_imag=float(input("enter the imaginary part of first complex number:"))
b_real=float(input("enter the real part of the second complex number:" ))
b_imag=float(input("enter the imaginary part of the second number"))
add_real=a_real+b_real
add_imag=a_imag+b_imag
sub_real=a_real-b_real
sub_imag=a_imag-b_imag
mul_real=a_real*b_real-a_imag*b_imag
mul_imag=a_real*b_imag+a_imag*b_real
conj_real=a_real
conj_imag=a_imag
print(f"addition:{add_real}+{add_imag}")
print(f"subtraction:{sub_real}+{sub_imag}")
print(f"multiplication:{mul_real}+{mul_imag}")

print(f"conjugate of the first number :{conj_real}+{conj_imag}i")





