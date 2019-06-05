import csv
with open('json.log', 'r') as logfile, open('json.csv', 'w') as csvfile:
    reader = csv.reader(logfile, delimiter =',', quotechar='"', escapechar='\\',)
    writer = csv.writer(csvfile, delimiter =',',)
    writer.writerow(['TimeMillis', 'thread', 'level', 'loggerName','marker', 'message', 'endOfBatch', 'parameterCount', 'loggerFqcn', 'formattedMessage', 'threadPriority', 'threadId', 'contextMap', 'hashcode', 'internal_className', 'internal_content:', 'stateMapping', 'clientId', 'shipmentOrde', 'externalCode', 'alteredEventDate', 'deliveryMethod', 'substatus', 'invoiceKey', 'ruleActionType', 'trackingCode', 'messageParams', 'logisticProviderId', 'invoiceSeries', 'invoiceNumber', 'ruleName', 'shipmentOrderNumber', 'shipmentOrderVolumeHistoryId', 'ruleId', 'status', 'microStateId', 'eventDate', 'internal_date', 'internal_logger', 'logisticProviderId', 'shipmentOrderId'])
    writer.writerows(reader)