const Pool = require("pg").Pool;

const pool = new Pool({
  user: "postgres",
  password: "password",
  port: 5432,
  host: "127.0.0.1",
  database: "starter-server"
});

module.exports = pool;