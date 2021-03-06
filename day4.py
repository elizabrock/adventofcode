import hashlib

class Day4:
    @classmethod
    def find_n_for_key(self, key, trailing_zeros):
        i = -1
        result = ''
        while not result.startswith('0'*trailing_zeros):
            i += 1
            value = "{0}{1}".format(key, i)
            result = hashlib.md5(bytes(value, 'utf-8')).hexdigest()
        return i

if __name__ == "__main__":
    result = Day4.find_n_for_key('yzbqklnj', 5)
    print("The hash salt for part 1 is {0}".format(result))
    result = Day4.find_n_for_key('yzbqklnj', 6)
    print("The hash salt for part 2 is {0}".format(result))