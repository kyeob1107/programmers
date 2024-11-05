function solution(arr) {
    var answer = 0;
    let sum = 0
    arr.forEach(function(el){
        sum = sum + el
    })
    answer = sum / arr.length
    return answer;
}