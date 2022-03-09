const pgtools = require('pgtools');
const {dbName, dbUser, dbPwd} = require('./configDB');


const config = {
    user: dbUser,
    host: 'localhost',
    port: 5432,
    password: dbPwd
  };
    
  //attempt to create DB
  //if it already exists, this does nothing and just connects to
  //the existing db of that name

  pgtools.createdb(config, dbName, function(err, res) {
    if (err) {
      console.error(err);
      process.exit(-1);
    }
    console.log(res);
  });