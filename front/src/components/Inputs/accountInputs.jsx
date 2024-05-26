import { useState } from "react"

export default function AccountInputs(props){
    const[inputs,setInputs]=useState({})

    function inputChangeHandler(e){
        inputs[e.target.name]=e.target.value;
        setInputs(inputs);
        props.Datafunc(inputs);
    }

    if(props.InputType==='add'){
        return(
            <div id="add" className="account-input">
                <div className="input-c">
                    <label htmlFor="name">Nome</label>
                    <input id="name" name="name" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="email">Email</label>
                    <input id="email" name="email" type="text" onChange={inputChangeHandler}></input>
                </div>
                <div className="input-c">
                    <label htmlFor="pword">Senha</label>
                    <input id="pword" name="pword" type="password" onChange={inputChangeHandler}></input>
                </div>
            </div>
        )
    }
    else if(props.InputType==="update"){
        return(
            <div id="add" className="account-input">
                <div className="input-c">
                    <label htmlFor="id">ID</label>
                    <input id="id" name="id" type="number" onChange={inputChangeHandler}></input>
                </div>
                <div className="input-c">
                    <label htmlFor="name">Nome</label>
                    <input id="name" name="name" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="email">Email</label>
                    <input id="email" name="email" type="text" onChange={inputChangeHandler}></input>
                </div>
                <div className="input-c">
                    <label htmlFor="pword">Senha</label>
                    <input id="pword" name="pword" type="password" onChange={inputChangeHandler}></input>
                </div>
            </div>
        )
    }
    else if(props.InputType==="delete"){
        return(
            <div id="add" className="account-input">
                <div className="input-c">
                    <label htmlFor="id">ID</label>
                    <input id="id" name="id" type="number" onChange={inputChangeHandler}></input>
                </div>
            </div>
        )
    }
}