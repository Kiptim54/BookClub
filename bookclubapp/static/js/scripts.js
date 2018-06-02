$(document).ready(function(){
    $("form").submit(function(event){
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
