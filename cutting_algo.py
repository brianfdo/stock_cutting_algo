cut_dict = {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26}

def generate_cut_list(cut_dict):
    cut_list = []
    for key, value in cut_dict.items():
        for i in range(value):
            cut_list.append(int(key))
    # cut_list.sort(reverse=True)
    return cut_list
cut_list = generate_cut_list(cut_dict)

sum = sum(cut_list) / 300
print(sum)

# temp hard coded sheet size
sheet_sizes = [300,100]

# max number of sheets
max_sheets = len(cut_list)

def wood_cutting(cut_list, sheet_sizes, max_sheets):
    sheet_sizes.sort(reverse=True)
    sheets = 0
    sheet_type = [0] * max_sheets
    rem_sheets = [0] * max_sheets
    cuts_per_sheet = []

    # loops through all cuts
    for i in range(len(cut_list)):
        j = 0

        # algo to find best sheet to assign the cut
        min_waste = sheet_sizes[0] + 1
        best_index = 0
        for j in range(sheets):
            if (rem_sheets[j] >= cut_list[i] and rem_sheets[j] - cut_list[i] < min_waste):
                best_index = j
                min_waste = rem_sheets[j] - cut_list[i]
             
        # if no sheet can accommodate the cut, then we create new sheet
        if (min_waste == sheet_sizes[0] + 1):
            rem_sheets[sheets] = sheet_sizes[0] - cut_list[i]
            cuts_per_sheet.append([cut_list[i]])
            sheets += 1
        # assign the cut to best sheet
        else: 
            rem_sheets[best_index] -= cut_list[i]
            cuts_per_sheet[best_index].append(cut_list[i])

    sheet_sizes.sort()
    for i in range(len(cuts_per_sheet)):
        sizeFit = False
        j = 0
        total = 0
        for element in range(len(cuts_per_sheet[i])):
            total = total + cuts_per_sheet[i][element]
        while sizeFit is False:
            if total <= sheet_sizes[j]:
                sheet_type[i] = sheet_sizes[j]
                rem_sheets[i] = sheet_sizes[j] - total
                sizeFit = True
            else:
                j += 1




    
    return(sheets, cuts_per_sheet, sheet_type[:sheets], rem_sheets[:sheets])

print(wood_cutting(cut_list, [300,100], len(cut_list)))