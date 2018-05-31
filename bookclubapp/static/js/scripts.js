$(document).ready(function(){
    $('form').submit(function(event){
        event.preventDefault()

        $.ajax({
            'path':'/ajax/comment/',
            'type':'POST',
            'data':form.serialize(),
            'dataType':'json',
            'success':function(data){
                alert(data['success'])
            },

        })
    });
});