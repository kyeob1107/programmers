function solution(arr, idx) {
    var answer = -1;
    for(let i=idx; i<arr.length; i++){
        if(arr[i]>0 && answer == -1){
            answer = i
        }
    }
    return answer;
}