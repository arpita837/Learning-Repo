import sys
def main():
    # Check if there are at least two command-line arguments
    if len(sys.argv) >= 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        print("Argument 1:", arg1)
        print("Argument 2:", arg2)
    else:
        print("Please provide at least two command-line arguments.")

if __name__ == "__main__":
    main()
