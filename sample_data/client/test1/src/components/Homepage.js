import React, { Fragment, useState } from "react";
import { BrowserRouter as Router, Routes, Route, Link } from "react-router-dom";
import Linkify from 'react-linkify';
import './Homepage.css';

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
        <h1 className="my-5">Search</h1>
        <form className="d-flex" onSubmit={onSubmitForm}>
          <input
            type="text"
            name="name"
            placeholder="Search ..."
            className="form-control"
            value={name}
            onChange={e => setName(e.target.value)}
          />
          
          <button className="btn">Search</button>


          {/*<Router>
          <button><Link to="/Results">Submit</Link></button>
          <Routes>
            <Route path="/Results" element={<Results />} />
          </Routes>
          </Router>*/}
          
        </form>
          <body>
            {project_data.map(project_data => (
              <tr key={project_data.id}>
                <h4>{project_data.title}</h4>
                <Linkify>
                  <p>{project_data.url}</p>
                </Linkify>
                <p>more info about link. Maybe first sentence?</p>
                
                
              </tr>
            ))}
          </body>
        {project_data.length === 0 && <p>No Results Found</p>}
      </div>
    </Fragment>
  );
}

export default App;