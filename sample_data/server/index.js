const express = require("express");
const cors = require("cors");
const app = express();
const pool = require("./db");


app.use(cors());
app.get("/users", async (req, res) => {
  try {
    const { name } = req.query;

    const users = await pool.query(
      "SELECT * FROM users WHERE first_name || ' ' || last_name ILIKE $1",
      [`%${name}%`]
    );

    res.json(users.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.listen(5000, () => {
  console.log("Server is starting on port 5000");
});