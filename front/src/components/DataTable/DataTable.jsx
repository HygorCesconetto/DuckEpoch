import { useEffect, useState } from "react";
import { BdModels } from "../Models/BdModels";





const DataTable = (props) =>{
    const[Data, setData] = useState([]);
    const[IsLoading, setIsLoading] = useState(true);

    const fetchApi = () =>{
        fetch(`http://localhost:5000/${props.Type}`)
            .then(response => response.json())
            .then(data => setData(data))
            .catch(error => console.log(error))
            .finally(()=>setIsLoading(false))
    }
    
    useEffect(()=>{
        fetchApi();
    },[])





    if (!IsLoading){
        return (
        <div className="DataTable">
            <table>
                <thead>
                    <tr>
                        {BdModels[props.Type].map((title,index)=>{
                            return <th key={index}>{title}</th>
                        })}
                    </tr>
                </thead>
                <tbody>
                    {Data.map((dict,index)=>(
                        <tr key={index}>
                            {BdModels[props.Type].map((data, index2)=>(
                                <td key={index2}>{dict[data]}</td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
        )
    }
    else {
        return(<div>Loading...</div>)
    }  

}

export default DataTable;