const Pool = require("pg").Pool;

const pool = new Pool({
  user: "postgres",
  password: "GPM54!90",
  port: 5432,
  host: "localhost",
  database: "project_data"
});

module.exports = pool;