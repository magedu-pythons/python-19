def gencode(num:int = 200,length:int = 5):
    '''
    num is the number of generated code,
    length is the length of each code,should be greater than 5.
    '''
    import random
    if length < 5:
        print('Length should be greater than 5!')
        return

    rec = {}
    gent_from = list(range(97,97+26))+list(range(65,65+26))+list(range(48,48+10))
    count = 1
    
    while count <= num: 
        one = bytearray(b'0')*length

        for i,v in enumerate(random.choices(gent_from,k=length)):
            one[i] = v
        one = one.decode(encoding='utf-8')

        if rec.get(one,0) == 0:
            rec[one] = 1
            count += 1
        else:
            continue
            
    return tuple(rec.keys())




gencode()




