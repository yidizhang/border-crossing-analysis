import csv
import math
import copy
import argparse
from operator import itemgetter
from datetime import datetime
from itertools import groupby

#function to round values
def rounding(i):
    f = math.floor(i)
    return f if i - f < 0.5 else f+1

#remove extra brackets for the output csv file 
def output_file(raw_list):
    output = []
    for item in output_file:
        if isinstance(item, list):
            for i in output_file(item):
                output.append(i)
        else:
            output.append(item)
    return output

#function to compute the number of months per measure. Input are a list of datesor dict if the frequency for each measure is different
def count_months(list_with_sums):
    dates = set()
    measure_dict = {}
    for row in list_with_sums:
        if row[1] not in dates:
            dates.add(row[1])
        if row[2] in measure_dict:
            measure_dict[row[2]] += 1
        else:
            measure_dict[row[2]] = 1
    # Remove the column name Measure
    del(measure_dict['Measure'])

    # test if each measure has same frequency for each month
    next_value = next(iter(measure_dict.values()))
    all_equal_frequency = all(value == next__value for value in measure_dict.values())

    return len(dates) if all_equal_frequency else measure_dict

#function to find the average crosssing per month per measure
def calculate_average_crossing_per_month_and_measure(num_of_months, list_with_sums):
    list_avg = []
    for i in range(len(list_with_sums) - 1, 0, -1):
        each_row = list_with_sums[i]
        # check if each measure has different frequency
        if isinstance(num_of_months, dict):
            for key, value in num_of_months.items():
                if each_row[2] == key:
                    if i % value == 0:
                        sumSoFar, count = 0, 0
                        each_row = each_row + [0]
                    else:
                        previous_row = list_with_sums[i + 1]
                        sumSofar += previous_row[3]
                        counter += 1
                        each_row = each_row + [rounding(sumSoFar / count)]
                    list_avg.append(each_row)
        #the case with same frequency for each month            
        else:
            if i % (num_of_months - 1) == 0:
                sumSoFar, count = 0, 0
                each_row = each_row + [0]
            else:
                previous_row = list_with_sums[i + 1]
                sumSoFar += previous_row[3]
                count += 1
                each_row = each_row + [my_rounding(sumSoFar / count)]
            list_avg.append(each_row)
    return list_avg

def parse_args():
    """
    Helper function that takes in the arguments passed in the shell to be used in the main script.
    Returns:
        args -- arguments
    """
    parser = argparse.ArgumentParser(description='Look for Border Crossing Statistics')
    parser.add_argument('--input', help="enter the input filename", type=str)
    parser.add_argument('--output', help="enter the output filename", type=str)
    args = parser.parse_args()
    return args


def main():
    """ Main function that takes in the input file of border crossing entry data and returns the desired statistics. """

    # input and output Error-Handling
    args = parse_args()
    if args.input is None:
        raise ImportError('Did not specify the correct input file!')
    if args.output is None:
        raise ImportError('Did not specify the correct output file!')

    # Read input data
    with open(args.input, mode='r') as csv_file:

        csv_reader = csv.reader(csv_file, delimiter=',')

        # Sort list by Border, Date, and Measure in descending order
        sorted_list = sorted(csv_reader, key=itemgetter(3, 5))


        # find sum of each measure per month and store it as a new list, for example, add the sum for each row where the border, date and measure are the same
        list_with_sums = [key + [sum([int(r[6]) for r in rows if r[6].isdigit() and int(r[6]) != 0])] for key, rows in groupby(sorted_list, key=lambda x: x[3:6])]

        # compute the number of number for each measure, if the frequence is the same, an int is returned.Otherwise, a dictionary is returned.
        num_of_months = count_the_months(list_with_agg_sums)

        # calculate the average crossing per month and per measure
        list_avg = calculate_aver_crossing(num_of_months, list_with_sums)

        # Sort the list by Date, Value, Measure, Border in descending order
        sorted_list_border_measure_value_average = sorted(list_avg, key=itemgetter(3, 2, 0), reverse=True)
        Last_sorted_list = sorted(sorted_list_border_measure_value_average,
                                   key=lambda x: datetime.strptime(x[1], '%d/%m/%Y %H:%M:%S %p'), reverse=True)

    # Write to an output csv file
    with open(args.output, mode='w') as csv_outfile:
        outfile_writer = csv.writer(csv_outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_NONE)

        # Column headers
        outfile_writer.writerow(['Border', 'Date', 'Measure', 'Value', 'Average'])

        outfile_writer = csv.writer(csv_outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        # remove brackets and outlist is matched to required format
        for row in final_sorted_list:
            outfile_writer.writerow(output(row))

if __name__ == '__main__':
    main()

        
       

    

