import os
def main():
    old = "hello.zip"
    index = old.find('.')
    print(index)
    print(old[:index])
    new = old[:index] + "(" + "1" + ")" + old[index:]
    print(new)  

if __name__ == "__main__":
    main()
