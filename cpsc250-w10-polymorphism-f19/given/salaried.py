"""
Use this to create Salaried class
 @author
 @version
"""
# pylint: disable-msg=C0103

from given.employee import Employee

class Salaried(Employee):
    def __init__(self, pay_rate):
        Employee.__init__(self, pay_rate)

    def __str__(self):
        return "${:.02f}/period".format(self.pay_rate)

    def get_pay(self, hours):
        return self.pay_rate

