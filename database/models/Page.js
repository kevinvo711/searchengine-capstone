const Sequelize = require('sequelize');
const db = require('../db');

const Page = db.define("page", {

  number: {
    type: Sequelize.STRING,
    allowNull: false
  }

});

module.exports = Page;