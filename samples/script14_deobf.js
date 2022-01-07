var var0 = ['dHh0', 'dGltZWRDb3VudCgp'];
function function0(var1){
	return decodeURIComponent(escape(window.atob(var0[var1])));
}

var var2 = 0;
var var3;
var var4 = 0;
function function1(var5){
	var6 = 162;
	while (var6 < 282)
		switch (var6){
			case (162):
				var6 = 125;
				break;
			case (125):
				var6 = 282;
				document.getElementById(function0(0)).value = var2;
				break;
		}
	var2 = var2 + 1;
	var3 = setTimeout(function0(1), 1000);
}