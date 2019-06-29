
class BunchClass(dict):
    def __init__(self, *args, **kwds):
        super(BunchClass, self).__init__(*args, **kwds)
        self.__dict__ = self


def main():
    # 1) 딕셔너리 특수화
    bc = BunchClass  # ()가 없다.
    tree = bc(left=bc(left="Buffy", right="Angel"),
              right=bc(left="Willow", right="Xander"))
    print(tree)

    # 2) 일반 딕셔너리
    tree2 = dict(left=dict(left="Buffy", right="Angel"),
                 right=dict(left="Willow", right="Xander"))
    print(tree2)

if __name__ == "__main__":
    main()
