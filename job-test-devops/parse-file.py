import csv
with open('file.log', 'r') as logfile, open('file.csv', 'w') as csvfile:
    reader = csv.reader(logfile, delimiter =',')
    writer = csv.writer(csvfile,delimiter=',',)
    writer.writerow(['Date', 'Id', 'scheduled-executor', 'INFO', 'TrackingRuleEngineAndServiceImpl'])
    writer.writerows(reader)