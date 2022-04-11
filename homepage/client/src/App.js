import React, { Fragment, useState, Component } from "react";
import "./App.css";

function App() {
  const [query, setQuery] = useState("");
  const [results, setResults] = useState([]);

  const onSubmitForm = async e => {
    e.preventDefault();
    try {
      if (query !== ""){
      const response = await fetch(`http://localhost:5000/results/?text=${query}`);
      // const response = await fetch(`http://localhost:5000/test/?text=${query}`);


      const parseResponse = await response.json();

      setResults(parseResponse);}
    } catch (err) {
      console.error(err.message);
    }
  };
  
  return (
    <Fragment>
      <div className="container text-center">
        <h1 className="my-5">Search Engine</h1>
        <form className="d-flex" onSubmit={onSubmitForm} >
        {/* method="post" action="/test" for after demo*/ }
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
          <thead>
            <tr>
              <th>Title</th>
              <th>URL</th>
            </tr>
          </thead>
          <tbody>
            {results.map(result => (
              <tr key={result.id}>
                <td>{result.title}</td>
                <td><a target ="_blank" href={result.url}>{result.url}</a></td>
              </tr>
            ))}
          </tbody>
        </table>
        {results.length === 0 && <p>No Results Found</p>}
      </div>
    </Fragment>
  );
}

export default App;