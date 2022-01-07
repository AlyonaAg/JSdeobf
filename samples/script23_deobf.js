var var0 = ['PENFTlRFUj4=', 'PEgxPtCU0L7QsdGA0L7QtSAt0YvQuSA=', 'KNCg0LDQvdC90LXQtSkg0KPRgtGA0L4=', '0KPRgtGA0L4=', '0JTQtdC90Yw=', '0JLQtdGH0LXRgA==', 'ITwvSDE+', '0JLRiyDQstC+0YjQu9C4INGB0Y7QtNCwIA==', 'PC9DRU5URVI+', '0K/QvdCy0KTQtdCy0JzRgNGC0JDQv9GA0JzQsNC50JjRjtC90JjRjtC70JDQstCz0KHQtdC90J7QutGC0J3QvtGP0JTQtdC6', 'PENFTlRFUj4=', 'PFRBQkxFIEJPUkRFUj4=', 'PFRSPjxUSCBDT0xTUEFOPTc+', 'LiA=', 'PFRSPjxUSD7QktGB0Lo8VEg+0J/QvtC9PFRIPtCS0YLRgDxUSD7QodGA0LQ8VEg+0KfRgtCyPFRIPtCf0YLQvTxUSD7QodCx0YI=', 'PFRSPg==', 'PFREPg==', 'PFREPg==', 'PEZPTlQgQ09MT1I9XCJyZWRcIj4=', 'PC9GT05UPg==', 'PFRSPg==', 'PC9UQUJMRT4=', 'PC9DRU5URVI+', 'PGJyPg==', ''];
function function1(var11){
	return decodeURIComponent(escape(window.atob(var0[var11])));
}

function function5(var36){
	var var4 = new Date();
	var var16 = var4.getHours();
	document.writeln(function1(0));
	document.write(function1(1));
	if (var16 < 6)
		document.write(function1(2));
	else
		if (var16 < 12)
			document.write(function1(3));
	else
		if (var16 <= 18)
			document.write(function1(4));
	else
		document.write(function1(5));
	document.writeln(function1(6));
	document.write(function1(7));
	var37 = var4.toLocaleString();
	document.write(var37);
	document.writeln(function1(8));
}

function function9(var35, var56, var7, var30, var10, var24, var57, var55, var6, var41, var15, var44){
	var5[0] = var35;
	var5[1] = var56;
	var5[2] = var7;
	var5[3] = var30;
	var5[4] = var10;
	var58 = 35;
	while (var58 < 237)
		switch (var58){
			case (35):
				var58 = 100;
				break;
			case (100):
				var58 = 237;
				var5[5] = var24;
				break;
			case (84):
				document.write(function1(24));
				document.write(function1(1));
				document.write(function1(1));
				document.write(var29);
				var9 = 0;
				document.write(function1(17));
				break;
		}
	var5[6] = var57;
	var5[7] = var55;
	var5[8] = var6;
	var5[9] = var41;
	var5[10] = var15;
	var59 = 196;
	while (var59 < 205)
		switch (var59){
			case (196):
				var59 = 66;
				break;
			case (66):
				var59 = 205;
				var5[11] = var44;
				break;
			case (126):
				var29 = var4.getYear() + 1900;
				document.write(function1(13));
				var5[2] = var7;
				var2 <= var3;
				document.writeln(function1(0));
				var9 = 0;
				break;
		}
}

function function11(var36){
	var var14 = function1(9);
	var var4 = new Date();
	var var28;
	var var17 = new function9(31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31);
	var29 = var4.getYear() + 1900;
	var28 = var4.getDate();
	if (((var29 % 4 == 0) && (var29 % 100 != 0)) || (var29 % 400 == 0))
		var17[1] = 29;
	var3 = var17[var4.getMonth()];
	var25 = var4;
	var25.setDate(1);
	var46 = var25.getDate();
	if (var46 == 2)
		var25.setDate(0);
	var8 = var25.getDay();
	document.writeln(function1(10));
	document.write(function1(11));
	var64 = 143;
	while (var64 < 342)
		switch (var64){
			case (143):
				var64 = 135;
				break;
			case (135):
				var64 = 342;
				document.write(function1(12));
				break;
		}
	document.write(var14.substring(var4.getMonth() * 3, (var4.getMonth() + 1) * 3));
	document.write(function1(13));
	var65 = 193;
	while (var65 < 366)
		switch (var65){
			case (193):
				var65 = 178;
				break;
			case (178):
				var65 = 366;
				document.write(var29);
				break;
		}
	document.write(function1(14));
	document.write(function1(15));
	var66 = 6;
	while (var66 < 330)
		switch (var66){
			case (6):
				var66 = 130;
				break;
			case (130):
				var66 = 330;
				var9 = 0;
				break;
			case (124):
				document.writeln(function1(0));
				break;
		}
	for (var2 = 0; var2 < var8; var2++ )
	{
		document.write(function1(16));
		var9++ ;
	}
	for (var2 = 1; var2 <= var3; var2++ )
	{
		document.write(function1(17));
		if (var2 == var28)
			document.write(function1(18));
		document.write(var2);
		if (var2 == var28)
			document.write(function1(19));
		var9++ ;
		if (var9 == 7)
		{
			document.write(function1(20));
			var9 = 0;
		}
	}
	document.write(function1(21));
	document.writeln(function1(22));
}

function5();
document.write(function1(23));
function11();
document.write(function1(24));