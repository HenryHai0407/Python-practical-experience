def cToFConverter():
    while True:
        cTemp = input("Please enter C degree:")
        if cTemp == "":
            print("cTemp is empty, please type again")
            continue
        try:
            cTemp = float(cTemp)
            fTemp = round(cTemp * 9/5 + 32, 2)
            print(f"{cTemp} C is equal to {fTemp} F")
            break
        except ValueError:
            print("cTemp is wrong")
            continue


def main():
    #print("Hello World")
    cToFConverter()

if __name__ == "__main__":
    main()