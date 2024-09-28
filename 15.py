def p_e(input_string):
    words=input_string.split()
    even_length=[word for word in words if len(word%2)==0]
    print(' '.join(even_length))
input_string="the sum rises in the east"
p_e(input_string)