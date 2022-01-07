var var0 = ['', 'PGJyPg==', 'ZGVtbw=='];
function function1(var8){
	return decodeURIComponent(escape(window.atob(var0[var8])));
}

var var5 = 3;
var var4 = function1(0);
while (var5 != Infinity)
{
	var5 = var5 * var5;
	var9 = 154;
	while (var9 < 246)
		switch (var9){
			case (154):
				var9 = 98;
				break;
			case (98):
				var9 = 246;
				var4 = var4 + var5 + function1(1);
				break;
			case (68):
				var var4 = function1(0);
				var4 = var4 + var5 + function1(1);
				var var5 = 3;
				var4 = var4 + var5 + function1(1);
				var5 = var5 * var5;
				var5 = var5 * var5;
				break;
		}
}
document.getElementById(function1(2)).innerHTML = var4;