from helpers import shout, area

def main() -> None:
    length = 5
    width = 8
    result = area(length, width)
    message = f"The area of a {length}-by-{width} rectangle is {result}."
    print(shout(message))

if __name__ == "__main__":
    main()

Run
python main.py