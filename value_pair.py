# function valuePair(obj1, obj2, key) {
#     let val1 = obj1[key];
#     let val2 = obj2[key];
#     const arr = [val1, val2];

#     return arr;
# }

def value_pair(obj1, obj2, key):
    val1 = obj1[key]
    val2 = obj2[key]
    li = [val1, val2]

    return li


print(value_pair('fish', 'cat', 'food'))

# CODE DOESNT WORK, i dont really understand what the javascript code is doing
