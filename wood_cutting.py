cut_dict = {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26}

cut_list = []
for key, value in cut_dict.items():
    for i in range(value):
        cut_list.append(int(key))
cut_list.sort(reverse=True)

# hard coded sheet size
sheet_size = 250


def cut(cut_list, sheet_size):
    sheets = 0
    rem_length = sheet_size
    cuts_per_sheet = []
    temp = []
    for i in range(len(cut_list)):
        if rem_length >= cut_list[i]:
            rem_length = rem_length - cut_list[i]
            temp.append(cut_list[i])
        else:
            sheets += 1
            cuts_per_sheet.append(temp)
            rem_length = sheet_size - cut_list[i]
            temp = [cut_list[i]]
    return(sheets, cuts_per_sheet)
