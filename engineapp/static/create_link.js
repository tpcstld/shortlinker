function handleSubmit() {
    var button = document.getElementById( "submit-button" );
    button.innerHTML = "Processing...";
    button.disabled = true;
    document.getElementById( "shortlink-link" ).style.display = "none";
	
	createShortlink();
}

function createShortlink() {
    $.ajax( {
        url: "generate_link",
        type: "POST",
        data: $("form[name='shortlink-form']").serialize(),
        success: function( data ) {
            var downloadMessage = document.getElementById( "shortlink-link" );
            downloadMessage.classList.toggle( "error", false );
            downloadMessage.innerHTML = data;
        },
        error: function( jqXHR, textStatus, errorThrown ) {
            var downloadMessage = document.getElementById( "shortlink-link" );
            if ( errorThrown == "Bad Request" ) {
                downloadMessage.innerHTML = jqXHR.responseText;
            } else {
                downloadMessage.innerHTML = "<b>An internal error has occured!</b>"
            }
            downloadMessage.classList.toggle( "error", true );
        },
        complete: function( data ) {
            var downloadMessage = document.getElementById( "shortlink-link" );
            downloadMessage.style.display = "block";
            var button = document.getElementById( "submit-button" );
            button.innerHTML = "Start";
            button.disabled = false;
        }
    } );
}