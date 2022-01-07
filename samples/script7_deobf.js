var var0 = ['IA==', 'IA==', 'IA==', 'JmhlbGxpcDs=', '', 'cA==', 'I21vcmU=', 'I2xlc3M=', 'dGV4dA==', 'dGV4dA==', 'I21vcmU=', 'I2xlc3M='];
function function1(var7){
	return decodeURIComponent(escape(window.atob(var0[var7])));
}

function function4(var17, var18){
	var19 = 39;
	while (var19 < 257)
		switch (var19){
			case (39):
				var19 = 75;
				break;
			case (75):
				var19 = 257;
				var var4 = var17.split(function1(0));
				break;
		}
	var4.splice(var18, var4.length - 1);
	return var4.join(function1(1)) + (var4.length !== var17.split(function1(2)).length ? function1(3) : function1(4));
}

var var11 = $(function1(5));
var var9 = $(function1(6));
var var20 = $(function1(7));
function function5(var21){
	var11.data(function1(8), var11.html());
	var11.html(function4(var11.html(), 50));
	var9.show();
	var22 = 42;
	while (var22 < 264)
		switch (var22){
			case (42):
				var22 = 152;
				break;
			case (152):
				var22 = 264;
				var20.hide();
				break;
		}
}

function5();
$(function1(10)).click(_0ib80k8462s);
var23 = 21;
while (var23 < 243)
	switch (var23){
		case (21):
			var23 = 94;
			break;
		case (94):
			var23 = 243;
			$(function1(11)).click(_0ib71k1155s);
			break;
	}
