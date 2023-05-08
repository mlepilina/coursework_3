from utils.result import create_result


if __name__ == '__main__':
    for item in create_result():
        for text in item:
            print(text)
