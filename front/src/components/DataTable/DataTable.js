import React, { useState } from 'react';
import './DataTable.css';
import axios from 'axios';



const API_URL = "http://localhost:5000/"


const DataTable = (props) => {
  const[Response, setResponse]= useState({})



  const DataFetch = () =>(
    axios.get(`${API_URL}${props.Type}`).then(res=>{
      setResponse(res.data)
      console.log(Response)
    })
  );

  return(<div className="DataTable">
    <button onClick={DataFetch}>DATA</button>
  </div>
  );
};


export default DataTable;
