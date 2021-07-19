
function sendReq(e){
  let xhr = new XMLHttpRequest();
  xhr.open("POST", '/' + e.value);
  xhr.send();
  console.log(e.value);

}
