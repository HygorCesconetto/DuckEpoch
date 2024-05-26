import { useState } from "react"
import ButtonPanel from "../ButtonPanel/ButtonPanel";


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
            <div className="form-container">
            {/* fazer blocos de input com BDModelsDict */}
            </div>
            <ButtonPanel Type ={props.Type} Data={InputData}/>
        </div>
    )
}

export default BasicInputForm