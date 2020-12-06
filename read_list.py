filename = 'day2.txt'


passwords =[]
test_cases = []
how_often = []
letters = []
#liste in der die folgen sind auf die man password testen will
test_words = []
# generate information from file and sort into lists
with open(filename, 'r') as f:
    for line in f:
        to_check = line.split(':')[-1].strip()
        check_for = line.split(':')[0].strip()
        symbol = check_for.split(' ')[-1]
        numbers = [int(s) for s in check_for.split(' ')[0].split('-')]
        test_cases.append({'numbers': numbers, 'symbol': symbol})
        #list with pairs of numbers
        how_often.append(numbers)
        #the char that needs to be checked
        letters.append(symbol)
        #passwords that need to be checked
        passwords.append(to_check)

count = 0
help_word = ''
wanted_number = 0
#for every password
while count < len(passwords):
    #get password that will be checked from list
    relevant_password = passwords[count]
    need_to_test = []
    #get the range for the letter
    range_values = how_often[count]
    #count how often the letter is in password
    amount_letter_in_password = relevant_password.count(letters[count])
    #check if amount is in range
    if amount_letter_in_password >= range_values[0] and amount_letter_in_password <= range_values[1]:
        wanted_number = wanted_number +1
    count = count+1
print(wanted_number)
print('finish')

