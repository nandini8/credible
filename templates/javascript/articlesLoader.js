var xmlhttp = new XMLHttpRequest();

xmlhttp.onreadystatechange = function () {
    if (this.readyState === 4 && this.status === 200) {

        var obj = JSON.parse(this.responseText);

        document.getElementById("title_0").innerHTML = obj[0].title;
        document.getElementById("cred_0").innerHTML = obj[0].credibility;
        document.getElementById("content_0").innerHTML = obj[0].content;
        document.getElementById("title_1").innerHTML = obj[1].title;
        document.getElementById("cred_1").innerHTML = obj[1].credibility;
        document.getElementById("content_1").innerHTML = obj[1].content;
        document.getElementById("title_2").innerHTML = obj[2].title;
        document.getElementById("cred_2").innerHTML = obj[2].credibility;
        document.getElementById("content_2").innerHTML = obj[2].content;
        document.getElementById("title_3").innerHTML = obj[3].title;
        document.getElementById("cred_3").innerHTML = obj[3].credibility;
        document.getElementById("content_3").innerHTML = obj[3].content;
        document.getElementById("title_4").innerHTML = obj[4].title;
        document.getElementById("cred_4").innerHTML = obj[4].credibility;
        document.getElementById("content_4").innerHTML = obj[4].content;
        document.getElementById("title_5").innerHTML = obj[5].title;
        document.getElementById("cred_5").innerHTML = obj[5].credibility;
        document.getElementById("content_5").innerHTML = obj[5].content;
        document.getElementById("title_6").innerHTML = obj[6].title;
        document.getElementById("cred_6").innerHTML = obj[6].credibility;
        document.getElementById("content_6").innerHTML = obj[6].content;
        document.getElementById("title_7").innerHTML = obj[7].title;
        document.getElementById("cred_7").innerHTML = obj[7].credibility;
        document.getElementById("content_7").innerHTML = obj[7].content;
        document.getElementById("title_8").innerHTML = obj[8].title;
        document.getElementById("cred_8").innerHTML = obj[8].credibility;
        document.getElementById("content_8").innerHTML = obj[8].content;
        document.getElementById("title_9").innerHTML = obj[9].title;
        document.getElementById("cred_9").innerHTML = obj[9].credibility;
        document.getElementById("content_9").innerHTML = obj[9].content;
        document.getElementById("title_10").innerHTML = obj[10].title;
        document.getElementById("cred_10").innerHTML = obj[10].credibility;
        document.getElementById("content_10").innerHTML = obj[10].content;
        document.getElementById("title_11").innerHTML = obj[11].title;
        document.getElementById("cred_11").innerHTML = obj[11].credibility;
        document.getElementById("content_11").innerHTML = obj[11].content;
        document.getElementById("title_12").innerHTML = obj[12].title;
        document.getElementById("cred_12").innerHTML = obj[12].credibility;
        document.getElementById("content_12").innerHTML = obj[12].content;
        document.getElementById("title_13").innerHTML = obj[13].title;
        document.getElementById("cred_13").innerHTML = obj[13].credibility;
        document.getElementById("content_13").innerHTML = obj[13].content;
        document.getElementById("title_14").innerHTML = obj[14].title;
        document.getElementById("cred_14").innerHTML = obj[14].credibility;
        document.getElementById("content_14").innerHTML = obj[14].content;
        document.getElementById("title_15").innerHTML = obj[15].title;
        document.getElementById("cred_15").innerHTML = obj[15].credibility;
        document.getElementById("content_15").innerHTML = obj[15].content;
    }
};

xmlhttp.open("GET", "json/articles.json", true);
xmlhttp.send();
