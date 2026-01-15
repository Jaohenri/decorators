"""Different implementations of functions that receive a list of strings
as a parameter and display how many of them start with an uppercase letter.
"""

from func_time import func_time


@func_time
def starts_with_uppercase1(texts: list[str]) -> None:
    """Counts and prints how many strings start with an uppercase letter.

    Strategy:
        Directly compares the first character with its uppercase version
        using a for loop.
    """

    counter = 0
    for text in texts:
        if text[0] == text[0].upper():
            counter += 1

    print(counter)


@func_time
def starts_with_uppercase2(texts: list[str]) -> None:
    """Counts and prints how many strings start with an uppercase letter.
    
    Strategy:
        Uses ASCII values (A-Z correspond to 65-90).
    """

    counter = 0
    for text in texts:
        if 65 <= ord(text[0]) <= 90:
            counter += 1

    print(counter)


@func_time
def starts_with_uppercase3(texts: list[str]) -> None:
    """Counts and prints how many strings start with an uppercase letter.
    
    Strategy:
        Uses the str.isupper() method.
    """

    counter = 0
    for text in texts:
        if text[0].isupper():
            counter += 1

    print(counter)


@func_time
def starts_with_uppercase4(texts: list[str]) -> None:
    """Counts and prints how many strings start with an uppercase letter.
    
    Strategy:
        Uses list comprehension and the sum() function.
    """
    print(sum(1 for t in texts if t[0].isupper()))


@func_time
def starts_with_uppercase5(texts: list[str]) -> None:
    """Counts and prints how many strings start with an uppercase letter.
    
    Strategy:
        Uses the filter() function.
    """
    print(len(list(filter(lambda t: t[0].isupper(), texts))))


@func_time
def starts_with_uppercase6(texts: list[str]) -> None:
    """Counts and prints how many strings start with an uppercase letter.
    
    Strategy:
        Uses the map() function.
    """
    print(sum(map(lambda t: 1 if t[0].isupper() else 0, texts)))


if __name__ == '__main__':
    test_strings = [
        "Banana", "orange", "Dog", "cat", "Elephant",
        "tiger", "Pineapple", "strawberry", "Grape", "pear",
        "Car", "bicycle", "Motorcycle", "airplane", "Train",
        "boat", "Ship", "canoe", "Fish", "Shark",
        "Dolphin", "Macaw", "parrot", "Falcon", "eagle",
        "Gorilla", "monkey", "Horse", "Zebra", "lion",
        "Giraffe", "hippopotamus", "Rhinoceros", "Ant",
        "bee", "Butterfly", "scorpion", "Snake",
        "Alligator", "lizard", "Turtle", "Wolf", "bear",
        "Fox", "frog", "Duck", "Rooster", "hen",
        "Cow", "ox", "Pig", "sheep", "Lamb",
        "Strawberry", "Watermelon", "Peach", "kiwi", "Raspberry",
        "Tomato", "Pepper", "Mango", "Starfruit", "Coconut",
        "Blackberry", "Cherry", "Lemon", "Papaya", "Jabuticaba",
        "Pine nut", "Cassava", "Onion", "Garlic", "Chayote",
        "Pumpkin", "Beetroot", "Lettuce", "Kale", "Spinach",
        "Eggplant", "Cabbage", "Radish", "Ginger", "Cucumber",
        "Bell pepper", "Broccoli", "Okra", "Jilo", "Maxixe",
        "Turnip", "Taro", "Pea", "Soursop", "Surinam cherry",
        "Lychee", "Guarana", "Date", "Mandarin", "Walnut",
        "Chestnut", "Almond", "Hazelnut", "Pistachio", "Macadamia",
        "Parsley", "Coriander", "Basil", "Oregano", "Rosemary",
        "Thyme", "Bay leaf", "Green onion", "Mint", "Sage",
        "Cinnamon", "Clove", "Nutmeg", "Anise", "Cardamom",
        "Fennel", "Mustard", "Paprika", "Cumin", "Guava"
    ]

    starts_with_uppercase1(test_strings * 100000)
    starts_with_uppercase2(test_strings * 100000)
    starts_with_uppercase3(test_strings * 100000)
    starts_with_uppercase4(test_strings * 100000)
    starts_with_uppercase5(test_strings * 100000)
    starts_with_uppercase6(test_strings * 100000)
