function circleArea(number){
  let pi = Math.PI;    
  let num = Math.abs(number);
  return num * num * pi;
  }
  console.log(circleArea(10));
    
  
  function mintoMax(min,max){
    let random = Math.floor((Math.random() * (max-2)) + min);
    return random;
  }
  
  function ceilBy5(num){
      let number = Math.ceil( num / 5 ) * 5;
      return number;
  }
  
  function htmlHexCode(){
    let String = '#';
    for(let i=0; i < 6; i++) {
      a=Math.floor(Math.random()*16);
       b=a.toString(16);
    String += b;
  }
    return String;
  }
  htmlHexCode();
  
  
  function randomRgbCode(){
    let String = 'rgb(';
    for(let i=0; i < 3; i++) {
    a=Math.floor(Math.random()*255);
    String += a;
    if(i!=2){
    String += ', ';
         }
  }
    return String += ')';
  }
  randomRgbCode();
  
  
  function fixFloat(a, b){
    let numObj = a;
    let i =	b;
    return numObj.toFixed(i);  
  }
  fixFloat(10.12345, 2);
  fixFloat(15.5678, 1);
  
  
  function camelToSnake(str) {
    let strobj = '';
  
    for (let i = 0; i < str.length; i++) {
      if (str[i] === str[i].toUpperCase()) {
        strobj += '_';
        strobj += str[i].toLowerCase();
      } else {
        strobj += str[i];
      }
    }
    return strobj;
  }
  
  console.log(camelToSnake('helloWorld'));
  
  function snakeToCamel(str) {
    let strobj = '';
  
    for (let i = 0; i < str.length; i++) {
      if (str[i] === '_') {
        strobj += str[i + 1].toUpperCase();
        // str[i+1] = '';
        i += 1;
      } else {
        strobj += str[i];
      }
    }
    return strobj;
  }
  
  console.log(snakeToCamel('hello_world_javascript'));
  
  
  
  
  function getDay(a, b) {
    const dayday = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT'];
    const date = new Date(2016, a - 1, b);
    const day = date.getDay();
    return dayday[day];
  }
  
  console.log(getDay(5, 24));
  
  
  
  
  
  
  
  
  function hidePhoneNumber(string) {
    const str = string;
    let strobj = '';
    if (str.length > 3 && str.length < 20) {
      for (let i = 0; i < str.length - 4; i++) {
        strobj += str[i].replace(str[i], '*');
      }
    }
    const res = str.substring(str.length - 4);
    return strobj + res;
  }
  console.log(hidePhoneNumber('01033334444'));
  console.log(hidePhoneNumber('027778888'));
  