
class Customer:

    def __init__(self, customerId=None, name=None, email=None, password=None, address=None, contact=None):
        self.__customerId = customerId
        self.__customerName = name
        self.__customerEmail = email
        self.__customerPassword = password
        self.__customerAddress = address
        self.__customerContact = contact

    def setCustomerId(self, customerId):
        self.__customerId = customerId

    def getCustomerId(self):
        return self.__customerId

    def setCustomerName(self, customerName):
        self.__customerName = customerName

    def getCustomerName(self):
        return self.__customerName

    def setCustomerEmail(self, customerEmail):
        self.__customerEmail = customerEmail

    def getCustomerEmail(self):
        return self.__customerEmail

    def setCustomerPassword(self, customerPassword):
        self.__customerPassword = customerPassword

    def getCustomerPassword(self):
        return self.__customerPassword

    def setCustomerAddress(self, customerAddress):
        self.__customerAddress = customerAddress

    def getCustomerAddress(self):
        return self.__customerAddress

    def setCustomerContact(self, customerContact):
        self.__customerContact = customerContact

    def getCustomerContact(self):
        return self.__customerContact


class Food:

    def __init__(self, foodId=None, name=None, quantity=None, price=None):
        self.__foodId = foodId
        self.__foodName = name
        self.__foodQuantity = quantity
        self.__foodPrice = price

    def setFoodId(self, foodId):
        self.__foodId = foodId

    def getFoodId(self):
        return self.__foodId

    def setFoodName(self, foodName):
        self.__foodName = foodName

    def getFoodName(self):
        return self.__foodName

    def setFoodQuantity(self, foodQuantity):
        self.__foodQuantity = foodQuantity

    def getFoodQuantity(self):
        return self.__foodQuantity

    def setFoodPrice(self, foodPrice):
        self.__foodPrice = foodPrice

    def getFoodPrice(self):
        return self.__foodPrice


class Order:

    def __init__(self, orderId=None, customerId=None, foodId=None, quantity=None, bill=None, date=None):
        self.__orderId = orderId
        self.__customerId = customerId
        self.__foodId = foodId
        self.__quantity = quantity
        self.__bill = bill
        self.__orderdate = date

    def setOrderId(self, orderId):
        self.__orderId = orderId

    def getOrderId(self):
        return self.__orderId

    def setCustomerId(self, customerId):
        self.__customerId = customerId

    def getCustomerId(self):
        return self.__customerId

    def setFoodId(self, foodId):
        self.__foodId = foodId

    def getFoodId(self):
        return self.__foodId

    def setQuantity(self, quantity):
        self.__quantity = quantity

    def getQuantity(self):
        return self.__quantity

    def setBill(self, bill):
        self.__bill = bill

    def getBill(self):
        return self.__bill

    def setDate(self, date):
        self.__date = date

    def getDate(self):
        return self.__date
