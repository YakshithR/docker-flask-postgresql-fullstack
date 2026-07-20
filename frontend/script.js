const BACKEND_URL = "http://13.51.249.6:5000"

async function loadBackendInfo(){

    const response = await fetch(`${BACKEND_URL}/`);

    const data = await response.json();

    document.getElementById("message").innerText = data.message;

    document.getElementById("podName").innerText = data.pod_name;

    document.getElementById("podIp").innerText = data.pod_ip;

}

async function loadUsers(){

    const response = await fetch(`${BACKEND_URL}/users`);

    const users = await response.json();

    let html = "";

    users.forEach(user=>{

        html += `<li>${user.id}. ${user.name}</li>`;

    });

    document.getElementById("users").innerHTML = html;

}

async function saveUser(){

    const name=document.getElementById("username").value;

    if(name===""){

        alert("Enter your name");

        return;

    }

    await fetch(`${BACKEND_URL}/users`,{

        method:"POST",

        headers:{

            "Content-Type":"application/json"

        },

        body:JSON.stringify({

            name:name

        })

    });

    document.getElementById("username").value="";

    loadUsers();

}

loadBackendInfo();

loadUsers();
