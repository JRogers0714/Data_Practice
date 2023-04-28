# the kata wants me to be able to take two inputs and see if the second matches the end of the first.

def solution(pt_one, pt_two):

    suf = pt_one.endswith(pt_one)

    result: bool = False

    if pt_two == suf:
        result = True
        print(result)
    else:
        print(result)


#  input_one = input("Type any string")
#   input_two = input("Type any string")

print(solution(pt_one=input("Type any string: "), pt_two=input("Type any string: ")))

# def solution(pt_one, pt_two):

#   result: bool = False
#    for x in pt_one:
#    for y in pt_two:
#         if x == y:
#              result = True
#               return result
# return result

# print(result)


#  print(solution(pt_one=input("Type any string..."), pt_two=input("Type any string...")))
