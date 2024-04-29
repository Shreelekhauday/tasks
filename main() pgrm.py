#main() pgrm
from atm import ATM
def main():
    atm=ATM()
    print('press ')
    while True:
        print('1 for balance check \n2 for withdraw \n3 for deposit \n4 to Exit')
        choice=int(input('Enter your choice: '))
        if choice==1:
            username=input('Enter your username: ')
            atm.balance(username)
        elif choice==2:
            username=input('Enter your username: ')
            amount=int(input('Enter your amount: '))
            atm.withdraw(username,amount)
        elif choice==3:
            username=input('Enter your username: ')
            amount=int(input('Enter your amount: '))
            atm.deposit(username,amount)
        elif choice==4:
            print('thank you for visiting the ATM!!!!')
            break
        else:
            print('invalid input please try again')

print(main())