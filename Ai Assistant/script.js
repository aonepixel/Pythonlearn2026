async function sendMessage(){

let input=document.getElementById("message");

let text=input.value;


document.getElementById("chat").innerHTML +=
"<p><b>You:</b> "+text+"</p>";


let response = await fetch(
"http://localhost:5000/chat",
{
method:"POST",
headers:{
"Content-Type":"application/json"
},

body:JSON.stringify({
message:text
})

});


let data=await response.json();


document.getElementById("chat").innerHTML +=
"<p><b>Riya:</b> "+data.reply+"</p>";


input.value="";

}