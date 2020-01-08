"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""
dict = {}

for call in calls:
  if call[0] not in  dict.keys():
    dict.update({call[0]:int(call[3])})
  else:
    dict[call[0]] += int(call[3]) 
  if call[1] not in dict.keys():
    dict.update({call[1]:int(call[3])})
  else:
    dict[call[1]] += int(call[3])

call_durations = dict.values()
max_duration = 0

for item in call_durations:
  if max_duration < item:
    max_duration = item

ph_number = ''
for key in dict:
  if dict[key] == max_duration:
    ph_number = key

print(f'{ph_number} spent the longest time, {max_duration} seconds, on the phone during September 2016')


