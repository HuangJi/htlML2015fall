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

function getEin(theta, testDataList, s, column) {
	var error = 0;
	var dataList = [];
	for (var k = 0; k < testDataList.length; k++) {
		dataList.push(testDataList[k][column]);
	}
	for (var l = 0; l < dataList.length; l++) { //dataList.length == 100
		if(jSign(dataList[l] - theta ) * s != testDataList[l][10]) {
			error += 1;
		}
	}
	var errorRate = error / dataList.length;
	return errorRate;
}

function verifyTestData(testDataList, bestDecisionStump) {
	var bestDimension = -99;
	var errorRate = 0;
	var minimumErrorRate = 1000;
	var bestTheta = 0;
	var theta = bestDecisionStump;

	for (var column = 1; column < testDataList[0].length - 1; column++) {
		for (var raw = 0; raw < testDataList.length; raw++) {
			errorRatePositive = getEin(theta, testDataList, 1, column);
			errorRateNegative = getEin(theta, testDataList, -1, column);
			if (errorRatePositive < minimumErrorRate) {
				minimumErrorRate = errorRatePositive;
				bestTheta = theta;
				bestDimension = column;
			}
			if (errorRateNegative < minimumErrorRate) {
				minimumErrorRate = errorRateNegative;
				bestTheta = theta;
				bestDimension = column;
			}
		}
	}
	return {
		minimumErrorRate: minimumErrorRate,
		bestTheta: bestTheta,
		bestDimension: bestDimension
	}
}

var testDataList = [];
var bestDecisionStump = 1.461;

tsv({
    input: "./hw2_test.dat.txt",
    output: "output.json",
    parseRows: true
}, function(err, result) {
	var splitList = [];
	for (var i = 0; i < result.length; i++) {
		splitList = result[i][0].split(' ');
		testDataList.push(splitList);
	}
	var minimumAverageErrorRate = 0;
	var sum = 0;
	var answer = verifyTestData(testDataList, bestDecisionStump);
	console.log('minimumErrorRate is: ' + answer.minimumErrorRate);
});
