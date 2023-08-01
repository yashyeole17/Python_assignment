#21_01010

pattern = ['1', '0', '1', '1', '0', '1', '0', '1', '0', '1']
i = 0
for row_count in range(1,5):
    for i in range(row_count):
        print(pattern[i],end=' ')
        i += 1
        if i >= len(pattern):
            break
    print()
