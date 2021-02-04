def read_raw_input(file_name):
    raw_input = []
    try:
        file = open(file_name, "r")
        for line in file.readlines():
            raw_input.append(line)
        file.close()
    except Exception:
        print("Deu treta lendo arquivo")
        raise Exception
    return raw_input