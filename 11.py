def main():
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    x[1::2] = reversed(x[1::2])
    print(x)
    
if __name__ == "__main__":
    main()
