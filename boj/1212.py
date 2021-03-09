"""
    1212. 8진수 2진수
"""
def run():
    def get_octal():
        return int(input(), 8)
    
    def convert_to_binary():
        return bin(octal)
    
    octal = get_octal()

    print(convert_to_binary()[2:]) # print(f'{int(input(), 8):b}')

if __name__ == "__main__":
    run()