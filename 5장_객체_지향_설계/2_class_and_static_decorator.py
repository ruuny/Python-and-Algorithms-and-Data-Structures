class A(object):
    def foo(self, x):
        print(f"foo({self}, {x}) 실행")

    @classmethod
    def class_foo(cls, x):
        print(f"class_foo({cls}, {x}) 실행")
        
    @staticmethod
    def static_foo(x):
        print(f"static_foo({x}) 실행")

if __name__ == '__main__':
    a = A()
    a.foo(1)
    a.class_foo(2)
    A.class_foo(2)
    a.static_foo(3)
    A.static_foo(3)