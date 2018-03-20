function process(){
	
	chesis = document.getElementById('s').value;
	
	var xhttp = new XMLHttpRequest();
	xhttp.onreadystatechange = function() {
		
	var main_arr = JSON.parse(this.responseText);	
	
	var arr = main_arr[0];
	
	document.getElementById('details').innerHTML="Name: "+arr.name+"\nAddress: "+arr.add+"\nMobile: "+arr.mobile;
		
	}
	
	var request = "http://android23235616.pythonanywhere.com/get_location?chesis="+chesis;
	
		xhttp.open("GET", request, true);
		xhttp.send();
		
	

	
}