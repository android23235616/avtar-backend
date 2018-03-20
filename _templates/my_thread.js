var i=0;

onmessage = function(e){
	
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
           
            var myArr = JSON.parse(this.responseText);
			
			var main_arr = myArr[myArr.length-1];
			
			postMessage(main_arr["lat"],main_arr["lng"]);
       }
    };
	
	xhttp.open("GET", "http://android23235616.pythonanywhere.com/get_location?chesis=1234", true);
	xhttp.send();
	
	setTimeout(onmessage,4000);
	
}

