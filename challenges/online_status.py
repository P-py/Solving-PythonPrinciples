def online_count(status):
    online_counter = 0
    for user in status:
        if status[user] == 'online':
            online_counter += 1
        else:
            pass