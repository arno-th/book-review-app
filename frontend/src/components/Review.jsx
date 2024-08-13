import { useState } from "react";
import api from "../api";
import "../styles/Review.css";

const ReviewDetails = ({ review }) => {
    return (
        <div className="review-container">
            <h2>{review.author}</h2>
            <p>
                <strong>Rating:</strong> {review.rating}
            </p>
            <p>
                <strong>Content:</strong> {review.content}
            </p>
        </div>
    );
};

const NewReview = (bookTitle) => {
    const [newReview, setNewReview] = useState(false);
    const [content, setContent] = useState("");
    const [rating, setRating] = useState("");
    const route = "/api/reviews/create/"
    
    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const book = bookTitle
            const res = await api.post(route, { rating, content, book });
        } catch (error) {
            alert(error);
        } finally {
            setNewReview(false);
        }
    };

    if (!newReview) {
        return (
            <div className="new-review-button"
                onClick={() => {
                    setNewReview(true);
                }}
            >
                Review this book
            </div>
        );
    }

    return (
        <form className="new-review-form"
            onSubmit={handleSubmit}
        >
            <h2>Write a review</h2>
            <label htmlFor="rating">Rating:</label>
            <br />
            <input
                type="number"
                id="rating"
                name="rating"
                min="0"
                max="100"
                required
                onChange={(e) => setRating(e.target.value)}
                value={rating}
            />
            <br />
            <label htmlFor="content">Details:</label>
            <br />
            <textarea
                id="content"
                name="content"
                required
                onChange={(e) => setContent(e.target.value)}
                value={content}
            />
            <br />
            <input type="submit" value="Submit" />
        </form>
    );
};

export { ReviewDetails, NewReview };
