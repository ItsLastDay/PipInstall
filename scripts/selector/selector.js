
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
	var grade = document.getElementById("grade");
	var author = document.getElementById("author");



	var iterator = 0;
	renderValues();

	truthful.onclick = function(){
		add_to_array(truthful_array);
	};

	not_truthful.onclick = function() {
		add_to_array(not_truthful_array);
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


	function add_to_array(array) {

		array.push(data[iterator]);

		while (data[++iterator] && data[iterator].grade < 1);

		if (iterator == data.length) {
			alert("array is empty!");
			return;
		}

		renderValues();
	}


	function renderValues() {
		pro.innerHTML = data[iterator].pro;
		contra.innerHTML = data[iterator].contra;
		text.innerHTML = data[iterator].text;
		grade.innerHTML = data[iterator].grade + 3; // -2 .. 2
		author.innerHTML = data[iterator].author;
	}
}



