alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p',
            'q','r','s','t','u','v','w','x','y','z']

agin = "yes"
while agin == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    def shift_alphabet(arr, n, direction):
        n = n % len(arr) 
        if direction == "encode":
            return arr[n:] + arr[:n]  
        else:
            return arr[-n:] + arr[:-n]  

   
    shifted_alphabet = shift_alphabet(alphabet, shift, direction)

   
    result_text = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            result_text += shifted_alphabet[index]
        else:
            result_text += char  

    print(f"The {direction}d text is: {result_text}")
    agin = (input("you want to do it again(yes/no): ")).lower()

                    