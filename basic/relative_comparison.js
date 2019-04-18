//상대비교 기법을 통해서 함수를 만듬

function is_equal1(a, b, allowed=0){
    var ep = Math.pow(2, -52); //앱실론에 2의 -52승
    var diff = Math.abs(a-b); //A-B , B-A 상관없음 절대값이니
    return diff<=Math.max(Math.abs(a),Math.abs(b))*ep * Math.pow(2, allowed); //2의 승수로 allowed하는 이유는 cpu 최적화 관점에서 1.7배 이렇게하면 사용자가 보기는 좋음
}

function main(){
    var sum=0;

    for(var i=0; i<100; i++){
        sum+=0.01;
    }


    if(is_equal1(sum, 1.0, 2)){ //네배부터 인식됨
        console.log("THE SAME");
    }else{
        console.log("not the same");
    }
}