var var0 = ['MDA=', 'MjA=', 'NDA=', 'NjA=', 'ODA=', 'YTA=', 'YzA=', 'ZmY=', 'PHRhYmxlIGJvcmRlcj0xIGNlbGxwYWRkaW5nPTg+', 'PHRyPg==', 'PHRkIGJnY29sb3I9IiM=', 'Ij4=', 'PHR0Pjxmb250IGNvbG9yPSIj', 'Ij4g', 'IDwvZm9udD48L3R0PjwvdGQ+', 'PC90cj4=', 'PC90YWJsZT48YnI+'];
function function0(var1){
	return decodeURIComponent(escape(window.atob(var0[var1])));
}

var2 = 89;
while (var2 < 371)
	switch (var2){
		case (89):
			var2 = 195;
			break;
		case (195):
			var2 = 371;
			var3 = new Array(function0(0), function0(1), function0(2), function0(3), function0(4), function0(5), function0(6), function0(7));
			break;
	}
for (var4 = 0; var4 < 8; var4++ )
{
	document.write(function0(8));
	for (var5 = 0; var5 < 8; var5++ )
	{
		document.write(function0(9));
		for (var6 = 0; var6 < 8; var6++ )
		{
			document.write(function0(10) + var3[var4] + var3[var5] + var3[var6] + function0(11));
			document.write(function0(12) + var3[7 - var4] + var3[7 - var5] + var3[7 - var6] + function0(13));
			document.write(var3[var4] + var3[var5] + var3[var6] + function0(14));
		}
		document.write(function0(15));
	}
	document.write(function0(16));
}