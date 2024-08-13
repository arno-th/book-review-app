import { useState, useEffect } from "react";
import api from "../api";
import { BookSummary, NewBook } from "../components/BookDetails";
import "../styles/Home.css";

function Home() {
    const [books, setBooks] = useState([]);

    useEffect(() => {
        getBooks();
    }, []);

    const getBooks = () => {
        api.get("/api/books/")
            .then((res) => res.data)
            .then((data) => {
                setBooks(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    return (
        <div>
            <div>
                {books.map((book) => (
                    <BookSummary book={book} key={book.id} />
                ))}
            </div>
            <NewBook />
        </div>
    );
}
export { Home };
