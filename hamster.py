class Hamster:
    def __init__(self, h, g):
        self.h = h
        self.g = g

    def total_food_for_hamster(self, n):
        return self.h + (n-1) * self.g

    @staticmethod
    def find_max_number(name_of_file):
        with open(name_of_file, 'r') as file:
            s = int(file.readline())            
            c = int(file.readline())            
            hamsters = []
            
            for i in range(c):
                hams = Hamster(*list(map(int, file.readline().split(" "))))

                if hams.h <= s:
                    hamsters.append(hams)
        
        result = -1

        while result < len(hamsters):
            result += 1
            hamsters.sort(key=lambda hamster: hamster.total_food_for_hamster(result))

            print(result)


            s_current = sum(hamster.total_food_for_hamster(result) for hamster in hamsters[:result])
            if s_current > s:
                print("s_current in if: " + str(s_current))
                result -= 1
                break
                
        with open("hamsters_out.txt", mode="w") as file_output:
            file_output.write(f"{result}")

        return result