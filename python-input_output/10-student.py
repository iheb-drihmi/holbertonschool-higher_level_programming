#!/usr/bin/python3
""" 9-student: class Student """


class Student:
    """
        class Student
        Attributes:
            first_name(str): first name of student
            last_name(str): last name of student
            age(int): age of student
    """
    def __init__(self, first_name, last_name, age):
        """
            initializes values for all instances of Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
            retrieves dict representation of instances
        """
        if isinstance(attrs, list) and all(
                isinstance(s, str) for s in attrs):
            return {el: getattr(self, el) for el in attrs if hasattr(self, el)}
        return self.__dict__
