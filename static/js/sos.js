window.onload = process;
var text="";
function process(){
	
	var xhttp = new XMLHttpRequest();
	
	
	
	xhttp.onreadystatechange = function(){
		
		console.log(this.responseText);
		
		var mainArr = JSON.parse(this.responseText);
		
		for (var i=0; i<mainArr.length; i++){
			
			victim = '/delete?id='+mainArr[i].id;
			
			text = text + '<tr><th>' + mainArr[i].name + '</th> <th>' + mainArr[i].chesis + '</th> <th>' + mainArr[i].ssos + '</th><th> ' + mainArr[i].gender + '</th><th> <form action="/index2" method="get"> <input type="hidden" name="name" value="' + mainArr[i].name + '"/><input type="hidden" name="s" value="' + mainArr[i].chesis + '" /> <input type="hidden" name="said" value="' +mainArr[i].said + '" /> <input type="hidden" name="gender" value="' + mainArr[i].ssos + '"/> <input type="submit" name="submit" value="TRACK"/></th><th></form><a href='+victim+'>Sorted</th></tr>';
			//text = text + '<tr><th>' + mainArr[i].name + '</th> <th>' + mainArr[i].chesis + '</th> <th>' + mainArr[i].ssos + '</th><th> ' + mainArr[i].gender + '</th><th> <form action="/index2" method="get"> <input type="hidden" name="name" value="' + mainArr[i].name + '"/><input type="hidden" name="s" value="' + mainArr[i].chesis + '" /> <input type="hidden" name="said" value="' +mainArr[i].said + '" /> <input type="hidden" name="gender" value="' + mainArr[i].ssos + '"/> <input type="submit" name="submit" value="TRACK"/></th><th><a href='+victim+'>Sorted</th></tr>';
		}
		
		//document.getElementById('display').innerHTML = "<ul style='list-style-type:disc'>";
		
		document.getElementById('display').innerHTML = text;

		
		
		
		//document.getElementById('display').innerHTML = myTemp+"</ul>";
		
			
			
			
		
	};
	xhttp.open("GET","http://android23235616.pythonanywhere.com/emergency",true);
	
	xhttp.send();	
}

function deleter( chesis){
}