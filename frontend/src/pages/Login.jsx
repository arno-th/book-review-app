import { useNavigate } from "react-router-dom";
import Form from "../components/Form";

function Login() {
    const navigate = useNavigate();

    return (
        <div>
           <Form route="/api/token/" method="login" />
           <button className="register-button" onClick={() => navigate("/register")}>
                    Register
                </button>
        </div>
    );
}

export {Login};
