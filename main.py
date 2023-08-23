"""Calculate blackjack winnings."""
import re


def main() -> None:
    amount = 0
    with open("history.txt", "r") as f:
        lines = f.readlines()
        # find lines matching <number>\t<number>
        for line in lines:
            if re.match(r"\d+\t\d+", line):
                print(line)
                # split line into two numbers
                numbers = line.split("\t")
                # add the second number to amount
                amount += float(numbers[1].strip())

    print(amount)


if __name__ == "__main__":
    main()
