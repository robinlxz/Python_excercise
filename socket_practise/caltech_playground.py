### lecture_2 Class
class Challenge:
    """This class stores challenges"""

    def __init__(self, name: str, passion, eta, stress):
        """Initialize a Challenge"""
        self.name = name
        self.motive = {
            'passion': passion,
            'stress': stress
        }
        self.eta = eta

    def show_challenge(self):
        print(
            f'This is a {self.name}, hope to be conquered in {self.eta} days.')

    def __repr__(self):
        return self.name


### Lecture 2 handle error

# try:
#     a = 1 / 0
# # except ZeroDivisionError:
# except EOFError:
#     print('EOF Error message, lxz')
# except ZeroDivisionError:
#     print('cannot divide by zero')

# print('continue')


### Lecture 2 Define and raise exceptions
# class LxzException(BaseException):
#     def __init__(self, msg='lxz exception init msg'):
#         self.msg = msg
#     def __repr__(self):
#         return str(self.msg)

# def some_function(x):
#     if x < 0:
#         raise LxzException('x is smaller than 0!')

# # some_function(-5)
# try:
# #     some_function(-5)
#     1/0
# except LxzException:
#     print('exception happens')
# except ZeroDivisionError:
#     print('Zero Division Error happens')
# # except:
# #     print('other error, bad practise')


