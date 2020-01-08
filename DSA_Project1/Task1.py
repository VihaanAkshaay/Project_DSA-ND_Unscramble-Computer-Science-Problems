"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
unique_list = []
count = 0
for text in texts:
  if text[0] not in unique_list:
    unique_list.append(text[0])
    count +=1
  if text[1] not in unique_list:
    unique_list.append(text[1])
    count +=1
for call in calls:
  if call[0] not in unique_list:
    unique_list.append(call[0])
    count +=1
  if call[1] not in unique_list:
    unique_list.append(call[1])
    count +=1

print(f'There are {count} different telephone numbers in the record')
