class ProductOfNumbers:

    def __init__(self):
        self.prefix = []

    def add(self, num: int) -> None:
        if num == 0:
            self.prefix = []
            return

        size = len(self.prefix)
        if size == 0:
            self.prefix.append(num)
        else:
            self.prefix.append(num * self.prefix[-1])

    def getProduct(self, k: int) -> int:
        size = len(self.prefix)
        if k > size:
            return 0
        elif k == size:
            return self.prefix[-1]
        return self.prefix[-1] // self.prefix[-k - 1]


# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)

def main():


if __name__ == "__main__":
    main()
