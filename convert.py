from datetime import datetime
import os
import errno
import csv


print(os.path.dirname(os.path.realpath(__file__)))

current_dir_path = os.path.dirname(os.path.realpath(__file__))

os.chdir(current_dir_path)

try:
    os.mkdir('data_converted')
except OSError as exc:
    if exc.errno != errno.EEXIST:
        raise
    import shutil
    shutil.rmtree('data_converted')
    os.mkdir('data_converted')
    pass

clean_tac_path = current_dir_path + '/data/clean_tac'
clean_tac_list = os.scandir('data/clean_tac')

os.chdir(current_dir_path + '/data_converted')
# os.mkdir(current_dir_path + '/data_converted/'+ 'clean_tac_converted')
os.mkdir('clean_tac')
os.chdir('clean_tac')

for file in clean_tac_list:
    if file.is_file():
        clean_tac_file = clean_tac_path + '/' + file.name
        with open(clean_tac_file, 'r') as source:
            with open(file.name, 'w', newline='') as dest:
                dest.write(source.readline())
                writer = csv.writer(dest)
                for line in source.read().splitlines():
                    cols = line.split(',')
                    tup = [
                        datetime.utcfromtimestamp(
                            int(cols[0])).strftime('%Y-%m-%d %H:%M:%S'),
                        float(cols[1])
                    ]
                    writer.writerow(tup)

accelerometer_data_file_path = current_dir_path + \
    '/data/all_accelerometer_data_pids_13.csv'
