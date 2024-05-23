import { useState } from "react"

const BasicInputForm = (props)=>{
    const[InputData, setInputData]= useState({})

    const inputChangeHandler = (event) =>{
        if (event !== undefined){
            InputData[event.target.name] = event.target.value;
            setInputData(InputData)
        }
    }





    return(
        <div className="BasicInputForm">
            {props.InputList.map((input,index)=>(
                <div key={index} className="input-container">
                    <label htmlFor={input}>{input}</label>
                    <input type="text" id={input} name={input} onChange={inputChangeHandler}/>
                </div>
            ))}
        </div>
    )
}