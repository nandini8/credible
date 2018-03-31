var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {        
        var Obj = JSON.parse(this.responseText);
        
        document.getElementById("title").innerHTML = Obj[0].title;
        document.getElementById("content").innerHTML = Obj[0].content;
        document.getElementById("credibility").innerHTML = Obj[0].credibility_score;
        }
    };

    xmlhttp.open("GET", "http://18.216.28.234:8000/api/articles/" + localStorage.getItem('article_id'), true);
    xmlhttp.send();

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