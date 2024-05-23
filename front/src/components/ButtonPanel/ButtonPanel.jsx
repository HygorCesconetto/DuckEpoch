import { useState } from "react"
import axios from 'axios';

const ButtonPanel = (props) =>{

    const addButton = (event) =>{
        event.preventDefault();
        axios.post(`http://localhost:5000/${props.Type}`, props.Data)
        .then(response => alert(response))
        .catch(error => console.log(error))
    }
    const updateButton = (event) =>{
        event.preventDefault();
        axios.patch(`http://localhost:5000/${props.Type}`, props.Data)
        .then(response => alert(response))
        .catch(error => console.log(error))
    }
    const deleteButton = (event) =>{
        event.preventDefault();
        axios.delete(`http://localhost:5000/${props.Type}/${props.Data["id"]}`)
        .then(response => alert(response))
        .catch(error => console.log(error))
    }


    return(
        <div className="ButtonPanel">
            <button onClick={addButton}>ADD</button>
            <button onClick={updateButton}>UPDATE</button>
            <button onClick={deleteButton}>DELETE</button>
        </div>
    )
}