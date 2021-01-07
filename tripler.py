# function tripler(array) {
#   const arr = [];

#   for ( i = 0; i < array.length; i += 1) {
#     let num = array[i];
#     arr.push(num * 3);
#   }

#   return arr;
# }

def tripler(list):
    result = []

    for i in range(len(list)):
        num = list[i]
        result.append(num * 3)

    return result


print(tripler([2, 3, 4]))
