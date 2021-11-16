def print_array(arr):
    # if len(arr) == 1:
    #     return arr[0]
    return ','.join([str(i) for i in arr])


data = [2]
print(print_array(data), "2")

data = [2, 4, 5, 2]
print(print_array(data), "2,4,5,2")

data = [2, 4, 5, 2]
print(print_array(data), "2,4,5,2")

data = [2.0, 4.2, 5.1, 2.2]
print(print_array(data), "2.0,4.2,5.1,2.2")

data = ["2", "4", "5", "2"]
print(print_array(data), "2,4,5,2")

data = [True, False, False]
print(print_array(data), "True,False,False")

array1 = ["hello", "this", "is", "an", "array!"]
array2 = ["a", "b", "c", "d", "e!"]
data = array1 + array2
print(print_array(data), "hello,this,is,an,array!,a,b,c,d,e!")

array1 = ["hello", "this", "is", "an", "array!"]
array2 = [1, 2, 3, 4, 5]
data = [array1, array2]
print(print_array(data), "['hello', 'this', 'is', 'an', 'array!'],[1, 2, 3, 4, 5]")
