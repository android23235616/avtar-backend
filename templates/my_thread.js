var i=0;
var chesis  = "1234";


onmessage = function(e){
	
	var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function() {
        if ((this.readyState == 4 && this.status == 200)||i==0) {
			
			if(typeof(e)!=="undefined"){
			
			//.log(this.responseText);
			}
			
			if(typeof(e)!=="undefined"){
				//.log(typeof(e.data));
				chesis = e.data;
				//.log("not undefined");
			}else{
				//.log("undefined");
			}           
            var myArr = JSON.parse(this.responseText);			
			postMessage(myArr[myArr.length-1-i]);
			if(i<myArr.length){
				i++;
			}else{
				i=0;
			}
       }else{
		   //.log("error");
	   }
    };
	

	
	var request = "http://android23235616.pythonanywhere.com/get_location?chesis="+chesis;
	//.log(request);
	
	xhttp.open("GET", request, true);
	xhttp.send();
	
	setTimeout(onmessage,2000);
	
}

