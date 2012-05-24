function addResource(id, alias, domain, isVerified){
    var resourceHtml = "<tr>" +
        "<td>" + alias + "</td>" + 
        "<td>" + domain + "</td>";
        
    if(isVerified){
        resourceHtml += "<td id=\"is-verified-resource_" + id + "\">Verified</td>";
    }else{
        resourceHtml += "<td id=\"is-verified-resource_" + id + "\">" +
			"<button id=\"verify_resource_" + id + "\">Verify</button></td>";
    };

	resourceHtml += "<td>" +
			"<div class=\"row\">" +
				"<div class=\"span6\">" +
					"<button id=\"remove_resource_" + id + "\">Remove</button>" +
				"</div>" +
				"<div class=\"span6\">" +
					"<button id=\"resource_jobs_" + id + "\">Jobs</button>" +
				"</div>" +
			"</div>" +
		"</td></tr>";
    
    $("#resources tbody").append(resourceHtml);
    $("#verify_resource_" + id).button().click(function() {
        var verifyDialog = $('{% include "dialogs/verifyresource.html"%}');
		verifyDialog.children("#verificationFileLnk").attr("href", "/resources/getverificationfile/" + id);
		verifyDialog.dialog({
			autoOpen: false,
			height: 400,
			width: 450,
			modal: true,
			buttons: {
				"Verify": function() {
					var self = this;
					
					$.get("/resources/verify/" + id, function(data){
						if(Boolean(Number(data))){
							$("#is-verified-resource_" + id).html("Verified");
							$(self).dialog( "close" );
						}else{
							alert("Cannot verify");
						}
					});
				},
				Cancel: function() {
					$(this).dialog("close");
				}
			}
		}).dialog( "open" );
	});
	$("#remove_resource_" + id).button().click(function(){
		$.get("/resources/remove/" + id);
		$(this).parent().parent().remove();
	});
	$("#resource_jobs_" + id).button().click(function(){
	});
};

{% include "js/access.js"%}