
// register models, set up associations between tables, and generate barrel file for the models;

const Result  = require('./Result');
const Page  = require('./Page');

Result.belongsTo(Page);
Page.hasMany(Result);

module.exports = {
  Result,
  Page
};