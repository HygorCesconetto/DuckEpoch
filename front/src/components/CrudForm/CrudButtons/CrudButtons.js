import axios from 'axios';
import './CrudButtons.css';

const API_URL = "http://localhost:5000/"

const CrudButtons = (props) => {
  const c_add = () => {
    axios.post(`${API_URL}${props.Type}`, props.Data);
  };
  const c_update = () => {
    axios.patch(`${API_URL}${props.Type}`, props.Data);
  };
  const c_delete = () => {
    axios.delete(`${API_URL}${props.Type}/${props.Data["id"]}`);
  };

  return (
    <div className={'CrudButtons'}>
      <button id="buttonAdd" onClick={c_add}>
        ADD
      </button>
      <button id="buttonUpdate" onClick={c_update}>
        UPDATE
      </button>
      <button id="buttonDelete" onClick={c_delete}>
        DELETE
      </button>
    </div>
  );
};

export default CrudButtons;
