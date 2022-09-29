#ivedamas balas
# 0 - negali buti
# 1 - 3 neigiamas
# 4 - 6 patenkinamas
# 7 - 9 geras
# 10 - labai geras
# visais kitais atvejais - reikia akinuku

sk = int(input('sk = '))
salyga1 = ( sk>=1 and sk<=3)
salyga2 = ( sk>=4 and sk<=6)
salyga3 = ( sk>=7 and sk<=9)
salyga4 = ( sk==10)
salyga5 = (sk==0)

if salyga5 :
    print('negali buti')
elif salyga1 :
    print('neigiamas')
elif salyga2 :
    print('patenkinamas')
elif salyga3 :
    print('geras')
elif salyga4 :
    print('labai geras')
else:
    print('reikia akiniu')