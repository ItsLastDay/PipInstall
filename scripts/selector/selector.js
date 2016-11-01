
var data = [];

var input = document.getElementById("fileinput");
input.onchange = function() {
	var file = event.target.files[0];
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

	var pros = document.getElementById("pros");
	var cons = document.getElementById("cons");
	var comments = document.getElementById("comments");



	var iterator = 0;
	pros.innerHTML = data[0].pros;
	cons.innerHTML = data[0].cons;
	comments.innerHTML = data[0].comments;



	truthful.onclick = function(){
		truthful_array.push(data[iterator]);
		++iterator;
		if (iterator == data.length) {
			alert("array is empty!");
			return;
		}
		pros.innerHTML = data[iterator].pros;
		cons.innerHTML = data[iterator].cons;
		comments.innerHTML = data[iterator].comments;
	};

	not_truthful.onclick = function() {
		not_truthful_array.push(data[iterator]);
		++iterator;
		if (iterator == data.length) {
			alert("array is empty!");
			return;
		}
		pros.innerHTML = data[iterator].pros;
		cons.innerHTML = data[iterator].cons;
		comments.innerHTML = data[iterator].comments;
	};

	var saveButton = document.getElementById("save");
	saveButton.onclick = function() {
		var json = JSON.stringify(truthful_array),
			blob = new Blob([json], {type: "text/plain;charset=utf-8"});

		saveAs(blob, "truthful.txt" );


		json = JSON.stringify(not_truthful_array);
		blob = new Blob([json], {type: "text/plain;charset=utf-8"});

		saveAs(blob, "not_truthful.txt" )

	};
}



