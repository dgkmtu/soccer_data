
def registerCsv(data):
    
    with open('result.csv', 'a', encoding='utf-8')as f:
        f.write(data[0])
        for i in range(1,10):
            f.write(',')
            f.write(data[i])
            
        f.write('\n')

    state = True

    return state
