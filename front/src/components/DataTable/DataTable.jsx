import { useEffect } from "react";
import { BdModelsList } from "../Models/BdModelsList";


const DataTable = (props) =>{
    useEffect(()=>{
    
    },[props.Data])


    if (!props.Load){
        return (
        <div className="DataTable">
            <table>
                <thead>
                    <tr>
                        {BdModelsList[props.Type].map((title,index)=>{
                            return <th key={index}>{title}</th>
                        })}
                    </tr>
                </thead>
                <tbody>
                    {props.Data.map((dict,index)=>(
                        <tr key={index}>
                            {BdModelsList[props.Type].map((data, index2)=>(
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
        return(<div></div>)
    }  

}

export default DataTable;