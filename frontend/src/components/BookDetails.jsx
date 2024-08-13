import { useState } from "react";
import { useNavigate } from "react-router-dom";
import api from "../api";
import "../styles/Book.css";

const BookDetails = ({ book }) => {
    return (
        <div>
            <h2>{book.title}</h2>
            <p>
                <strong>Description:</strong> {book.description}
            </p>
            <p>
                <strong>ISBN:</strong> {book.isbn}
            </p>
            <p>
                <strong>Author:</strong> {book.author}
            </p>
        </div>
    );
};

const BookSummary = ({ book }) => {
    const navigate = useNavigate();

    return (
        <div
            className="book-details"
            onClick={() => navigate(`/book/${book.id}`)}
        >
            <h2>{book.title}</h2>
            <p>
                <strong>Description:</strong> {book.description}
            </p>
        </div>
    );
};

const NewBook = () => {
    const [newBook, setNewBook] = useState(false);
    const [description, setDescription] = useState("");
    const [title, setTitle] = useState("");
    const [ISBN, setISBN] = useState("");
    const [author, setAuthor] = useState("");
    const route = "/api/books/create/"
    
    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const res = await api.post(route, { title, description, ISBN, author });
        } catch (error) {
            alert(error);
        } finally {
            setNewBook(false);
        }
    };

    if (!newBook) {
        return (
            <div className="new-book-button"
                onClick={() => {
                    setNewBook(true);
                }}
            >
                Register new book
            </div>
        );
    }

    return (
        <form className="new-book-form"
            onSubmit={handleSubmit}
        >
            <h2>Create a Book</h2>
            <label htmlFor="title">Title:</label>
            <br />
            <input
                type="text"
                id="title"
                name="title"
                required
                onChange={(e) => setTitle(e.target.value)}
                value={title}
            />
            <br />
            <label htmlFor="description">Description:</label>
            <br />
            <textarea
                id="description"
                name="description"
                required
                onChange={(e) => setDescription(e.target.value)}
                value={description}
            />
            <br />
            <label htmlFor="ISBN">ISBN:</label>
            <input
                type="text"
                id="isbn"
                name="isbn"
                required
                onChange={(e) => setISBN(e.target.value)}
                value={ISBN}
            />
            <br />
            <label htmlFor="Author">Author:</label>
            <input
                type="text"
                id="author"
                name="author"
                required
                onChange={(e) => setAuthor(e.target.value)}
                value={author}
            />
            <br />
            <input type="submit" value="Submit" />
        </form>
    );
};

export { BookDetails, BookSummary, NewBook };
