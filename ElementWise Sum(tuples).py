
def tuple_elementwise_sum(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        return "Input tuples must have same length."
    result=tuple(a+b for a,b in zip(tuple1,tuple2))
    return result
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
print(tuple_elementwise_sum(tuple1, tuple2))