// LOAD PAGE
$('#build-id').click(function(){

    const id = $("#build-id").val();

    $.getJSON(`http://127.0.0.1:5000/build_api/${id}`, function(data){
        document.getElementById("helmet").value = data["helmet"];
        document.getElementById("body-armor").value = data["body"];
        document.getElementById("gloves").value = data["gloves"];
        document.getElementById("boots").value = data["boots"];
        document.getElementById("main-hand").value = data["main_hand"];
        document.getElementById("off-hand").value = data["off_hand"];
        document.getElementById("amulet").value = data["amulet"];
        document.getElementById("ring").value = data["ring"];
        document.getElementById("belt").value = data["belt"];
    })
});



// BUTTONS

$("#add").on("click",function(e){
    e.preventDefault;

    var build_data = {
        name: $('#build-name').val(),
        helmet: $('#helmet').val(),
        body: $('#body-armor').val(),
        gloves: $('#gloves').val(),
        boots: $('#boots').val(),
        main_hand: $('#main-hand').val(),
        off_hand: $('#off-hand').val(),
        amulet: $('#amulet').val(),
        ring: $('#ring').val(),
        belt:$('#belt').val()
    }; 

    for (const [key,value] of Object.entries(build_data)){
        if (value !== "null" && key !== "name"){
            build_data[key]= parseInt(value)
        };
    };


    $.ajax({
        url:"http://127.0.0.1:5000/build",
        type: "POST",
        data: JSON.stringify(build_data),
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
    
    var build_data = {
        id: $('#build-id').val(),
        name: $("option:selected",$("#build-id")).text(),
        helmet: $('#helmet').val(),
        body: $('#body-armor').val(),
        gloves: $('#gloves').val(),
        boots: $('#boots').val(),
        main_hand: $('#main-hand').val(),
        off_hand: $('#off-hand').val(),
        amulet: $('#amulet').val(),
        ring: $('#ring').val(),
        belt:$('#belt').val()
    }; 

    for (const [key,value] of Object.entries(build_data)){
        if (value !== "null" && key !== "name"){
            build_data[key]= parseInt(value)
        };
    };

    $.ajax({
        url:"http://127.0.0.1:5000/build",
        type: "PUT",
        data: JSON.stringify(build_data),
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
    
    var id = $('#build-id').val()

    $.ajax({
        url:`http://127.0.0.1:5000/build/${id}`,
        type: "DELETE",
        complete: function(response){
            alert(response["responseText"])
            location.reload(true)
        }
    })
});

$("#clear").click(function(e){
    e.preventDefault;
    
    document.getElementById('build-name').value = ''
    document.getElementById('helmet').value = 'null'
    document.getElementById('body-armor').value = 'null'
    document.getElementById('gloves').value = 'null'
    document.getElementById('boots').value = 'null'
    document.getElementById('main-hand').value = 'null'
    document.getElementById('off-hand').value = 'null'
    document.getElementById('amulet').value = 'null'
    document.getElementById('ring').value = 'null'
    document.getElementById('belt').value = 'null'
});




// ALTERATIONS

$('#build-id').on('change', function(e){
    e.preventDefault;

    const id = $("#build-id").val();

    $.getJSON(`http://127.0.0.1:5000/build_api/${id}`, function(data){
        document.getElementById("helmet").value = data["helmet"];
        document.getElementById("body-armor").value = data["body"];
        document.getElementById("gloves").value = data["gloves"];
        document.getElementById("boots").value = data["boots"];
        document.getElementById("main-hand").value = data["main_hand"];
        document.getElementById("off-hand").value = data["off_hand"];
        document.getElementById("amulet").value = data["amulet"];
        document.getElementById("ring").value = data["ring"];
        document.getElementById("belt").value = data["belt"];
    })
});