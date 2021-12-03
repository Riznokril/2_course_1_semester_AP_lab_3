from hamster import Hamster

if __name__ == '__main__':
    result = Hamster.find_max_number_of_hamsters("hamster_in.txt")
    Hamster.write_result_in_out(result)
    
    print("Result in hamsters_out.txt")