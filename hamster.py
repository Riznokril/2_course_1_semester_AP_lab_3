class Hamster:
    def __init__(self, h, g):
        self.h = h
        self.g = g

    def total_food_for_hamster(self, n):
        return self.h + (n-1) * self.g

    def write_result_in_out(result):
        with open("hamster_out.txt", mode="w") as hamster_out_file:
            hamster_out_file.write(f"{result}")

    def create_list_of_file_data(name_in_file):
        with open(name_in_file, 'r') as hamster_in_file:
            s = int(hamster_in_file.readline())           
            c = int(hamster_in_file.readline())          
            hamsters = []
            
            for i in range(c):
                hams = Hamster(*list(map(int, hamster_in_file.readline().split(" "))))
                hamsters.append(hams)

        return [s, c, hamsters]

    def find_max_number_of_hamsters(name_in_file):        
        hamsters = Hamster.create_list_of_file_data(name_in_file)[2]
        s = Hamster.create_list_of_file_data(name_in_file)[0]
        result = -1

        while result < len(hamsters):
            result += 1
            hamsters.sort(key=lambda hamster: hamster.total_food_for_hamster(result))

            s_current = sum(hamster.total_food_for_hamster(result) for hamster in hamsters[:result])

            if s_current > s: 
                result -= 1               
                break

        return result
                


