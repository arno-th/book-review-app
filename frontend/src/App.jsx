import react from 'react'
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom"
import {Login, Register, Home, NotFound, Book} from './pages'
import ProtectedRoute from "./components/ProtectedRoute"
import Navbar from "./components/Navbar"
import './styles/App.css'

function Logout() {
  localStorage.clear()
  return <Navigate to="/login" />
}

function RegisterAndLogout() {
  localStorage.clear()
  return <Register />
}

function App() {

  return (<div className="App">
    <BrowserRouter>
      <Navbar />
      <Routes>
        <Route 
          path="/"
          element={
            <ProtectedRoute>
              <Home />
            </ProtectedRoute>
          }
        />
        <Route 
          path="/book/:bookId"
          element={
            <ProtectedRoute>
              <Book />
            </ProtectedRoute>
          }
        />
        <Route path="/login" element={<Login />} />
        <Route path="/logout" element={<Logout />} />
        <Route path="/register" element={<RegisterAndLogout />} />
        <Route path="*" element={<NotFound />} />
      </Routes>
    </BrowserRouter>
    </div>
  )
}

export default App
