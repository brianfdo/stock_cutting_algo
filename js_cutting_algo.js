cut_dict = {'125': 10, '120': 40, '108': 26, '99': 5, '60': 10, '49': 10, '43': 24, '34': 12, '30': 5, '12': 26};
sheet_sizes = [200,100,150,300];

var cut_list = [];
function generate_cut_list(cut_dict){
    for (var key in cut_dict) {
        if (cut_dict.hasOwnProperty(key)) {
            for (let i = 0; i < cut_dict[key]; i++) {
                cut_list.push(key);
            }
        }
    }
}
generate_cut_list(cut_dict);

var cuts_per_sheet = []
function wood_cutting(cut_list, sheet_sizes) {
    var max_sheets = cut_list.length;
    sheet_sizes.sort(function(a, b){return b-a});
    var sheets = 0;

    var sheet_type = [];
    var rem_sheets = [];
    for (let i = 0; i < max_sheets; i++) {
        sheet_type[i] = 0;
        rem_sheets[i] = 0;
    }
    
    var min_waste = sheet_sizes[0] + 1;
    // loops through all cuts
    for (let i = 0; i < max_sheets; i++){
        var j = 0;

        // algo to find best sheet to assign the cut
        
        var best_index = 0;
        for (j = 0; j < sheets; j++) {
            if (rem_sheets[j] >= cut_list[i] && (rem_sheets[j] - cut_list[i]) < min_waste){
                // console.log('yo')
                best_index = j;
                min_waste = rem_sheets[j] - cut_list[i];
                // console.log(min_waste);
            }
        }


        // if no sheet can accommodate the cut, then we create new sheet
        
        if (min_waste == sheet_sizes[0] + 1) {
            // console.log(min_waste)
            // console.log(sheet_sizes[0] + 1)
            rem_sheets[sheets] = sheet_sizes[0] - cut_list[i];
            var temp = [];
            temp.push(cut_list[i]);
            cuts_per_sheet.push(temp);
            sheets++;
            // assign the cut to best sheet
        } else {
            rem_sheets[best_index] -= cut_list[i];
            // console.log('yo2')
            // console.log(cut_list[i])
            cuts_per_sheet[best_index].push(cut_list[i]);
            // console.log('yo3')
            // console.log(cuts_per_sheet[best_index]);
        }

    }

    sheet_sizes.sort()
    // console.log(cuts_per_sheet)
    for (let i = 0; i < cuts_per_sheet.length; i++) {
        var sizeFit = false;
        
        var total = 0;
        console.log(cuts_per_sheet[1][0]);
    
        for (let element = 0; element < cuts_per_sheet[i].length; element++) {
            console.log(total);
            total = total + parseInt(cuts_per_sheet[i][element]);
        }
        var k = 0;
        console.log(sheet_sizes)
        // while (sizeFit == false) {
        //     console.log(sheet_sizes[k]);
        //     // console.log(total);
        //     if (total <= sheet_sizes[k]){
        //         console.log('in if statement');
        //         sheet_type[i] = sheet_sizes[k];
        //         rem_sheets[i] = sheet_sizes[k] - total;
        //         sizeFit = true;
        //     } else {
        //         k += 1;
        //     }
        // }

    }
    // console.log(sheet_type);
    console.log(sheets)
    // console.log(cuts_per_sheet)
    // console.log(sheet_type.slice(sheets))

}
wood_cutting(cut_list, sheet_sizes);

// ef wood_cutting(cut_list, sheet_sizes, max_sheets):
//     sheet_sizes.sort(reverse=True)
//     sheets = 0
//     sheet_type = [0] * max_sheets
//     rem_sheets = [0] * max_sheets
//     cuts_per_sheet = []

//     # loops through all cuts
//     for i in range(len(cut_list)):
//         j = 0

//         # algo to find best sheet to assign the cut
//         min_waste = sheet_sizes[0] + 1
//         best_index = 0
//         for j in range(sheets):
//             if (rem_sheets[j] >= cut_list[i] and rem_sheets[j] - cut_list[i] < min_waste):
//                 best_index = j
//                 min_waste = rem_sheets[j] - cut_list[i]
             
//         # if no sheet can accommodate the cut, then we create new sheet
//         if (min_waste == sheet_sizes[0] + 1):
//             rem_sheets[sheets] = sheet_sizes[0] - cut_list[i]
//             cuts_per_sheet.append([cut_list[i]])
//             sheets += 1
//         # assign the cut to best sheet
//         else: 
//             rem_sheets[best_index] -= cut_list[i]
//             cuts_per_sheet[best_index].append(cut_list[i])

//     sheet_sizes.sort()
//     for i in range(len(cuts_per_sheet)):
//         sizeFit = False
//         j = 0
//         total = 0
//         for element in range(len(cuts_per_sheet[i])):
//             total = total + cuts_per_sheet[i][element]
//         while sizeFit is False:
            // if total <= sheet_sizes[j]:
            //     sheet_type[i] = sheet_sizes[j]
            //     rem_sheets[i] = sheet_sizes[j] - total
            //     sizeFit = True
            // else:
            //     j += 1    
//     return(sheets, cuts_per_sheet, sheet_type[:sheets], rem_sheets[:sheets])