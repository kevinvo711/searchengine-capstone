const express = require("express");
const cors = require("cors");
const app = express();
const pool = require("./db");
const request = require('request');

app.use(cors());
app.get("/results", async (req, res) => {
  try {
    const { text } = req.query;
    const results = await pool.query(
      "SELECT id, title, url, text FROM results"
    );
    // const results = await pool.query(
    //   "SELECT id, title, url FROM results WHERE text -> 'TF-IDF' -> $1 is not null ORDER BY text -> 'TF-IDF' ->> $1 DESC;",
    //   [`${text}`]
    // );
    res.json(results.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.post("/test", async (req, res) => {
  res.send([req.query]);
});

app.get("/test", async (req, res) => {
  fetch('http://127.0.0.1:8000/test', async (error, response, body) => {
  console.error('error:', error); // Print the error
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the data received
  res.send([req.query]); //Display the response on the website
})
});

app.get('/py', async (req, res) => {
  request('http://127.0.0.1:8000/flask', async (error, response, body) => {
  console.error('error:', error); // Print the error
  console.log('statusCode:', response && response.statusCode); // Print the response status code if a response was received
  console.log('body:', body); // Print the data received
  res.send(body); //Display the response on the website
});  
});

app.listen(5000, () => {
  console.log("Server is starting");
});