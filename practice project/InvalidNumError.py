class InvalidNumError(Exception):
    def __init__(self,choice):
        self.ch = choice
    
    def __str__(self):
        data = str(self.ch)+" is Invalid input. Please enter valid integer value.."
        return data