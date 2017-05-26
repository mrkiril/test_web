document.onreadystatechange = function () {
if (document.readyState == "complete") {

    document.getElementById("gotoregbtn").addEventListener("click", function{
        location.href = '/reg/';

    })
    document.getElementById("gotorembtn").addEventListener("click", function{
        location.href = '/remove/';

    })
}
}