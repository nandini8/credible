function newsLoader(data) {
    var xmlhttp = new XMLHttpRequest();

    xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        
        var Obj = JSON.parse(this.responseText);
        
        document.getElementById("title").innerHTML = Obj.title;
        document.getElementById("content").innerHTML = Obj.content;
        document.getElementById("like").innerHTML = Obj.like;
        document.getElementById("share").innerHTML = Obj.share;
        document.getElementById("date").innerHTML = Obj.engagement_id;
        document.getElementById("credibility").innerHTML = Obj.credibility;
        }
    };

    xmlhttp.open("GET", "api/article/" + data, true);
    xmlhttp.send();
}

/*
var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
        
        var Obj = JSON.parse(this.responseText);
        
        var curDiv = document.getElementById("main_footer");
        
        var newDiv1 = document.createElement('div');
        var newContent1 = document.createTextNode(Obj.title);
        newDiv1.appendChild(newContent1);
        document.body.insertBefore(newDiv1, curDiv);
        
        var newDiv2 = document.createElement('div');
        var newContent2 = document.createTextNode(Obj.content);
        newDiv2.appendChild(newContent2);
        document.body.insertBefore(newDiv2, curDiv);
        
        var newDiv3 = document.createElement('div');
        var newContent3 = document.createTextNode(Obj.content);
        newDiv3.appendChild(newContent3);
        document.body.insertBefore(newDiv3, curDiv);
        
    }
};

xmlhttp.open("GET", "json/dummy.json", true);
xmlhttp.send();

*/