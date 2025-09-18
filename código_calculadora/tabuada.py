import os
while True:
    number = int(input('Quer ver a tabuada de qual valor? (Aperte -1 para sair!): '))
    if number < 0:
        break

    os.system('cls')
    
    print('-'*30)
    for c in range(1, 11):
        print(f'{number} x {c:2} = {number * c:2}')

    print('-'*30)
print('FIM DO PROGRAMA!')









