var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {        
        var Obj = JSON.parse(this.responseText);
        
        document.getElementById("title").innerHTML = Obj[0].title;
        document.getElementById("article_link").innerHTML = Obj[0].article_link;
        document.getElementById("date").innerHTML = Obj[0].date;
        document.getElementById("publisher").innerHTML = Obj[0].publisher;
        document.getElementById("credibility_score").innerHTML = Obj[0].credibility_score;
        document.getElementById("content").innerHTML = Obj[0].content;
        }
    };

    xmlhttp.open("GET", "/api/articles/" + localStorage.getItem('article_id'), true);
    xmlhttp.send();