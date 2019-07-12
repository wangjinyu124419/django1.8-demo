class Parent():
    name = 'parent'

    def getName(self):
        print(self.name)
    def __init__(self):
        print self.name

    # class child:
    #     def getName(self):
    #         return parent.name


if __name__ == '__main__':
    child = Parent()
