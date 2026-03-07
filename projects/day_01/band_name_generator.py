import random
from collections import Counter
from data import question_pool

generator_session_log = []

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
    while True:
        again = input("Generate one more name? y/n/history").lower().strip()
        if again == 'history':
            print("\nThus were born:")
            for band in generator_session_log:
                print(band)
            print("\n")
            continue
        if again in ['y','n']:
            break

    if again=='n':
        print("Thank you for using Band Name Generator!")
        break
