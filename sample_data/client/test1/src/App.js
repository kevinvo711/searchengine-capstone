import React, { Fragment, useState } from "react";
//import { Linking } from 'react-native';
import "./App.css";

function App() {
  const [name, setName] = useState("");
  const [project_data, setUsers] = useState([]);

  const onSubmitForm = async e => {
    e.preventDefault();
    try {
      const response = await fetch(`http://localhost:5000/project_data/?name=${name}`);

      const parseResponse = await response.json();

      setUsers(parseResponse);
    } catch (err) {
      console.error(err.message);
    }
  };
  return (
    <Fragment>
      <div className="container text-center">
        <h1 className="my-5">Links</h1>
        <form className="d-flex" onSubmit={onSubmitForm}>
          <input
            type="text"
            name="name"
            placeholder="Search ..."
            className="form-control"
            value={name}
            onChange={e => setName(e.target.value)}
          />
          <button className="btn">Submit</button>
        </form>
        <table className="table my-5">
          <thead>
            <tr>
              <th>Title</th>
              <th>URL</th>
            </tr>
          </thead>
          <tbody>
            {project_data.map(project_data => (
              <tr key={project_data.id}>
                <td>{project_data.title}</td>
                <td>{project_data.url}</td>
                
              </tr>
            ))}
          </tbody>
        </table>
        {project_data.length === 0 && <p>No Results Found</p>}
      </div>
    </Fragment>
  );
}

export default App;