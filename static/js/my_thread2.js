var i=0;
var chesis  = "1234";





onmessage = function(e){
	
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if ((this.readyState == 4 && this.status == 200)||i==0) {
			
			if(typeof(e)!=="undefined"){
			
			console.log(this.responseText);
			}
			
			if(typeof(e)!=="undefined"){
				console.log(typeof(e.data));
				chesis = e.data;
				console.log("not undefined");
			}else{
				console.log("undefined");
			}           
            var myArr = JSON.parse(this.responseText);			
			postMessage(myArr);
			
       }else{
		   console.log("error");
	   }
    };
	

	
	var request = "http://android23235616.pythonanywhere.com/get_real_location?chesis="+chesis;
	console.log(request);
	
	xhttp.open("GET", request, true);
	xhttp.send();
	
	setTimeout(onmessage,800);
	
}

