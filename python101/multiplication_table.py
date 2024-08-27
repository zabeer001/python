def multiplication_table(e):
    #print(e,type(e))
    for i in range(1,11):
        #print(e,'x',i,'=',e*i)
        #print(f'{e} x {i} = {e * i}')
        print('{} X {} = {}'.format(e,i,e*i))
x = int(input('enter the number: '))
multiplication_table(x)