from datetime import datetime
import multiprocessing

def read_info(name):
    with open(name, "r") as file:
        all_data = []
        while True:
            line = file.readline()
            if not line:
                break
            else:
                all_data.append(line)



filenames = [f'./files_10.5/file {number}.txt' for number in range(1, 5)]


# stat = datetime.now()
# for i in filenames:
#     read_info(i)
# end = datetime.now()
# """0:00:05.354840"""
# print(end - stat)

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.now()
        pool.map(read_info, filenames)
        end = datetime.now()
    print(end - start)
    """0:00:02.069856"""















