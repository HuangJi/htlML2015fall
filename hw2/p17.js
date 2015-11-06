var fs = require('fs');
var tsv = require('node-tsv-json');

function generate20DataSetArray() {
	var pointArray = [];

	for (var i = 0; i < 20; i++) {
		var point = new Object();
		x = Math.random();
		y = Math.random() + 1;
		point.x = x - y + 1;
		point.y = jSign(point.x) * percent20Flipper();
		pointArray.push(point);
	};
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

function getEin(theta, dataList, s) {
	var error = 0;
	for (var i = 0; i < dataList.length; i++) {
		if(jSign(dataList[i].x - theta ) * s != dataList[i].y) {
			error += 1;
		}
	}
	var errorRate = error / dataList.length;
	return errorRate;
}

function getMinimumAverageErrorRate() {
	var dataArray = generate20DataSetArray();
	var theta = 0;
	var errorRate = 0;
	var minimumErrorRate = 10;
	for (var i = 0; i < dataArray.length; i++) {
		theta = dataArray[i].x;
		errorRatePositive = getEin(theta, dataArray, 1);
		errorRateNegative = getEin(theta, dataArray, -1);
		if (errorRatePositive < minimumErrorRate) {
			minimumErrorRate = errorRatePositive;
		}
		else if (errorRateNegative < minimumErrorRate) {
			minimumErrorRate = errorRateNegative;
		}
	}
	return minimumErrorRate;
}

var sum = 0;
var errorAvAverageErrorRate = 0;
for (var i = 0; i < 5000; i++) {
	errorAvAverageErrorRate = getMinimumAverageErrorRate();
	sum += errorAvAverageErrorRate;
}; 

var averageErrorRate = sum / 5000;

console.log('Ein is: ' + averageErrorRate);