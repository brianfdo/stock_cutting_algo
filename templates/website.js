function addsheet() {
    var input = document.createElement('input');
    input.type = "text";
  input.className = "sheet";
    var parent = document.getElementById("sheetid");
    parent.appendChild(input);
}

function addcut() {
    var input = document.createElement('input');
    input.type = "text";
  input.className = "cutsize";
  var inputq = document.createElement('input');
    inputq.type = "text";
  inputq.className = "quantity";
    var parent = document.getElementById("cutid");
    parent.appendChild(input);
  parent.appendChild(inputq);
}

function submit() {

  var sheet_sizes = [];
  var cut_dict = {};

  var sheetList = document.getElementsByClassName("sheet");
  var cutList = document.getElementsByClassName("cutsize");
  var quantList = document.getElementsByClassName("quantity");
  
  for (var i = 0; i < sheetList.length; i++) {
    sheet_sizes.push(sheetList[i].value);
    console.log(sheet_sizes);
  }
  for (var j = 0; j < cutList.length; j++) {
    cut_dict[cutList[j].value] = quantList[j].value;
    console.log(cut_dict);
  }
  
  // // GET is the default method, so we don't need to set it
  // fetch('/hello')
  // .then(function (response) {
  //     return response.text();
  // })
  // .then(function (text) {

  //     // Print the greeting as text
  //     console.log('GET response text:');
  //     console.log(text);
  // });

  // // Send the same request
  // fetch('/hello')
  //     .then(function (response) {

  //         // But parse it as JSON this time
  //         return response.json();
  //     })
  //     .then(function (json) {

  //         // Do anything with it!
  //         console.log('GET response as JSON:');
  //         console.log(json);
  //     })

  // // POST
  // fetch('/hello', {

  //     // Declare what type of data we're sending
  //     headers: {
  //         'Content-Type': 'application/json'
  //     },

  //     // Specify the method
  //     method: 'POST',

  //     // A JSON payload
  //     body: JSON.stringify({"cut_list": cutList})
  // })
  // .then(function (response) {
  //     return response.text();
  // })
  // .then(function (text) {

  //     console.log('POST response: ');

  //     // Should be 'OK' if everything was successful
  //     console.log(text);
  // });

    for (var k = 0; k < res.length; k++) {
  
      var p = document.createElement('p');
      p.innerHTML = res[k];
      document.getElementById('results=here').appendChild(p);
  
  }

}