import time
def main():
    f = None
    try:
        with open('裸の心.txt', 'r', encoding='utf-8') as f:
            # for line in f:
                # print(line, end='')
                # time.sleep(0.1)
            lines = f.readlines()
        print(lines)


    except FileNotFoundError:
        print('file not found')
    except LookupError:
        print('Look up error')
    except UnicodeDecodeError:
        print('unicode decode error')
    finally:
        if f:
            f.close()


if __name__ == "__main__":
    main()