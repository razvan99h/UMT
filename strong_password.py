import re


class Password:
    """
    Class for building a password and checking if it is strong
    """
    def __init__(self, given_password: str):
        """
        Constructs a Password object from a given password
        :param given_password: the given password
        """
        self.__password = given_password

    def __check_length(self, min_length: int, max_length: int) -> int:
        """
        Checks if the password has at least min_length characters and at most max_length characters
        :param min_length: the minimum required length of the password
        :param max_length: the maximum required length of the password
        :return: the number of changes to be made in order to pass the stated condition
        """
        if len(self.__password) < min_length:
            return min_length - len(self.__password)
        if len(self.__password) > max_length:
            return len(self.__password) - max_length
        return 0

    def __check_letters(self) -> int:
        """
        Check if the password contains at least one lowercase letter, at least one uppercase letter, and at least one digit.
        :return: the number of changes to be made in order to pass the stated condition
        """
        match_upper = int(not re.match(".*[A-Z].*", self.__password))
        match_lower = int(not re.match(".*[a-z].*", self.__password))
        match_digits = int(not re.match(".*[0-9].*", self.__password))
        return match_upper + match_lower + match_digits

    def __check_repeating(self) -> int:
        """
        Check if the password contains groups of three repeating characters in a row
        :return: the number of changes to be made in order to pass the stated condition
        """
        return len(re.findall(r"(.)\1{2}", self.__password))

    def check_strength(self) -> int:
        """
        Main algorithm that checks if the password is considered strong, based on the given conditions
        :return: the number of changes to be made in order to pass all the conditions
        """
        return self.__check_length(6, 20) + self.__check_letters() + self.__check_repeating()


if __name__ == '__main__':
    password = Password(input("Input password: "))
    # password = Password("aaaa1Bccc")
    changes = password.check_strength()
    if changes == 0:
        print("Password is strong enough!")
    else:
        print("Password is not strong enough. You have to make {0} changes to it!".format(changes))
