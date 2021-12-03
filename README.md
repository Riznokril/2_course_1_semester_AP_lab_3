# 2_course_1_semester_AP_lab_3

## Hamsters

The pet store sells hamsters. These are peaceful domestic beings, however it turned out that they have interesting eating behavior.

In order to feed a hamster living alone, you need H packets of food for a day. However, if several hamsters live together, they wake up greedy. In this case, each hamster eats an additional G packets of food per day of each neighbor. The daily norm H and greed G are individual for each hamster.

There are only C hamsters in the store. You want to buy as much as possible, but you have there are only S packets of food per day. Determine the maximum number of hamsters you have you can feed.

Input data
The input file hamster_in.txt consists of C + 2 lines.

The first line contains S - daily food supply. 0 ≤ S ≤ 10^9
The second line contains C - the total number of hamsters on sale. 1 ≤ C ≤ 10^5
The next C lines contain H, G - integers separated by a space, which means daily norm and level of greed of each hamster. 0 ≤ H,G ≤ 10^9
Output data
The output file hamster_out.txt must contain one number - the maximum number of hamsters that you can feed by settling them together.

## Hot to run

1) Download files from the repository https://github.com/Riznokril/2_course_1_semester_AP_lab_3
2) Change input file(hamster_in.txt) according to previously set rules
3) In console write: python main.py
4) Enter the name of input file
5) Check output file(hamster_out.txt) to see the result

## How to run tests

1) Download files from the repository https://github.com/Riznokril/2_course_1_semester_AP_lab_3
2) Change input file(hamster_in.txt) according to previously set rules
3) In console write: python test.py

## How it works

Methods in class Hamster(file: hamster.py):
    total_food_for_hamster:
        returns a total food spend for one hamster with n heignbours
    
    write_result_in_out:
        rewrites output file(hamster_out.txt)

    create_list_of_file_data:
        reads input file(hamster_in.txt)
        returns list of s(daily food supply), c(number of hamsters to sale) and hamsters(list of hamsters data h(daily consumption) and g(greed))

    find_max_number_of_hamsters:
        in cycle while in one step sort hamsters by their total_food_for_hamster and summing the most suitable hamsters
        checks if we have more s(daily food supply) than this number of hamsters need? we do: next iteration, we don't: returns previous iteration number
        returns maximum number of hamsters, which person can provide