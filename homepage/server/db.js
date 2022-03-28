const Pool = require("pg").Pool;

const pool = new Pool({
  // user: "postgres",
  // password: "GPM54!90",
  // port: 5432,
  // host: "localhost",
  // database: "test1"
  user: "postgres",
  password: "password",
  port: 5432,
  host: "localhost",
  database: "starter-server"
});

module.exports = pool;