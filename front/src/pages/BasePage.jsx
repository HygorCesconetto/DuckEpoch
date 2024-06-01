import { useState, useEffect } from "react";
import DataTable from "../components/DataTable/DataTable";
import Navbar from "../components/Navbar/Navbar";
import Calculator from "../components/Calculator/Calculator";
import BaseCrud from "../components/Forms/BaseCrud";
import './style.css';

const BasePage = () => {
  const [Route, setRoute] = useState("accounts");
  const [dataTable, setdataTable] = useState([]);
  const [IsLoading, setIsLoading] = useState(true);

  const fetchApi = () => {
    if(Route !== "calculator"){
    setIsLoading(true);
    fetch(`http://localhost:5000/${Route}`)
      .then((response) => response.json())
      .then((data) => setdataTable(data))
      .catch((error) => console.log(error))
      .finally(() => setIsLoading(false));
    }
  };

  useEffect(() => {
    fetchApi();
  }, []);

  useEffect(() => {
    fetchApi();
  }, [Route]);

  const RouteHandler = (route) => {
    setRoute(route);
  };

  return (
    <div className="page">
      <Navbar Router={RouteHandler} />
      {Route !== "calculator" ? (
        <div className="main">
          <DataTable Load={IsLoading} Data={dataTable} Type={Route} />
          <BaseCrud upData={"aa"} Type={Route} />
        </div>
      ) : (
        <Calculator />
      )}
    </div>
  );
};

export default BasePage;
