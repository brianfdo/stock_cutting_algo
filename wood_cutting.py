cut_dict = {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26}

cut_list = []
for key, value in cut_dict.items():
    for i in range(value):
        cut_list.append(int(key))
cut_list.sort(reverse=True)

# hard coded sheet size
sheet_size = 250

# max number of sheets
max_sheets = len(cut_list)

def cut(cut_list, sheet_size, max_sheets):
    sheets = 0
    rem_sheets = [0] * max_sheets
    # rem_length = sheet_size
    cuts_per_sheet = []
    temp = []

    # loops through all cuts
    for i in range(max_sheets):
        j = 0

        min = sheet_size + 1
        best_index = 0
        # loop to find best sheet to assign the cut
        for j in range(sheets):
            if (rem_sheets[j] >= cut_list[i] and rem_sheets[j] - cut_list[i] < min):
                best_index = j
                min = rem_sheets[j] - cut_list[i]
             
        # if no sheet could accommodate the cut, then we create a new bin
        if (min == sheet_size + 1):
            rem_sheets[sheets] = sheet_size - cut_list[i]
            cuts_per_sheet.append([cut_list[i]])
            sheets += 1
        # assign the cut to best sheet
        else: 
            rem_sheets[best_index] -= cut_list[i]
            cuts_per_sheet[best_index].append(cut_list[i])

        # if rem_length >= cut_list[i]:
        #     rem_length = rem_length - cut_list[i]
        #     temp.append(cut_list[i])
        # else:
        #     sheets += 1
        #     cuts_per_sheet.append(temp)
        #     rem_length = sheet_size - cut_list[i]
        #     temp = [cut_list[i]]
    return(sheets, cuts_per_sheet, 'waste per sheet:', rem_sheets[:sheets])

print(cut(cut_list, 250, len(cut_list)))