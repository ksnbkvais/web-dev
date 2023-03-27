#In Python, a string can be split on a delimiter.

def split_and_join(line):
    line = line.split()
    return '-'.join(line)
    # write your code here

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
