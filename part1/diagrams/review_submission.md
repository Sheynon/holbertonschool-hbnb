sequenceDiagram
    participant User
    participant API
    participant ReviewModel
    participant Database

    User->>API: POST /places/:id/reviews {text, user_id}
    API->>ReviewModel: create_review(data)
    ReviewModel->>Database: INSERT INTO reviews
    Database-->>ReviewModel: return confirmation
    ReviewModel-->>API: return new review object
    API-->>User: 201 Created
