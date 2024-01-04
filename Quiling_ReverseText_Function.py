while True:
    here_type = input("Enter a word: ")

    if not here_type.isalpha():
        print(" Please enter a valid text (no numbers allowed). Try again!")
        continue

    bali_text = here_type[::-1]
    print("Reversed Text:", bali_text)

    pili_lang = input("Do you want to enter another text? (yes/no): ")
    if pili_lang.lower() != 'yes':
        break