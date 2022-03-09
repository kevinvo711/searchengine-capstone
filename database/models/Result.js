const Sequelize = require('sequelize');
const db = require('../db');

const Result = db.define("result", {

  id: {
    type: Sequelize.INTEGER,
    allowNull: false,
    primaryKey: true
  },

  title: {
    type: Sequelize.STRING,
    allowNull: false
  },

  url: {
    type: Sequelize.STRING,
    allowNull: false
  }

});

module.exports = Result;