// map;
var map;
var markers = new Array();
var i=0;
function myMap() {
  var myCenter = new google.maps.LatLng(20.2961,85.8245);
  var mapCanvas = document.getElementById("map");
  var mapOptions = {center: myCenter, zoom: 15};
  map = new google.maps.Map(mapCanvas, mapOptions);
  var marker = new google.maps.Marker({position:myCenter});
  marker.setMap(map);
  
}

function test(lat,lng){



	if(map!=undefined){
		//alert(" not undefined");
	}else{
		alert("undefined");
		 map = new google.maps.Map(mapCanvas, mapOptions);
	}


	
  var myCenter = new google.maps.LatLng(lat,lng);
  var mapCanvas = document.getElementById("map");
  var mapOptions = {center: myCenter, zoom: 25};
  //var map = new google.maps.Map(mapCanvas, mapOptions);
  var marker = new google.maps.Marker({position:myCenter});
  marker.setMap(map);
}

var w;

var mainChesis = "1234";
function startThread(){
	
	//.log("hello");

	if(typeof(Worker)!=="undefined"){
		if(typeof(w)=="undefined"){
			w = new Worker("my_thread.js");
			
			//w = new Worker("{{url}}");
					
		}
		
		w.postMessage(mainChesis);
		
		w.onmessage = function(event){
			
			
			
			document.getElementById("display").innerHTML=event.data.lng+" , "+event.data.lat;
			//test(event.data.lat,event.data.lng);
			
			var myCenter = new google.maps.LatLng(event.data.lat,event.data.lng);
			var mapCanvas = document.getElementById("map");
			var mapOptions = {center: myCenter, zoom: 15};
			var map = new google.maps.Map(mapCanvas, mapOptions);
			var marker = new google.maps.Marker({position:myCenter});
			
			marker.setMap(map);
		};
	}

}


function startThread2(ch){
	
	
	//.log("hello");

	if(typeof(Worker)!=="undefined"){
		if(typeof(w)=="undefined"){
			w = new Worker("my_thread.js");
			
			//w = new Worker("{{url}}");
					
		}
		
		w.postMessage(ch);
		var map;
		
		w.onmessage = function(event){
			
			
			document.getElementById("display").innerHTML=event.data.lng+" , "+event.data.lat;
			//test(event.data.lat,event.data.lng);
			
			var myCenter = new google.maps.LatLng(event.data.lat,event.data.lng);
			var mapCanvas = document.getElementById("map");
			var mapOptions = {center: myCenter, zoom: 18,
			styles: [
            {elementType: 'geometry', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.stroke', stylers: [{color: '#242f3e'}]},
            {elementType: 'labels.text.fill', stylers: [{color: '#746855'}]},
            {
              featureType: 'administrative.locality',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'geometry',
              stylers: [{color: '#263c3f'}]
            },
            {
              featureType: 'poi.park',
              elementType: 'labels.text.fill',
              stylers: [{color: '#6b9a76'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry',
              stylers: [{color: '#38414e'}]
            },
            {
              featureType: 'road',
              elementType: 'geometry.stroke',
              stylers: [{color: '#212a37'}]
            },
            {
              featureType: 'road',
              elementType: 'labels.text.fill',
              stylers: [{color: '#9ca5b3'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry',
              stylers: [{color: '#746855'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'geometry.stroke',
              stylers: [{color: '#1f2835'}]
            },
            {
              featureType: 'road.highway',
              elementType: 'labels.text.fill',
              stylers: [{color: '#f3d19c'}]
            },
            {
              featureType: 'transit',
              elementType: 'geometry',
              stylers: [{color: '#2f3948'}]
            },
            {
              featureType: 'transit.station',
              elementType: 'labels.text.fill',
              stylers: [{color: '#d59563'}]
            },
            {
              featureType: 'water',
              elementType: 'geometry',
              stylers: [{color: '#17263c'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.fill',
              stylers: [{color: '#515c6d'}]
            },
            {
              featureType: 'water',
              elementType: 'labels.text.stroke',
              stylers: [{color: '#17263c'}]
            }
          ]
			
			};
			
			
			
			if(!map)
			map = new google.maps.Map(mapCanvas, mapOptions);
			marker = new google.maps.Marker({position:myCenter,
			icon:'https://thumb.ibb.co/cnA9Cx/a.png',
			label:{
				text:i.toString(),
				color:'white'
			}
			});
			
			marker.setTitle(i.toString());
			
			
			
			markers[i] = marker;
			
			markers[i].setMap(map);
			//alert(i);
			
			if(i!=0){
				markers[i-1].setMap(null);
			}
			
			i++;
			
			document.getElementById('name').innerHTML = event.data.name;
			document.getElementById('mobile').innerHTML = event.data.mobile;
			document.getElementById('add').innerHTML = event.data.add;
			
        
			
		};
	}

}


function stopThread(){
	
	if(typeof(w)!=="undefined")
	w.terminate();
	w = undefined;
	
}


function process(){
	
	var chesis = document.getElementById('chesis').value;
	
	mainChesis = chesis;
	
	//stopThread();
	
	startThread2(chesis);
	
}