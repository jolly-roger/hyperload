function addResource(id, alias, domain, isVerified){
    var resourceHtml = "<tr>" +
        "<td>" + alias + "</td>" + 
        "<td>" + domain + "</td>";
        
    if(isVerified){
        resourceHtml += "<td>" + Verified + "</td>" +
            "</tr>";
    }else{
        resourceHtml += "<td><button id=\"resource_" + id + "\">Verify</button></td>" +
            "</tr>";
    };
    
    $("#resources tbody").append(resourceHtml);
    $("#resource_" + id).button().click(function() {
        $('{% include "dialogs/verifyresource.html"%}').dialog({
			autoOpen: false,
			height: 400,
			width: 450,
			modal: true,
			buttons: {
				"Verify": function() {
                    $( this ).dialog( "close" );
				},
				Cancel: function() {
					$(this).dialog("close");
				}
			}
		}).dialog( "open" );
	});
};

function logout(){
    $.get("/auth/logout", function(data){
        window.location = data;
    });
};

function login(){
    FB.login(function(response) {
        if (response.authResponse && response.authResponse.accessToken &&
            response.authResponse.userID) {
            $.post( "/auth/login", "accessToken=" + response.authResponse.accessToken +
                "&userID=" + response.authResponse.userID, function(data){
                    if(data){
                        window.location = data;
                    }
            });
        } else {
          alert('User cancelled login or did not fully authorize.');
        }
    });
};