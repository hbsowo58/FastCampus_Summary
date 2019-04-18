//절대비교 기법을 통해서 함수를 만듬

function is_equal(a, b){
    return Math.abs(a-b)<= 1e-10;
}

function main(){
    var a = 0.3;
    var b = 0.1 * 3;


    // if(a==n)
    if(is_equal(a, b)){
        console.log("THE SAME");
    }else{
        console.log("not the same");
    }
}