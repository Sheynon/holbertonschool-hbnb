sequenceDiagram
    participant User
    participant API
    participant UserModel
    participant Database

    User->>API: POST /users {email, password}
    API->>UserModel: create_user(data)
    UserModel->>Database: INSERT INTO users
    Database-->>UserModel: return confirmation
    UserModel-->>API: return new user object
    API-->>User: 201 Created
