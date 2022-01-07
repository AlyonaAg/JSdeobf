var var0 = ['Lg==', 'Lg==', 'MA==', '', '', 'LQ==', 'Kw==', 'Lw==', 'Kg==', 'MS94', 'c3FydA==', 'ZXhw', 'Ky8t', 'PQ==', 'MA==', 'Qw==', 'Lg==', 'MA=='];
function function2(var17){
	return decodeURIComponent(escape(window.atob(var0[var17])));
}

var var2 = 0, var5 = 0, var6 = 0, var7 = 0, var9 = 1, var8 = 0, var18, var3;
function function6(var13){
	document.form1.ekran.value = var13;
	var2 = 0, var5 = 0, var6 = 0, var7 = 0;
	var9 = 1;
	var8 = 0;
}

function function8(var14){
	var18 = 1;
	if (var6 || var9)
	{
		var6 = 0;
		var9 = 0;
		var3 = var14;
	}
	for (var30var20 = 0; var20 < var3.length; var20++ )
		if (var3[var20] == function2(0))
			var18 = 0;
}