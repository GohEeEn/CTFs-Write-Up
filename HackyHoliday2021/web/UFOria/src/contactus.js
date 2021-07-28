function contactus() {

	var code = prompt("This option is invitation only. Enter your invite code:");

	var verify = (function(code) {
	    if (code.length != 12) { return false; }

	    var parts = [code.substr(0,3), code.substr(4,4), code.substr(9,3)]; 
	    if (parts.join("-") != code) { return false; }								// 1st Flag : UFO-VUZP-234

	    if (parts[0] != "UFO") { return false; }								// UFO
	    if (parts[1] != btoa("UFO")) { return false; }								// VUZP
	    if (parts[2] != ("UFO".charCodeAt(0) + "UFO".charCodeAt(1) + "UFO".charCodeAt(2))) { return false; }	// 234

	    return true;
	})(code);

	if (verify) {
	    alert("Great, please continue the booking process by sending us an email with your invitation code.")        
	} else {
	    alert("Wrong invite code.")
	}
}

