def find_duplicates(datas):
    duplicates = []
    count = 0
    for i in range(len(datas)):
        for j in range(len(datas)):
            if i != j:
                if datas[i] == datas[j]:
                    if datas[i] not in duplicates:
                        duplicates.append(datas[i])
                        count += 1
                        # print('{0} and {1} are the same'.format(datas[i], datas[j]))
    if not duplicates:
        print('No duplicates')
    else:
        print(duplicates, '\nDuplicates Count:', count)
    return duplicates, count
