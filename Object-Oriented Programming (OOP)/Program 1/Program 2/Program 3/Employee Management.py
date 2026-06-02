class Employee:
    def work(self):
        print("Employee Working")

class Manager(Employee):
    def manage(self):
        print("Managing Team")

m = Manager()

m.work()
m.manage()