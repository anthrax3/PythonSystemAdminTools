class Person(object):
    '''This class is a person class holding values of first name, 
    last name, email and skills '''

    def __init__(self, first_name, last_name, email, skills):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.skills = skills

    def get_firstname(self):
        '''This method prints out the first name'''
        print self.first_name

    def get_lastname(self):
        '''This method prints out the last name'''
        print self.last_name

    def set_email(self, email):
        '''This method sets the objects email'''
        self.email = email

    def get_email(self):
        '''This method returns the objects email'''
        return self.email

    def get_all(self):
        '''This method prints all of the objects attributes'''
        print self.first_name
        print self.last_name
        print self.email
        print self.skills
