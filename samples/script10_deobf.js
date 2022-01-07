var var0 = ['QmFuYW5h', 'T3Jhbmdl', 'QXBwbGU=', 'TWFuZ28=', 'PHVsPg==', 'PGxpPg==', 'PC9saT4=', 'PC91bD4=', 'ZGVtbw=='];
function function3(var17){
	return decodeURIComponent(escape(window.atob(var0[var17])));
}

var var2, var3, var4, var5;
var2 = [function3(0), function3(1), function3(2), function3(3)];
var4 = var2.length;
var18 = 145;
while (var18 < 327)
	switch (var18){
		case (145):
			var18 = 194;
			break;
		case (194):
			var18 = 327;
			var3 = function3(4);
			break;
	}
for (var5 = 0; var5 < var4; var5++ )
	var3 += function3(5) + var2[var5] + function3(6);
var3 += function3(7);
document.getElementById(function3(8)).innerHTML = var3;