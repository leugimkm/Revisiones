"""AyudaEnPython: https://www.facebook.com/groups/ayudapython
"""
NOT_ALLOWED = "!\"#$%&\\\'()*+,-./:;<=>?@[]^_`{|}~©®°¦±¼½¾"


def sol(s: str) -> str:
    return "".join(c for c in s if c not in NOT_ALLOWED)


def main():
    print(sol(input("Entrada: ")))


if __name__ == "__main__":
    main()
