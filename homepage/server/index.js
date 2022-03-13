const express = require("express");
const cors = require("cors");
const app = express();
const pool = require("./db");


app.use(cors());
app.get("/results", async (req, res) => {
  try {
    const { text } = req.query;

    const results = await pool.query(
      "SELECT * FROM results WHERE title ILIKE $1",
      [`%${text}%`]
    );

    res.json(results.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.listen(5000, () => {
  console.log("Server is starting on port 5000");
});