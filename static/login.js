import replit
db = replit.database
const keys = db.keys();

for (let i = 0; i < keys.length; i++) {
  const key = keys[i];
  const value = db[key];
  // Do something with the key and value
  document.getElementById('username').innerHTML = key
}
