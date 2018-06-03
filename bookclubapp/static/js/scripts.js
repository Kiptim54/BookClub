$(document).ready(function(){
    $("#endpoint-url-div").submit(function(event){
        event.preventDefault()
        event.stopImmediatePropagation();
        form = $("form")
        var url = document.getElementById('endpoint-url-div').getAttribute('action');
    
    $.ajax({
        'url':url,
        'type':'POST',
        'data':$(this).serialize(),
        'dataType':'json',
        'success': function(response){
            console.log(response)
          $("#comments").prepend(`<p>${response.user}~~${response.comment}</p><p>${response.time_posted}</p>`)
          $("form")[0].reset()
        },

    })
})

});
$(function() {


    // This function gets cookie with a given name
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie != '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = jQuery.trim(cookies[i]);
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) == (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    /*
    The functions below will create a header with csrftoken
    */

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }
    function sameOrigin(url) {
        // test that a given url is a same-origin URL
        // url could be relative or scheme relative or absolute
        var host = document.location.host; // host + port
        var protocol = document.location.protocol;
        var sr_origin = '//' + host;
        var origin = protocol + sr_origin;
        // Allow absolute or scheme relative URLs to same origin
        return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
            (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
            // or any other URL that isn't scheme relative or absolute i.e relative.
            !(/^(\/\/|http:|https:).*/.test(url));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                // Send the token to same-origin, relative URLs only.
                // Send the token only if the method warrants CSRF protection
                // Using the CSRFToken value acquired earlier
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

});

// for the random questions to pop up
$(document).ready(function(){
    $(".randoms").submit(function(event){
        event.preventDefault()
        event.stopImmediatePropagation();
        form = $("form")
        var url = document.getElementById('randomquestions').getAttribute('action');
    
    $.ajax({
        'url':url,
        'type':'POST',
        'data':$(this).serialize(),
        'dataType':'json',
        'success': function(response){
            console.log(response)
          $(".questions").text(response.Question)
          $("form")[0].reset()
        },

    })
})

});
$(document).ready(function(){
    $("#formbooks").submit(function(event){
        event.preventDefault();
        event.stopImmediatePropagation();
        form = $("form")
        var url = document.getElementById('formbooks').getAttribute('action');
    
    $.ajax({
        'url':url,
        'type':'GET',
        'data':$(this).serialize(),
        'dataType':'json',
        'success': function(response){
            $(".new").empty()
            for(i=0; i<10; i++){
                console.log(JSON.stringify(response))
                // alert(JSON.stringify(response[i].volumeInfo.title))
                
                $(".searched").hide()
                $(".new").append(` <img style="display:inline-block; height: 100%; width:auto;" class="img-responsive" src=${JSON.stringify(response[i].volumeInfo.imageLinks.smallThumbnail)} alt="here"/>`)
                $("form")[0].reset()
           

            }
        },

    })
})

});
