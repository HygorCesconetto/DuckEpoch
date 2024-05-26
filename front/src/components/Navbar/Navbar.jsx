const Navbar = ({Router}) =>{

    const routeChangeHandler =(e) =>{
        const value = e.target.value;
        Router(value);
    }   

    return(
        <div className="Navbar">
            <button onClick={routeChangeHandler} value={"accounts"}>Accounts</button>
            <button onClick={routeChangeHandler} value={"builds"}>Builds</button>
            <button onClick={routeChangeHandler} value={"itens"}>Itens</button>
            <button onClick={routeChangeHandler} value={"monsters"}>Monsters</button>
            <button onClick={routeChangeHandler} value={"calculator"}>DPS Calculator</button>
            <button>Login</button>
        </div>
    )
}

export default Navbar