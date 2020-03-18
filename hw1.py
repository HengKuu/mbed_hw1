# Part. 1
#=======================================
# Import module
#  csv -- fileIO operation
import csv
#=======================================

# Part. 2
#=======================================
# Read cwb weather data
cwb_filename = '106012042.csv'
data = []
header = []
with open(cwb_filename) as csvfile:
   mycsv = csv.DictReader(csvfile)
   header = mycsv.fieldnames
   for row in mycsv:
        # print(row)
        data.append(row)
#=======================================
#test
# Part. 3
#=======================================
# Analyze data depend on your group and store it to target_data like:
# Retrive all data points which station id is "C0X260" as a list.
# target_data = list(filter(lambda item: item['station_id'] == 'C0X260', data))

# Retrive ten data points from the beginning.
# target_data = list(filter(lambda item: item['station_id'] == 'C0F9A0', data))

class result:
    def __init__(self, station_id, WDSD):
        self.station_id = station_id
        self.WDSD = WDSD

list1 = list(filter(lambda item: (item['station_id'] == 'C0A880') | 
                                       (item['station_id'] == 'C0F9A0') |
                                       (item['station_id'] == 'C0G640') |
                                       (item['station_id'] == 'C0R190') |
                                       (item['station_id'] == 'C0X260'), data))
# print(len(list1)) 
for i in range(len(list1)):
    if (list1[i]['WDSD'] == '-99.000') | (list1[i]['WDSD'] == '-999.000'):
        list1[i]['WDSD'] = 'None'
#create five list to store each lists' WDSD
A, F, G, R, X = [], [], [], [], []  
for i in range(len(list1)):
    # print(list1[i]['station_id'])
    if(list1[i]['station_id'] == 'C0A880'):
        A.append(list1[i]['WDSD'])
    elif(list1[i]['station_id'] == 'C0F9A0'):
        F.append(list1[i]['WDSD'])
    elif(list1[i]['station_id'] == 'C0G640'):
        G.append(list1[i]['WDSD'])
    elif(list1[i]['station_id'] == 'C0R190'):
        R.append(list1[i]['WDSD'])
    elif(list1[i]['station_id'] == 'C0X260'):
        X.append(list1[i]['WDSD'])
# print(float(max(F)) - float(min(F)))
#calculate max_range
rangeA, rangeF, rangeG, rangeR, rangeX = 0, 0, 0, 0, 0
if(((max(A)) == 'None') | (min(A) == 'None')):
    rangeA = 'None'
else:
    rangeA = float(max(A)) - float(min(A))
if(((max(F)) == 'None') | (min(F) == 'None')):
    rangeF = 'None'
else:
    rangeF = float(max(F)) - float(min(F))
if(((max(G)) == 'None') | (min(G) == 'None')):
    rangeG = 'None'
else:
    rangeG = float(max(G)) - float(min(G))
if(((max(R)) == 'None') | (min(R) == 'None')):
    rangeR = 'None'
else:
    rangeR = float(max(R)) - float(min(R))
if(((max(X)) == 'None') | (min(X) == 'None')):
    rangeX = 'None'
else:
    rangeX = float(max(X)) - float(min(X))
# print(rangeA)
print ("[['C0A880', " ,rangeA, "], ['C0F9A0', " ,rangeF, "], ['C0G640', " ,rangeG,"], ['C0R190', " ,rangeR, "], ['C0X260', " ,rangeX, "]]")
# target_data = []
# target_data.append(result('C0A880', rangeA))
# target_data.append(result('C0F9A0', rangeF))
# target_data.append(result('C0G640', rangeG))
# target_data.append(result('C0R190', rangeR))
# target_data.append(result('C0X260', rangeX))
# # for obj in target_data:
# #     print(obj.station_id, obj.WDSD, sep=' ')



# print(list1)
# print(data[0]['station_id'])
# print(target_data[1]['WDSD'])
# target_data = data[:10]

#=======================================

# Part. 4
#=======================================
# Print result
# print(target_data)
#========================================