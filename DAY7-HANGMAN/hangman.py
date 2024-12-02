import api
import json

print('''
        ██╗░░██╗░█████╗░███╗░░██╗░██████╗░███╗░░░███╗░█████╗░███╗░░██╗
        ██║░░██║██╔══██╗████╗░██║██╔════╝░████╗░████║██╔══██╗████╗░██║
        ███████║███████║██╔██╗██║██║░░██╗░██╔████╔██║███████║██╔██╗██║
        ██╔══██║██╔══██║██║╚████║██║░░╚██╗██║╚██╔╝██║██╔══██║██║╚████║
        ██║░░██║██║░░██║██║░╚███║╚██████╔╝██║░╚═╝░██║██║░░██║██║░╚███║
        ╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝░╚═════╝░╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝ 
        ''')
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', 
'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''',
'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
json_word = api.data 
String_word = json.dumps(json_word)
#print(String_word)
#print(String_word[api.num+1])
#print(String_word[2])
#print(api.num)

Dead_number = 0
string_index = 2
display_array = ["_"]*(api.num)
letter_check_index = 2
winning_number = 0
winnig_string = " " 
while Dead_number != 6:
    letter = input("Enter the Letter: ")[0]
    
    for index in range(2,api.num+2):
        if String_word[index] == letter:
            display_array[index-2] = letter
            for n in range(0,api.num):
                 if display_array[n] == '_':
                     winning_number += 1
            if winning_number == 0:
                winnig_string = "You win..!"
                break
            winning_number = 0         
        else:
            letter_check_index += 1
            
    #print(letter_check_index)
    
    if letter_check_index == api.num:
        Dead_number += 1
        print(HANGMANPICS[Dead_number])
        print(''.join(display_array))
        letter_check_index = 0    
    else:
        print(HANGMANPICS[Dead_number])
        print(''.join(display_array))
        letter_check_index = 0    
    if winnig_string == "You win..!":
        print(''' 
                __     __                    _       
                \ \   / /                   (_)      
                 \ \_/ /__  _   _  __      ___ _ __  
                  \   / _ \| | | | \ \ /\ / / | '_ \ 
                   | | (_) | |_| |  \ V  V /| | | | |
                   |_|\___/ \__,_|   \_/\_/ |_|_| |_|
                                      
                                      ''')
        break
    elif Dead_number == 6:
        print(''' __     __             _           _   
                  \ \   / /            | |         | |  
                   \ \_/ /__  _   _    | | ___  ___| |_ 
                    \   / _ \| | | |   | |/ _ \/ __| __|
                     | | (_) | |_| |   | | (_) \__ \ |_ 
                     |_|\___/ \__,_|   |_|\___/|___/\__|
                                      ''')
        break

        