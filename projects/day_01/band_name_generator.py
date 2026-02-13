import random
from collections import Counter
from data import question_pool

# question_set = random.sample(question_pool, random.randint(1, len(question_pool)))
# print(question_set)
# answer=''
generator_session_log= []

print("Welcome to the band name generator! type start")
start=input("Welcome to the band name generator! type start")


while True:
    answer=''
    question_set = random.sample(question_pool,int(random.triangular(1, 10, 2)))
    print(question_set)
    for question in question_set:
        while True:
            user_input = input(question).strip()
            if len(user_input) > 0:
                answer= (answer + ' ' + user_input).strip()
                break
            else:
                print("One simply cannot write without using letters!")
    band_name = 'The '+ f"{answer}'" if answer.endswith('s') else 'The ' + f"{answer}s"
    print(band_name)
    generator_session_log.append(band_name)
    again = input("Generate one more name? y/n/history").lower()
    if again == 'history':
        print("\nThus were born:")
        for band in generator_session_log:
            print(band)
        again = input("\nGenerate one more name? y/n").lower()
    if again != 'y':
        break







# for question in question_set:
#     while True:
#         user_input = input(question).strip()
#         if len(user_input) > 0:
#             answer= answer + user_input + ' '
#             break
#         else:
#             print("One simply cannot write without using letters!")
#
# display_answer = 'The ' + answer.rstrip()
# if (display_answer.endswith("s")):
#     display_answer+="'"
# else:
#     display_answer+="s"
# generator_session_log.append(display_answer)
# print(display_answer)