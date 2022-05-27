//JavaScript for Signup form
$("form[name=signup_form").submit( async(e)=> {
    e.preventDefault();
    $('#loader2').show();

    var form = document.getElementById('myForm')
    var imgURI = takepicture();
    stopVideo();

    var formData = new FormData(form);
    formData.append("file", imgURI);

    const res = await fetch('/user/signup', {
        method: 'POST',
        body: formData
    });
    const stat = await res.json();    
    console.log(stat)
    if(stat.sucess)
    {
        $('#loader2').hide();
        window.location.href = "/user/login-recog";
    }    
    if(stat.error)
    {
        $('#loader2').hide();
        var er = document.getElementById('er')
        er.innerHTML = stat.error
        er.classList.remove('error--hidden')
    } 

});


//JavaScript for Quick-Login
$("form[name=login_recog_form").submit( async(e)=> {
    e.preventDefault();
    $('#loader2').show();

    var imgURI = takepicture();
    stopVideo();

    var formData = new FormData();
    formData.append("file3", imgURI);

    const res = await fetch('/user/login-recog', {
        method: 'POST',
        body: formData
    });
    const stat = await res.json();    
    console.log(stat)   
    if(stat._id)
    {
        $('#loader2').hide();
        window.location.href = "/dashboard/";
    }
    if(stat.error)
    {
        $('#loader2').hide();
        console.log(stat.error)
        var er = document.getElementById('er2')
        er.innerHTML = stat.error
        er.classList.remove('error--hidden')


    }   

});





