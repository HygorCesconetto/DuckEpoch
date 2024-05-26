import { useState } from "react"
import CUD from "../components/Buttons/CUD"
import DataTable from "../components/DataTable/DataTable"
import Navbar from "../components/Navbar/Navbar"
import CrudInputs from "../components/Inputs/CrudInputs"
import Confirm from "../components/Buttons/Confirm"

const BasePage = () =>{
    const[Route, setRoute] = useState("accounts")

    const RouteHandler =(route) =>{
        setRoute(route)
    }

    const[ConfirmButtons, setConfirmButtons]= useState(false)




    return(
       <div>
        <Navbar Router={RouteHandler}/>
        {Route !== "calculator" ? 
            <div>
                <DataTable Type={Route}/>
                <div className="CrudPanel">
                    <CrudInputs/>
                    {ConfirmButtons? <Confirm/>:<CUD Type={Route}/>}
                </div>
            </div> :
                 "calculator"}
       </div>

    )
}

export default BasePage