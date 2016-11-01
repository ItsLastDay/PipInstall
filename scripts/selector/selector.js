
var data = [];
var file_name = "";
var input = document.getElementById("fileinput");
input.onchange = function() {
	var file = event.target.files[0];
	file_name = file.name;
	var fr = new FileReader();
	fr.onload = function (e) {
		var parsed = JSON.parse(e.target.result);
		console.dir(parsed);
		data = parsed;
		run_comparison();
	};
	fr.readAsText(file);
};


function run_comparison() {
	var truthful_array = [];
	var not_truthful_array = [];

	var truthful = document.getElementById("truthful");
	var not_truthful = document.getElementById("not_truthful");

	var pro = document.getElementById("pros");
	var contra = document.getElementById("cons");
	var text = document.getElementById("comments");



	var iterator = 0;
	pro.innerHTML = data[0].pro;
	contra.innerHTML = data[0].contra;
	text.innerHTML = data[0].text;



	truthful.onclick = function(){
		truthful_array.push(data[iterator]);
		++iterator;
		if (iterator == data.length) {
			alert("array is empty!");
			return;
		}
		pro.innerHTML = data[iterator].pro;
		contra.innerHTML = data[iterator].contra;
		text.innerHTML = data[iterator].text;
	};

	not_truthful.onclick = function() {
		not_truthful_array.push(data[iterator]);
		++iterator;
		if (iterator == data.length) {
			alert("array is empty!");
			return;
		}
		pro.innerHTML = data[iterator].pro;
		contra.innerHTML = data[iterator].contra;
		text.innerHTML = data[iterator].text;
	};

	var saveButton = document.getElementById("save");
	saveButton.onclick = function() {
		var json = JSON.stringify(truthful_array),
			blob = new Blob([json], {type: "text/plain;charset=utf-8"});

		saveAs(blob,file_name + "_truthful.txt" );


		json = JSON.stringify(not_truthful_array);
		blob = new Blob([json], {type: "text/plain;charset=utf-8"});

		saveAs(blob,file_name + "_not_truthful.txt" )

	};
}



