def solution(pt_one, pt_two):
    pt_one = input("Type any string...")
    pt_two = input("Type any string...")
    result = False
    for x in pt_one:
        for y in pt_two:
            if x == y:
                result = True
                return result

    return result


solution()
