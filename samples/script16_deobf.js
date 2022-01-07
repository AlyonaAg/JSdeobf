var var0 = ['0JzQuNC90L7QvdC+0YHQtdGG', '0KTRgNC10LPQsNGC', '0JrRgNC10LnRgdC10YA=', '0JvQuNC90LrQvtGA', '', 'UHJlbG9hZGluZyBpbWFnZXMuLi5wbGVhc2Ugd2FpdA==', 'YmF0dA==', 'LmdpZg==', '', 'cGM=', 'Xw==', 'YmF0dA==', 'LmdpZg==', 'cGx5', 'Xw==', 'YmF0dA==', 'LmdpZg==', 'PGEgaHJlZj0iamF2YXNjcmlwdDpncmlkQ2xpY2so', 'LA==', 'KTsiPjxpbWcgbmFtZT0icGM=', 'Xw==', 'IiBzcmM9ImJhdHQxMDAuZ2lmIiB3aWR0aD0xNiBoZWlnaHQ9MTY+PC9hPg==', 'PGEgaHJlZj0iamF2YXNjcmlwdDp2b2lkKDApOyI+PGltZyBuYW1lPSJwbHk=', 'Xw==', 'IiBzcmM9ImJhdHQ=', 'LmdpZiIgd2lkdGg9MTYgaGVpZ2h0PTE2PjwvYT4=', 'PGJyPg==', '0JLRiyDQv9C+0YLQvtC/0LjQu9C4INC80L7QuSA=', 'IQ==', '0JLRiyDQstGL0LnQs9GA0LDQu9C4ISDQndCw0LbQvNC40YLQtSDQutC90L7Qv9C60YMgXCLQntCx0L3QvtCy0LjRgtGMXCIK', 'eW/QtNC70Y8g0L3QsNGH0LDQu9CwINC90L7QstC+0Lkg0LjQs9GA0Ysu', '0K8g0L/QvtGC0L7Qv9C40Lsg0JLQsNGIIA==', 'IQ==', '0K8g0LLRi9C50LPRgNCw0LshINCd0LDQttC80LjRgtC1INC60L3QvtC/0LrRgyBcItCe0LHQvdC+0LLQuNGC0YxcIgo=', '0LTQu9GPINC90LDRh9Cw0LvQsCDQvdC+0LLQvtC5INC40LPRgNGLLg==', 'Q29tcHV0ZXIgaGFzIA==', 'LCA=', '0LHQvtC70YzRiNC1INC90LjRh9C10LPQviDQvdC1INC+0YHRgtCw0LvQvtGB0YwuINCh0L/QsNGB0LjQsdC+ISE=', 'PGNlbnRlcj48dGFibGU+PHRyPjx0ZCBhbGlnbj1jZW50ZXI+PHAgY2xhc3M9J2hlYWRpbmcnPtCY0LPRgNC+0LLQvtC1INC/0L7Qu9C1INC60L7QvNC/0YzRjtGC0LXRgNCwPC9wPjwvdGQ+', 'PHRkIGFsaWduPWNlbnRlcj48cCBjbGFzcz0naGVhZGluZyc+0JLQsNGI0LUg0LjQs9GA0L7QstC+0LUg0L/QvtC70LU8L3A+PC90ZD48L3RyPjx0cj48dGQ+', 'PC90ZD48dGQ+', 'PC90ZD48L3RyPjwvdGFibGU+PC9jZW50ZXI+'];
function function3(var50){
	return decodeURIComponent(escape(window.atob(var0[var50])));
}

var var34 = [[[1, 5], [1, 2, 5], [1, 2, 3, 5], [1, 2, 3, 4, 5]], [[6, 10], [6, 7, 10], [6, 7, 8, 10], [6, 7, 8, 9, 10]]];
var var42 = [[[201, 203], [201, 202, 203], [201, 202, 202, 203], [201, 202, 202, 202, 203]], [[204, 206], [204, 205, 206], [204, 205, 205, 206], [204, 205, 205, 205, 206]]];
var var10 = [[function3(0), 2, 4], [function3(1), 3, 4], [function3(2), 4, 2], [function3(3), 5, 1]];
var var8 = 16, var32 = 16;
var var4 = [], var13 = [], var33 = [], var24 = [];
var var51 = 0, var52 = 0, var29 = true;
var var45 = [];
function function4(var53){
	var var25, var44 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 100, 101, 102, 103, 201, 202, 203, 204, 205, 206];
	window.status = function3(5);
	for (var25 = 0; var25 < var44.length; ++ var25)
	{
		var var46 = new Image, var55 = function3(6) + var44[var25] + function3(7);
		var46.var21 = var55;
		var45[var25] = var46;
	}
	window.status = function3(8);
}

function function8(var66){
	var var7, var14;
	var11 = [];
	for (var7 = 0; var7 < var8; ++ var7)
	{
		var11[var7] = [];
		for (var14 = 0; var14 < var8; ++ var14)
			var11[var7][var14] = [100,  - 1, 0];
	}
	var var12 = 0;
	var var23;
	for (var23 = var10.length - 1; var23 >= 0; -- var23)
	{
		var var25;
		for (var25 = 0; var25 < var10[var23][2]; ++ var25)
		{
			var var67 = Math.floor(Math.random() * 2);
			var var36 = var10[var23][1], var68 = var8, var69 = var32, var26 = 0, var70 = 0;
			if (var67 == 0)
			{
				var68 = var8 - var36;
				var26 = 1;
			}
			else
{
				var69 = var32 - var36;
				var70 = 1;
}
			var var14, var7, var3;
			{
				var7 = Math.floor(Math.random() * var69);
				var14 = Math.floor(Math.random() * var68);
				var var15, var16 = var14, var17 = var7;
				var3 = true;
				for (var15 = 0; var15 < var36; ++ var15)
				{
					if (var11[var17][var16][0] < 100)
					{
						var3 = false;
						break;
					}
					var16 += var26;
					var17 += var70;
				}
} (!var3)
			var var15, var16 = var14, var17 = var7;
			for (var15 = 0; var15 < var36; ++ var15)
			{
				var11[var17][var16][0] = var34[var67][var23][var15];
				var11[var17][var16][1] = var12;
				var11[var17][var16][2] = var42[var67][var23][var15];
				var16 += var26;
				var17 += var70;
			}
			if (var66)
			{
				var24[var12] = [var23, var10[var23][1]];
				var52++ ;
			}
			else
{
				var33[var12] = [var23, var10[var23][1]];
				var51++ ;
}
			var12++ ;
		}
	}
	return var11;
}

function function12(var7, var14, var19, var66){
	if (var66)
	{
		var13[var7][var14][0] = var19;
		document.images[function3(9) + var7 + function3(10) + var14] = function3(11) + var19 + function3(12);
	}
	else
{
		var4[var7][var14][0] = var19;
		document.images[function3(13) + var7 + function3(14) + var14] = function3(15) + var19 + function3(16);
}
}

function function15(var66){
	var var7, var14;
	for (var7 = 0; var7 < var32; ++ var7)
	{
		for (var14 = 0; var14 < var8; ++ var14)
		{
			if (var66)
				document.write(function3(17) + var7 + function3(18) + var14 + function3(19) + var7 + function3(20) + var14 + function3(21));
			else
				document.write(function3(22) + var7 + function3(23) + var14 + function3(24) + var4[var7][var14][0] + function3(25));
		}
		document.write(function3(26));
	}
}

function function26(var53){
	var var102 = false;
	for (var25 = 0; var25 < var24.length; ++ var25)
		if (var24[var25][1] > 0)
		{
			if (var102)
				var23 = var23 + function3(36);
			else
				var102 = true;
			var23 = var23 + var10[var24[var25][0]][0];
		}
	if (!var102)
		var23 = var23 + function3(37);
	var41 = var23;
	window.status = var41;
}

function4();
var4 = function8(false);
var13 = function8(true);
document.write(function3(38) + function3(39));
function15(true);
document.write(function3(40));
function15(false);
document.write(function3(41));
function26();