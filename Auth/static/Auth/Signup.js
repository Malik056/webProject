$(document).ready(function (){
    //alert("Alert");
    var el = document.getElementById('newsFeed');
    var fe = document.getElementById('feed');

    
    $(window).scroll(function() {
        //alert("bottom!");
        if($(window).scrollTop() + $(window).height() == $(document).height()) {
            // alert("bottom!");
            var cln= fe.cloneNode(true);
            fe.parentNode.appendChild(cln);
        }
    });
});



