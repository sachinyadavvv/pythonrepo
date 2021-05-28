#string occurance
test_string = "Hello my name is"

spl_word = 'best'

print("The original string : " + str(test_string))

print("The split string : " + str(spl_word))

res = test_string.partition(spl_word)[2]

print("String after the substring occurrence : " + res)
