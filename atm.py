
class ATM:
    def __init__(self):
        self.user_data=self.load()
    def load(self):
        user_data={}
        with open("test.txt", "r") as file:
            for line in file:
                username, balance = line.strip().split(',')
                user_data[username] = float(balance)
        print(user_data)
        return user_data
    def update_data(self):
        f=open('test.txt','w')
        for a,b in self.user_data.items():
            f.write(str(a)+','+str(b)+'\n')

    def withdraw(self,username,amount):
        if username in self.user_data:
            if self.user_data[username]<amount:
                print('insufficient funds')
            else:
                self.user_data[username]-=amount
                print('The Available Amount is:',self.user_data[username])
                self.update_data()
    def deposit(self,username,amount):
        self.user_data[username]+=amount
        print('The Available Amount is:', self.user_data[username])
        self.update_data()
    def balance(self,username):
        print('The Available Amount is:', self.user_data[username])