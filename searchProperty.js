let arr = []
function searchProperty(obj, count, res) {
	if (count > 8){
		return 0
	}
	count++;
	
	if(obj instanceof Array) {
		let len = Math.min(obj.length, 5)
		for(let i=0; i<len; i++){
			if(obj[i] == res){
				return 1
			}
			if (searchProperty(obj[i], count, res)){
				arr.unshift(i)
				return 1
			}
		}
	}else if(obj instanceof Object){
		for(let k in obj){
			if(k == res){
				return 1
			}
			if (searchProperty(obj[k], count, res)){
				arr.unshift(k);
				return 1
			}
		}
	}else{
		return 0
	}
}