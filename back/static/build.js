$("#add").on("click",function(e){
    e.preventDefault;

    var user_data = {
        usuario: $('#usuario').val(),
        email: $('#email').val(),
        senha: $('#senha').val()
    };

    $.ajax({
        url:"http://127.0.0.1:5000/account",
        type: "POST",
        data: JSON.stringify(user_data),
        dataType: "json",
        contentType: "application/json",
        complete: function(response){
            alert(response["responseText"])
            location.reload(true)
        }
    })
});

$("#edit").on("click",function(e){
    e.preventDefault;
    
    var user_data = {
        id: $('#id').val(),
        usuario: $('#usuario').val(),
        email: $('#email').val(),
        senha: $('#senha').val()
    };

    $.ajax({
        url:"http://127.0.0.1:5000/account",
        type: "PUT",
        data: JSON.stringify(user_data),
        dataType: "json",
        contentType: "application/json",
        complete: function(response){
            alert(response["responseText"])
            location.reload(true)
        }
    })
});

$("#delete").on("click",function(e){
    e.preventDefault;
    
    var id = $('#id').val()

    $.ajax({
        url:`http://127.0.0.1:5000/account/${id}`,
        type: "DELETE",
        complete: function(response){
            alert(response["responseText"])
            location.reload(true)
        }
    })
});