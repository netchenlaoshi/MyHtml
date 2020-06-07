for cock in range(5,101,5):   # 公鸡
    for hen in range(3,101 - cock,3):  #母鸡
        for chick in range(1,101 - cock - hen): #小鸡
            if cock // 5 + hen // 3 + chick * 3 == 100 and cock + hen + chick == 100:
                print("公鸡有%d只\t母鸡有%d只\t小鸡有%d只" % (cock // 5, hen // 3, chick * 3))
