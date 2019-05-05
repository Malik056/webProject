
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

function validateEmail(email)
{
    var pattern=/([A-z]|[0-9])+@([A-z]|[0-9])+.([a-z]|[0-9])+/i;
    //alert(pattern);
    return pattern.test(email);
}

function validateLoginForm()
{
    var form=document.getElementById('loginForm');
    var email=document.getElementById('email');
    var password=document.getElementById('pwd');
    console.log(email.value);
    if(!validateEmail(email.value))
    {
        alert("Email is not valid");
    }
    else
    {
        //form.action="{% url 'Auth:signup' "+email.value+" "+password.value+"%}";
        //return true;
    }
}