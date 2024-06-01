import { useState } from "react";

export default function BuildsInputs(props){
    const[inputs,setInputs]=useState({})

    function inputChangeHandler(e){
        inputs[e.target.name]=e.target.value;
        setInputs(inputs);
        props.Datafunc(inputs);
    }
    
    if(props.InputType==='update'){
        return(
            <div className="inputlist">
                <div className="input-c">
                    <label htmlFor="id">ID</label>
                    <input id="id" name="id" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="id_account">ID_Account</label>
                    <input id="id_account" name="id_account" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="name">Nome</label>
                    <input id="name" name="name" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="helmet">Hemlet</label>
                    <input id="helmet" name="helmet" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="body">Armour</label>
                    <input id="body" name="body" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="gloves">Gloves</label>
                    <input id="gloves" name="gloves" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="boots">Boots</label>
                    <input id="boots" name="boots" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="main_hand">MainHand</label>
                    <input id="main_hand" name="main_hand" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="off_hand">OffHand</label>
                    <input id="off_hand" name="off_hand" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="amulet">Amulet</label>
                    <input id="amulet" name="amulet" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="ring">Ring</label>
                    <input id="ring" name="ring" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="belt">Belt</label>
                    <input id="belt" name="belt" type="number" onChange={inputChangeHandler} ></input>
                </div>
            </div>
        )
    }
    else if(props.InputType==="add"){
        return(
            <div className="inputlist">
                <div className="input-c">
                    <label htmlFor="id_account">ID_Account</label>
                    <input id="id_account" name="id_account" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="name">Nome</label>
                    <input id="name" name="name" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="helmet">Hemlet</label>
                    <input id="helmet" name="helmet" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="body">Armour</label>
                    <input id="body" name="body" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="gloves">Gloves</label>
                    <input id="gloves" name="gloves" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="boots">Boots</label>
                    <input id="boots" name="boots" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="main_hand">MainHand</label>
                    <input id="main_hand" name="main_hand" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="off_hand">OffHand</label>
                    <input id="off_hand" name="off_hand" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="amulet">Amulet</label>
                    <input id="amulet" name="amulet" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="ring">Ring</label>
                    <input id="ring" name="ring" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="belt">Belt</label>
                    <input id="belt" name="belt" type="number" onChange={inputChangeHandler} ></input>
                </div>
            </div>
        )
    }
    else if(props.InputType==="delete"){
        return(
        <div className="input-c">
            <label htmlFor="id">ID</label>
            <input id="id" name="id" type="number" onChange={inputChangeHandler} ></input>
        </div>
        )
    }


}