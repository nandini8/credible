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