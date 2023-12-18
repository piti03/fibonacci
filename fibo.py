# The fibonacci code!
# To increase the range of calculation add the value of counter

def fibo():
    first_val = 1
    second_val = 1
    counter = 1
    result = 0
    while counter <= 50:
        result = first_val + second_val
        print(f'fibonacci stage -> {counter} : {result}')
        counter += 1
        first_val = second_val
        second_val = result
    print("=======================")   
fibo()      