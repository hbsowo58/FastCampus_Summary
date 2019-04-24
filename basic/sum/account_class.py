class Account:
    # 생성자(constructor)
    # 객체를 생성할때, "반드시" 한번 호출한다
    def __init__(self, cust_name, init_balance):
        #인스턴스 멤버(객체가 가지는 속성,데이터,변수)를 설정한다
        self.name=cust_name
        self.balance=init_balance
        
    #소멸자 (destructor)
    #객체가 소멸될 때 '반드시' 한번 호출
    def __del__(self):
        pass
    
    #인스턴스 메서드(기능, 행동)
    def deposit(self, money):
        if money <0:
            return False
        
        # 관련 있는 변수를 :인스턴스멤버
        self.balance+=money
        return True
    
    def withdraw(self, money):
        if money > self.balance:
            return 0
        
        self.balance -= money
        return money
    
    def transfer(self, other, money):
        self.balance -= money
        #다른 객체의 멤버에 바로 접근하지 않는다
        #다른 객체의 데이터를 변경할 떄는
        # "반드시" 상대 객체가 가진 메서드에 맡겨야 한다!!
        # 메시지 패싱
        # other.money+=money 돈에 직접가면안댐
        other.deposit(money)