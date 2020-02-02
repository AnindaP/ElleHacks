const user = [
    {
        username: "sinrostro",
        password: "luisa"
    },
    {
        username: "rosesolano",
        password: "alverrr"
    }
]

function getLogin() {
	var username = document.getElementById('user').value
	var password = document.getElementById('pass').value

	for(var i = 0; i < user.length; i++) {
		if(username == user[i].username && password == user[i].password) {
            window.location.href="accounts.html";
            return false;
		}
	}
	console.log("incorrect username or password")
}