class Usuario:
    def __init__(self, name, email, message):
        self._name = name
        self._email = email
        self._message = message
 
    @property
    def name(self):
        return self._name
 
    @name.setter
    def name(self, new_name):
        self._name = new_name
 
    @property
    def email(self):
        return self._email
 
    @email.setter
    def email(self, new_email):
        self._edad = new_email
 
    @property
    def message(self):
        return self._message
 
    @message.setter
    def message(self, new_message):
        self._message = new_message
 
