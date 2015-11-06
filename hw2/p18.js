var fs = require('fs');
var tsv = require('node-tsv-json');
var noise = 0.04611234;
function generate20DataSetArray() {
	var pointArray = [];

	for (var i = 0; i < 20; i++) {
		var point = new Object();
		x = Math.random();
		y = Math.random() + 1;
		point.x = x - y + 1;
		point.y = jSign(point.x) * percent20Flipper();
		// point.y = jSign(point.x);
		pointArray.push(point);
	};
	pointArray.sort(function(a, b) {
		return parseFloat(a.x) - parseFloat(b.x); 
	});
	return pointArray;
}

function percent20Flipper() {
	if (Math.random() < 0.2) {
		return -1;
	}
	else {
		return 1;
	}
}

function jSign(x) {
	if (x > 0) {
		return 1;
	}
	else {
		return -1;
	}
}

function getEout(theta, s) {
	return 0.5 + 0.3 * s * (Math.abs(theta) - 1);
}

function getMinimumAverageErrorRate() {
	var dataArray = generate20DataSetArray();
	var theta = 0;
	var minimumErrorRate = 100;
	for (var i = 0; i < dataArray.length; i++) {
		theta = dataArray[i].x;
		errorRatePositive = getEout(theta, 1);
		errorRateNegative = getEout(theta, -1);
		if (errorRatePositive < minimumErrorRate) {
			minimumErrorRate = errorRatePositive;
		}
		if (errorRateNegative < minimumErrorRate) {
			minimumErrorRate = errorRateNegative;
		}
	}
	return minimumErrorRate;
}

var sum = 0;
var errorAvAverageErrorRate = 0;
for (var i = 0; i < 5000; i++) {
	errorAvAverageErrorRate = noise + getMinimumAverageErrorRate();
	sum += errorAvAverageErrorRate;
	console.log(errorAvAverageErrorRate);
}; 
var averageErrorRate = sum / 5000;

console.log('Eout is: ' + averageErrorRate);