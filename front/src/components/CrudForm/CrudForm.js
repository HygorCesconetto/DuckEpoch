import React from 'react';
import './CrudForm.css';
import CrudButtons from './CrudButtons/CrudButtons';

export default function CrudForm(props){

  const data = {
    id:6,
    name:"aaaaaaa",
    email:"a@lek.com",
    pword:"pword"
  };


  return(
    <div className="CrudForm">
      <div className='Form'>

      </div>
      <CrudButtons Type={props.Type} Data={data}/>
    </div>
  );
};
