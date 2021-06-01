def breakChunks(list, chunk):
    result_list = []
    chunk_list = []

    for i in list:
        chunk_list.append(i)
    
        if len(chunk_list) == chunk:
            result_list.append(chunk_list)
            chunk_list = []

    if chunk_list:
        result_list.append(chunk_list)
    return result_list


chunks = breakChunks([11, 12, 46, 33, 88, 37, 63, 0, 87], 3)
print("List broken up into chunks:", chunks)
chunk_list2 = []

c1 = max(chunks[0])
print("Largest (local) element in chunck 1: ", c1)
chunk_list2.append(c1)

c2 = max(chunks[1])
print("Largest (local) element in chunck 2: ", c2)
chunk_list2.append(c2)

c3 = max(chunks[2])
print("Largest (local) element in chunck 3: ", c3)
chunk_list2.append(c3)

print("Largest (global) element in list: ", max(chunk_list2))