"""
Use this to create Person class
 @author
 @version
"""
# pylint: disable-msg=C0103


class Person:

    def __init__(self, first_name, middle_name, last_name, second_last_name=None):
        if first_name == "":
            raise Exception(" Must have valid first name")

        if last_name == "":
            raise Exception(" Must have valid last name")

        if second_last_name == "":
            second_last_name = None

        self.first_name = first_name
        self.middle_name = middle_name
        self.last_name = last_name
        self.second_last_name = second_last_name

    def __str__(self):

        if self.second_last_name is None:
            return "{} {} {}".format(self.first_name, self.middle_name,
                                     self.last_name)
        else:
            return "{} {} {}-{}".format(self.first_name, self.middle_name,
                                        self.last_name, self.second_last_name)

    def __eq__(self, other):
        # print("Calling equality check with {} == {}".format(id(self), id(other)))
        if self.last_name != other.last_name:
            return False
        if self.second_last_name != other.second_last_name:
            return False
        if self.first_name != other.first_name:
            return False
        if self.middle_name != other.middle_name:
            return False

        return True

    def __lt__(self, other):

        if not isinstance(other, Person):
            print(str(other) + " is not a Person instance")
            return False

        if self.last_name < other.last_name:
            return True
        elif self.last_name == other.last_name:
            if self.second_last_name == other.second_last_name:
                if self.first_name < other.first_name:
                    return True
                elif self.first_name == other.first_name:
                    return self.middle_name < other.middle_name
            elif self.second_last_name is not None and other.second_last_name is not None:
                if self.second_last_name < other.second_last_name:
                    return True
            elif self.second_last_name is None and other.second_last_name is not None:
                return True

        return False

