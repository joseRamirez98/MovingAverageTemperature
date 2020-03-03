import csv
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.lines as lines

def main():
    infile = "NorCal-1880-2018.csv"
    outfile = "moving_ave.csv"
    window = input("Enter an integer between 0 and 60:")
    correct_input = False

    while correct_input != True: 
        if window.isdigit() == False:
            print("Input not within 0 and 60.")
            window = input("Enter an integer between 0 and 60:")
        elif int(window) in range(0,61):
            correct_input = True
            calcData(int(window), infile)
            dataToPlot(int(window), outfile)
        else:
            print("Enter an integer up to 60.")
            window = input("Enter an integer between 0 and 60:")

def calcData(window, filename):
    year_list = []
    temp_list = []

    with open(filename, 'r') as csv_infile:
        csv_read = csv.reader(csv_infile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        next(csv_read)
        for line in csv_read:
            year_list.append(line[0])
            temp_list.append(float(line[1]))
        csv_infile.close()
    with open('moving_ave.csv', 'w') as csv_outfile:
        csv_write = csv.writer(csv_outfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_write.writerow(['Year', 'Value'])

        for i in range(window, len(temp_list)-window):
            ave =  sum(temp_list[i-window:i+window+1])/(2*window+1)
            formatted_ave = "{:.4f}".format(ave)
            csv_write.writerow([year_list[i],formatted_ave])
        csv_outfile.close()

def dataToPlot(window, filename):
    data = pd.read_csv(filename, sep=",")
    years_list = data['Year'].tolist()
    temp_data = data['Value'].tolist()

    fig = plt.figure()
    ax=fig.add_subplot(111)
    ax.plot(years_list, temp_data, c='b')
    plt.title('Sacramento July Temperature Anomaly\n' + str(window) + ' Year +/- Moving Average')
    plt.xlabel('Year')
    plt.ylabel('Moving Averages Temps')
    fig.savefig("output.jpg", dpi=500)


main()
    





















