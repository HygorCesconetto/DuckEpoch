import React from 'react';
import './DataTable.css';
import axios from 'axios';
import { BdModels } from '../Models/BdModels';

const API_URL = "http://localhost:5000/"


class DataTable extends React.Component{
  constructor(props){
    super(props);
    this.state = {Data: []};
  }
  

  render(){
    return (
      <div className='DataTable'>
      </div>
    )
  }

}
export default DataTable;
