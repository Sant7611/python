
# 3. Abstract Classes (Enforcing a Contract)
# Real-world use case: Creating pluggable systems where multiple classes must guarantee they have the same methods (like different database connectors or payment gateways).

# The Scenario: A notification service that can send alerts via different channels.
# The Task:
# Import ABC and abstractmethod.
# Create an abstract base class called NotificationProvider with an abstract method send_message(user, message).
# Create two subclasses: EmailNotifier and SMSNotifier.
# If a developer tries to instantiate an EmailNotifier without implementing the send_message method, Python should throw an error. Implement the methods to just print "Sending Email to [user]: [message]" (and similarly for SMS).

from abc import ABC, abstractmethod

class NotificationProvider(ABC):

    @abstractmethod
    def send_message(self,user,message):
        pass


class EmailNotifier(NotificationProvider):

    def __init__(self, user, message):
        self.user = user
        self.message = message

    def send_message(self):
        return f'sending Email to {self.user}: {self.message}'
    
emailNotifier = EmailNotifier('santosh', 'hello sir! great to have you.')
print(emailNotifier.send_message())