document.onreadystatechange = function () {
if (document.readyState == "complete") {
    var is_auth = false;
    var is_reg = false;
    var upd_twit_id = null;
    var upd_twit_text = null;


    $('body').on('click', 'a[href^=\\/main\\/del\\/]', function(event) {
        event.preventDefault();
        
        var result = $(this).attr('href').search( "/del/(.*)/i" );        
        var url = $(this).attr('href');
        var id = $(this).attr('id');
        var name = $(this).attr('name');
        $.ajax({
            url: "/main/del/",
            method: "POST",
            data: {"del": $(this).attr("id") },
            dataType: "json",
            
            success: function(data) 
            { 
                if ("ID" in data )
                {
                    $("#list_item_"+data["ID"]).slideToggle(200);
                }
                else
                {
                    var snackbarContainer = document.querySelector('#demo-toast-example');
                    snackbarContainer.MaterialSnackbar.showSnackbar({message: data["error"]});
                }
            },
            error: function(){ 
                snackbarContainer.MaterialSnackbar.showSnackbar({message: "Something wrong. page will be reload"});
                location.reload();
            }
        });
        return false;
    });


    $('body').on('click', '#add_new_user_btn', function(event) {
        event.preventDefault();
        var url = $(this).parent().attr('action');        
        $.ajax({
            url: $(this).parent().attr('action'),
            method: $(this).parent().attr('method'),            
            data: $("#add_user_form").serialize(),  
            dataType: "json",
            success: function(data) 
            { 
                var res_json = data
                console.log( res_json );    
                if ( "error" in res_json )
                {  
                    var snackbarContainer = document.querySelector('#demo-toast-example');
                    snackbarContainer.MaterialSnackbar.showSnackbar({message: res_json["error"]});
                }
                else
                {
                    var elem = document.getElementById('temp_list_item').innerHTML;
                    elem = elem.replace("ID", res_json["ID"])                     
                    elem = elem.replace("USERNAME", res_json["USERNAME"])                     
                    $( "#list_items" ).append( elem );
                    document.getElementById('add_user_form').reset();
                }
            },
            error: function()
            {
                snackbarContainer.MaterialSnackbar.showSnackbar({message: "Something wrong. page will be reload"});
                location.reload();
            }
        });
        return false;
    });



}
}