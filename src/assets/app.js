/* global echarts */

var app

app = (function(){
	var charts = echarts.init(document.getElementById('main')),
		loop = function(){}

	function run(callback){
		callback = callback || loop
		var xhr = new XMLHttpRequest()
		xhr.open('GET','data.json')
		xhr.addEventListener('load', function(){
			var opt = callback(JSON.parse(this.responseText))
			if(opt){
				setOptions(opt)
			}
		})
		xhr.send()
	}

	function setOptions(option){
		charts.setOption(option);
	}

	function fillArr(len,callback){
		return Array.from(new Array(len)).map(callback || loop)
	}
	return {
		run:run,
		utils:{
			fillArr:fillArr
		}
	}
})()