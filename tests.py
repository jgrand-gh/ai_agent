from functions.get_files_info import get_files_info

def main():
    result = get_files_info("calculator", ".")
    print("Testing for 'calculator' and '.':")
    print(result + "\n")

    result = get_files_info("calculator", "pkg")
    print("Testing for 'calculator' and 'pkg':")
    print(result + "\n")

    result = get_files_info("calculator", "/bin")
    print("Testing for 'calculator' and '/bin':")
    print(result + "\n")

    result = get_files_info("calculator", "../")
    print("Testing for 'calculator' and '../':")
    print(result + "\n")

if __name__ == "__main__":
    main()