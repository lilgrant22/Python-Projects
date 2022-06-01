"""
Use this to create Employee class
 @author
 @version
"""
# pylint: disable-msg=C0103


class Employee:
    def __init__(self, pay_rate):
        self.pay_rate = pay_rate

    def __str__(self):
        return "${:.02f}/hr".format(self.pay_rate)

    def get_pay(self, hours):
        if hours > 40:
            return self.pay_rate*(40 + 1.5*(hours-40))
        else:
            return self.pay_rate*hours

