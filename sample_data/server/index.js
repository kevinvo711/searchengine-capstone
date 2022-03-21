const express = require("express");
const cors = require("cors");
const app = express();
const pool = require("./db");


app.use(cors());
app.get("/project_data", async (req, res) => {
  try {
    const { name } = req.query;

    const project_data = await pool.query(
      "SELECT * FROM project_data WHERE title ILIKE $1",
      [`%${name}%`]
    );

    res.json(project_data.rows);
  } catch (err) {
    console.error(err.message);
  }
});

app.listen(5000, () => {
  console.log("Server is starting on port 5000");
});