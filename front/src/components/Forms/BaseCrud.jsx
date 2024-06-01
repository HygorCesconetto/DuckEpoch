import { useEffect, useState } from "react";
import AccountInputs from "../Inputs/accountInputs";
import ItemInputs from "../Inputs/itensInputs";
import BuildsInputs from "../Inputs/buildsInputs";
import MonsterImputs from "../Inputs/monsterInputs";
import './style.css';

const BaseCrud = (props) => {
  const [DataCRUD, setDataCRUD] = useState({});
  const [inputType, setinputType] = useState("");
  const [ConfirmButtons, setConfirmButtons] = useState(false);

  useEffect(() => {
    setDataCRUD({});
    setinputType("");
    setConfirmButtons(false);
  }, [props.Type]);

  const DataUpdateHandler = (data) => {
    setDataCRUD(data);
  };

  function inputRenderHandler(type){
    setinputType(type);
    setConfirmButtons(true);

  }


  function confirmHandler() {
    const baseurl = "http://localhost:5000/";
    const add_options = {
      method: "POST",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(DataCRUD),
    };
    const update_options = {
      method: "PATCH",
      headers: {
        Accept: "application/json",
        "Content-Type": "application/json",
      },
      body: JSON.stringify(DataCRUD),
    };
    const delete_options = { method: "DELETE" };

    if (inputType === "add")          {fetch(`${baseurl}${props.Type}`, add_options)
    .finally(()=>{window.location.reload();})}
    
    else if (inputType === "update")  {fetch(`${baseurl}${props.Type}`, update_options)
    .finally(()=>{window.location.reload();})}
    
    else if (inputType === "delete")  {fetch(`${baseurl}${props.Type}/${DataCRUD["id"]}`, delete_options)
    .finally(()=>{window.location.reload();})}
  }

  function discardHandler(){
    setDataCRUD({})
    document.getElementById("form").reset();
    setinputType("")
    setConfirmButtons(false);
  }
  
  const renderDict = {
    accounts:<AccountInputs Datafunc={DataUpdateHandler} InputType={inputType}/>,
    builds:<BuildsInputs Datafunc={DataUpdateHandler} InputType={inputType}/>,
    itens:<ItemInputs Datafunc={DataUpdateHandler} InputType={inputType}></ItemInputs>,
    monsters:<MonsterImputs Datafunc={DataUpdateHandler} InputType={inputType}/>
  }

  return (
    <div className="form-c">
      <form className="form" id="form">
        {renderDict[props.Type]}
      </form>

      {ConfirmButtons ? (
        <div className="buttons-c">
          <button onClick={confirmHandler}>Save</button>
          <button onClick={discardHandler}>Discard</button>
        </div>
      ) : (
        <div className="buttons-c">
          <button onClick={()=>inputRenderHandler('add')}>ADD</button>
          <button onClick={()=>inputRenderHandler('update')}>UPDATE</button>
          <button onClick={()=>inputRenderHandler('delete')}>DELETE</button>
        </div>
      )}
    </div>
  );
};

export default BaseCrud;
