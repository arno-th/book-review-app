import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { BookDetails } from "../components/BookDetails";
import { NoteOverview } from "../components/Note"
import { ReviewDetails, NewReview } from "../components/Review";
import api from "../api";

const Book = () => {
    const [book, setBook] = useState(null);
    const [notes, setNotes] = useState([]);
    const [reviews, setReviews] = useState([]);
    const { bookId } = useParams();

    useEffect(() => {
        getBook();
        getNotes();
        getReviews();
    }, []);

    const getBook = () => {
        console.log(`Getting book, id: ${bookId}`)
        api.get(`/api/books/${bookId}/`)
            .then((res) => res.data)
            .then((data) => {
                setBook(data);
                console.log(data);
            })
            .catch((err) => alert(err));
    };

    const getNotes = () => {
        console.log("Getting notes");
        api.get("/api/notes/")
            .then((res) => res.data)
            .then((data) => {
                setNotes(data);
                console.log(data);
                
            })
            .catch((err) => alert(err));
    };

    const getReviews = () => {
        console.log("Getting reviews");
        api.get("/api/reviews/")
            .then((res) => res.data)
            .then((data) => {
                setReviews(data);
                console.log(data);
                
            })
            .catch((err) => alert(err));
    };

    if (!book || notes.length === 0 || reviews.length === 0) {
        return <div>Loading book details...</div>;
    }

    return (
        <div className="app">
            <h1>Book Details</h1>
            <BookDetails book={book} />
            <div>
                <h2>Notes</h2>
                {notes.map((note) => (
                    <NoteOverview note={note} key={note.id} />
                ))}
            </div>
            <div>
                <h2>Reviews</h2>
                <NewReview bookTitle={book.title} />
                {reviews.map((review) => (
                    <ReviewDetails review={review} key={review.id} />
                ))}
            </div>
        </div>
    );
};

export {Book};
