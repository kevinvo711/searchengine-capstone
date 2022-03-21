const express = require("express");
const cors = require("cors");
const app = express();
const pool = require("./db");


app.use(cors());
app.get("/results", async (req, res) => {
  try {
    const { text } = req.query;

    const results = await pool.query(
      "SELECT id, title, url FROM results WHERE text -> 'TF-IDF' -> $1 is not null ORDER BY text -> 'TF-IDF' ->> $1 DESC;",
      [`${text}`]
    );


    res.json(results.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.listen(5000, () => {
  console.log("Server is starting on port 5000");
});