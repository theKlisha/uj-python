class Bug:
    counter = 0

    def __init__(self) -> None:
        Bug.counter += 1
        self.id = self.counter
        pass

    def __del__(self) -> None:
        Bug.counter -= 1
        print("End: id: {}, counter: {}".format(self.id, self.counter))
        pass

    def __str__(self) -> str:
        return "id: {}, counter: {}".format(self.id, self.counter)

bugs = []
for i in range(100):
    bugs.append(Bug())
    print(bugs[-1])
