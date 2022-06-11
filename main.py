import random


try:
    import pyperclip
except ImportError:
    pass


def main():
    """Run the Spongetext program."""
    print('''sPoNgEcAsE, bY aSianCarT''')

    spongetext = englishToSpongecase(input('> '))
    print()
    print(spongetext)

    try:
        pyperclip.copy(spongetext)
        print('(cOpIed SpOnGeTexT to ClIpbOaRd.)')
    except:
        pass


def englishToSpongecase(message):
    """Return the spongetext form of the given string."""
    spongetext = ''
    useUpper = False

    for character in message:
        if not character.isalpha():
            spongetext += character
            continue

        if useUpper:
            spongetext += character.upper()
        else:
            spongetext += character.lower()

        if random.randint(1,100)<= 90:
            useUpper = not useUpper

    return spongetext


if __name__ == '__main__':
    main()