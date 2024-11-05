from bintreeFile import Bintree

svenska = Bintree()
engelska = Bintree()
hidden_message = []

with open("word3.txt", "r", encoding="utf-8") as svenskfil:
    for rad in svenskfil:
        ordet = rad.strip()  # Ett trebokstavsord per rad
        if ordet in svenska:
            print(ordet, end=" ")
        else:
            svenska.put(ordet)  # in i sökträdet
print("\n")


with open('engelska.txt', 'r', encoding='utf-8') as engelskfil:

    word_list = engelskfil.read().split()

    # filtrerar bort specialtecken
    for word in word_list:
        cleaned_word = word.strip("."",!?'")

        if cleaned_word in engelska:
            pass

        else:
            engelska.put(cleaned_word)
            if cleaned_word in svenska:
                hidden_message.append(cleaned_word)

    separator = ' '
    message = separator.join(hidden_message)    # omvandlar alla substrings til en string
    print(message)
