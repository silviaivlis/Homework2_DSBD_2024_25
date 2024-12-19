class RegisterUserCommand:
    def __init__(self, email, ticker, requestId, highValue, lowValue):
        self.email = email
        self.ticker = ticker
        self.requestId = requestId
        self.highValue = highValue
        self.lowValue = lowValue

class UpdateTickerCommand:
    def __init__(self, email, ticker, requestId):
        self.email = email
        self.ticker = ticker
        self.requestId = requestId

class UpdateValuesCommand:
    def __init__(self, email, requestId, highValue, lowValue):
        self.email = email
        self.requestId = requestId
        self.highValue = highValue
        self.lowValue = lowValue

class DeleteUserCommand:
    def __init__(self, email, requestId):
        self.email = email
        self.requestId = requestId

class GetLatestValueQuery:
    def __init__(self, email):
        self.email = email

class CalcAverageValueQuery:
    def __init__(self, email, count):
        self.email = email
        self.count = count