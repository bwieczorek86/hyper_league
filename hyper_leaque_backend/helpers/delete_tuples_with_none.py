def delete_tuples_from_list(tuple_list):
    new_tuple_list = []
    for tuples in tuple_list:
        for ele in tuples:
            if isinstance(ele[0], int) and isinstance(ele[1], int) and ele[0] is not ele[1]:
                new_tuple_list.append(ele)
    return new_tuple_list
