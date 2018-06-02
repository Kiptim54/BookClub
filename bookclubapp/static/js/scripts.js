$(document).ready(function(){
    $("form").submit(function(event){
        event.preventDefault()
        form = $("form")
        var url = document.getElementById('endpoint-url-div').getAttribute('action');
    
    $.ajax({
        'url':url,
        'type':'POST',
        'data':form.serialize(),
        'dataType':'json',
        'success': function(comment, user){
            console.log(comment)
          $("#comments").prepend("comment.comment")
        },

    })
})

})