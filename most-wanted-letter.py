# Когда я увидел, что это делается в одну строку, расстроился, но зато хотя б честно сам сделал
def checkio(text: str) -> str:
    alphabet = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
    text = text.lower()
    symbols_in_text_list = []
    symbols_in_text_set = set()
    max = 0
    output_temp = []
    # получаю список всех вхождений, отбрасывая знаки.
    for i in text:
        if set(i).issubset(alphabet):
            symbols_in_text_list.append(i)
            symbols_in_text_set.add(i)
    for value in symbols_in_text_set:
        if symbols_in_text_list.count(value) > max:
            max = symbols_in_text_list.count(value)
            output_temp = [value]
        elif symbols_in_text_list.count(value) == max:
            output_temp.append(value)
    max = 25
    for i in output_temp:
        if alphabet.index(i) <= max:
            max = alphabet.index(i)
    return alphabet[max]

if __name__ == '__main__':
    print("Example:")
    print(checkio("Hello World!"))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio("Hello World!") == "l", "Hello test"
    assert checkio("How do you do?") == "o", "O is most wanted"
    assert checkio("One") == "e", "All letter only once."
    assert checkio("Oops!") == "o", "Don't forget about lower case."
    assert checkio("AAaooo!!!!") == "a", "Only letters."
    assert checkio("abe") == "a", "The First."
    print("Start the long test")
    assert checkio("a" * 9000 + "b" * 1000) == "a", "Long."
    print("The local tests are done.")