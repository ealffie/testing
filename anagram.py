def number_needed(a, b):
    l1 = list(a)
    l2 = list(b)
    c = len(l2)
    count = 0

    for i in l1:
        if i in l2:
            count +=1
            l2.remove(i)
    l3 = len(l1)+c-(2*count)
    return l3


a = input().strip()
b = input().strip()


print(number_needed(a, b))
//
