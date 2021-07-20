cut_dict = {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26}

cut_list = []
for key, value in cut_dict.items():
    for i in range(value):
        cut_list.append(int(key))
cut_list.sort(reverse=True)

# hard coded sheet size
sheet_size = 250


