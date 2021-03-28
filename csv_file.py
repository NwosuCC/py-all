import csv
import multiprocessing as mp


def process_csv():
    with open('files/employee_birthday.txt', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                print('Column names are {}'.format(", ".join(row)))
                line_count += 1
            message = '\t{name} works in the {department} department, and was born in {birthday_month}.'
            print(message.format(name=row['name'], department=row['department'], birthday_month=row['birthday month']))
            line_count += 1
        print('Processed {} lines.'.format(line_count))


# process_csv()

print(mp.cpu_count())
