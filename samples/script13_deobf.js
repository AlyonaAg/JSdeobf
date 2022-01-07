var var0 = ['ZXhwaXJlcz0=', 'PQ==', 'Ow==', 'O3BhdGg9Lw==', 'PQ==', 'Ow==', 'IA==', '', 'dXNlcm5hbWU=', '', 'V2VsY29tZSBhZ2FpbiA=', 'UGxlYXNlIGVudGVyIHlvdXIgbmFtZTo=', '', '', 'dXNlcm5hbWU='];
function function0(var1){
	return decodeURIComponent(escape(window.atob(var0[var1])));
}

function function1(var2, var3, var4){
	var var5 = new Date();
	var5.setTime(var5.getTime() + (var4 * 24 * 60 * 60 * 1000));
	var var6 = function0(0) + var5.toGMTString();
	document.cookie = var2 + function0(1) + var3 + function0(2) + var6 + function0(3);
}

function function4(var2){
	var16 = 14;
	while (var16 < 380)
		switch (var16){
			case (14):
				var16 = 191;
				break;
			case (191):
				var16 = 380;
				var var10 = var2 + function0(4);
				break;
			case (113):
				document.cookie = var2 + function0(1) + var3 + function0(2) + var6 + function0(3);
				var5.setTime(var5.getTime() + (var4 * 24 * 60 * 60 * 1000));
				var9 = prompt(function0(11), function0(12));
				break;
		}
	var var12 = decodeURIComponent(document.cookie);
	var var11 = var12.split(function0(5));
	for (var17var8 = 0; var8 < var11.length; var8++ )
	{
		var var13 = var11[var8];
		while (var13.charAt(0) == function0(6))
			var13 = var13.substring(1);
		if (var13.indexOf(var10) == 0)
			return var13.substring(var10.length, var13.length);
	}
	return function0(7);
}