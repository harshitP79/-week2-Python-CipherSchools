def countlist(l):
    count = 0
    for i in l:
        if type(i)== list:
            count += 1
    print(count)
    
l=['123',['harshit'],['7654'],'panwar']
countlist(l)
