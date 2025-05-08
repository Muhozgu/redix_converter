#Base
# print('Enter the number that you want to convert')
# value = input()
# print(f'Thank you for Entering {value}')

# step 01 : Find the binary
      # we have to create a function
      # we have to create a loop that will divide each dividend to get the remainder

def to_binary(figure):
    result_before = []
    result_after_a = []
    dividend = int(figure // 2)
    for d in range(dividend):
        result_before.append(d + 1)
    #result_after which will only contain the last value of result_before
    result_after = result_before[len(result_before) - 1]
    print(result_before)
    print(result_after)
    result_after_a.append(result_after)
    print(result_after_a)
to_binary(20)