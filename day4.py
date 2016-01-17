import hashlib

class Day4:
    @classmethod
    def find_n_for_key(self, key):
        i = -1
        result = ''
        while not result.startswith('00000'):
            i += 1
            value = "{0}{1}".format(key, i)
            result = hashlib.md5(bytes(value, 'utf-8')).hexdigest()
        return i

if __name__ == "__main__":
    result = Day4.find_n_for_key('yzbqklnj')
    print("The hash salt is {0}".format(result))