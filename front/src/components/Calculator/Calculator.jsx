import { useState } from "react"
import './style.css';

const Calculator = () =>{
    const[Data,setData]=useState({})
    const[isLoading,setIsLoading]=useState(true)

    function submit(){
        const id_b = document.getElementById("build").value
        const id_m = document.getElementById("monster").value
        fetch(`http://localhost:5000/dps/${id_b}/${id_m}`)
            .then(resp=>{
                console.log(resp);
                if(resp.ok){
                    return(resp.json()).then(data=>{setData(data);setIsLoading(false)})
                }
                else{setIsLoading(true);setData({});alert("Erro: id's inválidos.");}
            })
        document.getElementById("build").value = ""
        document.getElementById("monster").value = ""
    }
    
    return(
        <div className="calculator">
            <div className="calc-form">
                <div className="input">
                    <label htmlFor="build">Build</label>
                    <input id="build" name="build" type="number"></input>
                </div>
                <div className="input">    
                    <label htmlFor="monster">Monster</label>
                    <input id="monster" name="monster" type="number"></input>
                </div> 
                <button onClick={submit}>Calcular</button>
            </div>
            <div className="result">
                {isLoading?"":<div><p>DPS: {Data["raw_dps"]}</p>
                <p>Mitgated DPS: {Data["dps_on_monster"]}</p>
                <p>Time to kill: {Data["time_to_kill"]}s</p></div>}
            </div>
        </div>
    )
}

export default Calculator