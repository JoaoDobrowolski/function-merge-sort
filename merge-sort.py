# Créditos ao usuário sarath joseph do stack overflow
# Essa é uma função semelhante à .sort() do python, porém utiliza o método Merge Sort, enquanto a .sort() utiliza Timsort. Ambas possuem complexidade 0(nlogn)
# O que se destaca é, por mais que seja muito compacta em relação as outras do mesmo tipo, possui muita simplicidade
# OBS1: Merge Sort utiliza a técnica divisão e conquista
# OBS2: Possui complexidade temporal melhor do que Buble Sort e Insertion Sort, que são 0(n²)
# Fique a vontade para usá-la como quiser :)

def merge_sort(list):
    if len(list) < 2:
        return list

    result = []
    mid = int(len(list)/2)

    y = merge_sort(list[:mid])
    z = merge_sort(list[mid:])

    while (len(y) > 0) and (len(z) > 0):
        if y[0] > z[0]:
            result.append(z.pop(0))
        else:
            result.append(y.pop(0))

    result.extend(y+z)
    return result
