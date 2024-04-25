class ParentClass1(object):
    def feature_1(self):
        print("Feature 1 is from ParentClass1")


class ParentClass2(object):
    def feature_2(self):
        print("Feature 2 is from ParentClass2")


# Multiple Inheritance
class ChildClass(ParentClass1, ParentClass2):
    def call_features(self):
        # Accessing features using super()
        super().feature_1()
        super().feature_2()


# Creating an instance of ChildClass
child_instance = ChildClass()

# Calling the method to see the MRO
child_instance.call_features()

# Checking the MRO
print(ChildClass.__mro__)
