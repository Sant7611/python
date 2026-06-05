from random import randint

class Train:
    company = 'Nepali Railway'

    def __init__(self, trainNo):
        self.trainNo = trainNo


    def book_ticket(self, fro, to):
        print(f" Your ticket has been booked. Train No: {self.trainNo} from {fro} to {to}")

    def get_status(self):
        print(f"sir {self.trainNo}, Your ticket has been successfully booked. ")
       

    def get_fare_information(self, fro, to):
        print(f"The price for your fare is: {randint(222,555)} from {fro} to {to}")


t = Train(12345)

t.book_ticket('ktm', 'baitadi')
t.get_status()
t.get_fare_information('ktm',  'baitadi')