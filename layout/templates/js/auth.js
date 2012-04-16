if(typeof(hyperload) == "undefined"){
    hyperload = {};
};

hyperload._auth = function(){
    this.logout = function(){
        $.get("/auth/logout", function(data){
            window.location = data;
        });
    };

    this.login = function(loginType){
        if(loginType == "fb"){
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
        }else if(loginType == "ggl"){
        };
    };
};

hyperload.auth = new hyperload._auth();