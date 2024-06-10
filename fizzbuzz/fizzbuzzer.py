class FizzBuzzer():
    
    def fizzBuzz(self, zahl: int) -> str:
        if (zahl % 3 == 0 and zahl % 5 == 0): return "FIZZBUZZ"
        if (zahl % 3 == 0): return "FIZZ"
        if (zahl % 5 == 0): return "BUZZ"

        return str(zahl)
