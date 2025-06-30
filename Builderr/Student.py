





class Student:
    #def getInstance(Self):
    #    return Student.Builder()
    
    def __init__(self,Builder):
        self._name = Builder.get_name()
        self._roll_no = Builder.get_roll_no()
        self._age = Builder.get_age()
        self._course =Builder.get_course()
        self._email =Builder.get_email()

    def __str__(self):
        return (f"Student(name='{self._name}', roll_no={self._roll_no}, "
            f"age={self._age}, course='{self._course}', email='{self._email}')")
    
    

    class Builder:
        def __init__(self):
            self._name ="Ayush"
            self._roll_no =10
            self._age = None
            self._course = None
            self._email = None

    # Getters
        def get_name(self):
            return self._name

        def get_roll_no(self):
            return self._roll_no

        def get_age(self):
            return self._age

        def get_course(self):
            return self._course

        def get_email(self):
            return self._email

    # Setters
        def set_name(self, name):
            self._name = name
            return self

        def set_age(self, age):
       
            self._age = age   
            return self

        def set_course(self, course):
            self._course = course
            return self

        def set_email(self, email):
            self._email = email
            return self

        def build(self):
            if self._age <= 10:
                raise ValueError("Age must be greater than 10")
            return Student(self)