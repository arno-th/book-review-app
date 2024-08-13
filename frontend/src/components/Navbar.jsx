import { useState } from "react";
import "../styles/Navbar.css";
import { Link } from "react-router-dom";

function Navbar() {
    const [menuOpen, setMenuOpen] = useState(false);

    return (
        <nav>
            <Link to="/" className="title">
                Home
            </Link>
            <div className="menu" onClick={() => setMenuOpen(!menuOpen)}>
                <span></span>
                <span></span>
                <span></span>
            </div>
            <ul className={menuOpen ? "open" : ""}>
                <li>
                    <Link to="/Login">Login</Link>
                </li>
                <li>
                    <Link to="/Register">Register</Link>
                </li>
                <li>
                    <Link to="/Logout">Logout</Link>
                </li>
            </ul>
        </nav>
    );
}
export default Navbar;
