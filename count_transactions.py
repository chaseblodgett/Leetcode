from collections import Counter, defaultdict

def groupTransactions(transactions):
    transaction_counts = Counter(transactions)
    

    sorted_transactions = sorted(
        transaction_counts.items(),
        key=lambda x: (-x[1], x[0])
    )
    
    result = []

    for item, count in sorted_transactions:
        result.append(str(item) + " " + str(count))
    return result

from collections import defaultdict

logs = []
n = int(input())
for i in range(n):
    logs.append(input())
maxSpan = int(input())

def processLogs(logs, maxSpan):
    
    my_dict = defaultdict(int)
    ret = []

    for log in logs:
        arr_log = log.split()

        if arr_log[2] == "sign-in":
            my_dict[arr_log[0]] = int(arr_log[1])

        elif arr_log[0] in my_dict and my_dict[arr_log[0]] - int(arr_log[1]) <= maxSpan:
            ret.append(arr_log[0])

    ret.sort()
    return ret

ret = processLogs(logs,maxSpan)

for user in ret:
    print(user)
