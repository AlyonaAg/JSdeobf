var var0 = ['0J7RgdC90L7QstCw0L3QuNC1IA==', '0KLQtdGB0YIg0KTQtdGA0LzQsDog0YfQuNGB0LvQviA=', 'INGB0L7RgdGC0LDQstC90L7QtQ==', '0KLQtdGB0YIg0KTQtdGA0LzQsDog0YfQuNGB0LvQviA=', 'INCy0LXRgNC+0Y/RgtC90L4g0L/RgNC+0YHRgtC+0LU=', '0J3QntCUOiA=', 'CtCa0L7RjdGE0YTQuNGG0LjQtdC90YIg0L/RgNC4INGH0LjRgdC70LUg', 'OiA=', 'CtCa0L7RjdGE0YTQuNGG0LjQtdC90YIg0L/RgNC4INGH0LjRgdC70LUg', 'OiA=', 'MSkg0J3QsNC50YLQuCDQndCe0JQg0LTQstGD0YUg0YfQuNGB0LXQuwoyKSDQn9GA0L7QstC10YDQuNGC0Ywg0L/RgNC+0YHRgtC+0YLRgyDRh9C40YHQu9CwCg==', '0JLQstC10LTQuNGC0LUg0YfQuNGB0LvQvg==', '0JLQstC10LTQuNGC0LUg0L/QtdGA0LLQvtC1INGH0LjRgdC70L4=', '0JLQstC10LTQuNGC0LUg0LLRgtC+0YDQvtC1INGH0LjRgdC70L4='];
function function0(var1){
	return decodeURIComponent(escape(window.atob(var0[var1])));
}

function function4(var36, var37, var38){
	if (var37 == 1)
		return var36;
	if (var37 % 2 == 0)
		return function4(var36, var37 / 2, var38) ** 2 % var38;
	return function4(var36, var37 - 1, var38) * var36 % var38;
}

function function7(var6){
	var var18 = new Array();
	var var45;
	for (var7 = 0; var7 <= 7; var7++ )
		var18[var7] = Math.floor(Math.random() * (var6 - 4) + 2);
	for (var7 = 0; var7 <= 7; var7++ )
	{
		var45 = function4(var18[var7], var6 - 1, var6);
		if (var45 != 1)
		{
			console.log(function0(0) + var18[var7]);
			console.log(function0(1) + var6 + function0(2));
			return;
		}
	}
	console.log(function0(3) + var6 + function0(4));
}

function function10(var9, var8){
	var var28, var14, var15, var21, var23, var16, var17, var7;
	if (var8 > var9)
	{
		var28 = var8;
		var8 = var9;
		var9 = var28;
	}
	var9, var8 = var8, var9;
	var14 = var9, var15 = var8, var21 = 1, var23 = 0, var16 = 0, var17 = 1, var7 = 1;
	var32 = 1, var33 = 0, var34 = 0;
	while (var8)
	{
		var22 = Math.floor(var14 / var15);
		var30 = var14 - var22 * var15;
		if (!var30)
		{
			var32 = var15, var33 = var23, var34 = var17;
			break;
		}
		var20 = var21 - var22 * var23;
		var35 = var16 - var22 * var17;
		var21 = var23;
		var23 = var20;
		var16 = var17;
		var17 = var35;
		var14 = var15;
		var15 = var30;
		var7++ ;
	}
	console.log(function0(5) + var32 + function0(6) + var9 + function0(7) + var33 + function0(8) + var8 + function0(9) + var34);
}

var25 = prompt(function0(10));
if (var25 == 2)
{
	var6 = prompt(function0(11));
	function7(var6);
}
else
	if (var25 == 1)
	{
		var var9 = prompt(function0(12));
		var var8 = prompt(function0(13));
		function10(var9, var8);
	}