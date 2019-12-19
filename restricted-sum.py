def checkio(data):
    if len(data) > 1:
        data[0] = data[0] + data.pop()
        return checkio(data)
    return data[0]