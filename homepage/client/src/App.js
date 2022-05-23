import React, { Fragment, useState, Component } from "react";
import List from "./List"
import "./App.css";


function App() {
  const [query, setQuery] = useState("");

  return (
    <Fragment>
      <div className="container text-center">
        <h1 className="my-5">Search</h1>
        <form className="d-flex" method="post" action="/test" >
          <input
            type="text"
            name="text"
            placeholder="Search for.."
            className="form-control"
            value={query}
            onChange={e => setQuery(e.target.value)}
          />
          <button className="btn btn-success">Submit</button>
        </form>

        <table className="table my-5">
          <List />
        </table>
      </div>
    </Fragment>
  );
}

export default App;