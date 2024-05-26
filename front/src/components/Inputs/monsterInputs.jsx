import { useState } from "react";

export default function MonsterImputs(props){
    const[inputs,setInputs]=useState({})

    function inputChangeHandler(e){
        inputs[e.target.name]=e.target.value;
        setInputs(inputs);
        props.Datafunc(inputs);
    }
    
    if(props.InputType==='update'){
        return(
            <div className="monster-input">
                <div className="input-c">
                    <label htmlFor="id">ID</label>
                    <input id="id" name="id" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="type">Type</label>
                    <input id="type" name="type" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="name">Nome</label>
                    <input id="name" name="name" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="atk">ATK</label>
                    <input id="atk" name="atk" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="atks">ATKs</label>
                    <input id="atks" name="atks" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="def">DEF</label>
                    <input id="def" name="def" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="hp">HP</label>
                    <input id="hp" name="hp" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="crit_chance">CC</label>
                    <input id="crit_chance" name="crit_chance" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="crit_mult">CM</label>
                    <input id="crit_mult" name="crit_mult" type="number" onChange={inputChangeHandler} ></input>
                </div>
            </div>
        )
    }
    else if(props.InputType==="add"){
        return(
            <div className="monster-input">
                <div className="input-c">
                    <label htmlFor="type">Type</label>
                    <input id="type" name="type" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="name">Nome</label>
                    <input id="name" name="name" type="text" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="atk">ATK</label>
                    <input id="atk" name="atk" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="atks">ATKs</label>
                    <input id="atks" name="atks" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="def">DEF</label>
                    <input id="def" name="def" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="hp">HP</label>
                    <input id="hp" name="hp" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="crit_chance">CC</label>
                    <input id="crit_chance" name="crit_chance" type="number" onChange={inputChangeHandler} ></input>
                </div>
                <div className="input-c">
                    <label htmlFor="crit_mult">CM</label>
                    <input id="crit_mult" name="crit_mult" type="number" onChange={inputChangeHandler} ></input>
                </div>
            </div>
        )
    }
    else if(props.InputType==="delete"){
        return(
            <div className="monster-input">
                <label htmlFor="id">ID</label>
                <input id="id" name="id" type="number" onChange={inputChangeHandler}></input>
            </div>
        )
    }


}