import React from 'react';
import ReactDOM from 'react-dom/client';
import reportWebVitals from './reportWebVitals';
import './index.css';
import DataTable from './components/DataTable/DataTable';
import BasicInputForm from './components/Forms/BasicInputs';
import { BdModelsList } from './components/Models/BdModelsList';


const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <DataTable Type="itens"/>
    <BasicInputForm Type="itens" InputList={BdModelsList.itens}/>
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
