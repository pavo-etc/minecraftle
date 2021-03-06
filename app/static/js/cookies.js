
var user_id;

/**
 * Checks if user_id exists already, creates one if not
 */
function checkUserCookie() {
    user_id = localStorage.getItem("user_id");
    if (user_id !== null) {
        console.log("Welcome back! Your user_id is: " + user_id);
    } else {
        createUserID();
    }
}

/**
 * Generates a random UUID and stores it in webstorage
 */
function createUserID() {
    let uuid = Date.now().toString() + Math.random().toString();//self.crypto.randomUUID();// crypto only works with SSL
    localStorage["user_id"] = uuid;
    console.log("Generated new user_id: "+ localStorage["user_id"] );
    user_id = localStorage["user_id"];
}

/**
 * On document load, looks to call checkUserCookie() function to check to see if
 * user_id exists
 */
 document.addEventListener("DOMContentLoaded", ()=>{
    checkUserCookie();
    let statsbutton = document.getElementById("statsbutton");
    statsbutton.onclick = ()=>{
        location.href = "/stats/"+user_id;
    };
});
