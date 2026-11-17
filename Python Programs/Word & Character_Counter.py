# Word and Character Counter Program:
print("===== Word and Character Counter Program =====")

while True:

    text = input("Enter your text ('x' to exit): ")

    if text.lower() == 'x':
        break
    else:
        print("Words:", len(text.split()))
        print("Characters:", len(text.replace(" ", "")))
