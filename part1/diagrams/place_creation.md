sequenceDiagram
    participant User
    participant API
    participant PlaceModel
    participant Database

    User->>API: POST /places {name, city_id, ...}
    API->>PlaceModel: create_place(data)
    PlaceModel->>Database: INSERT INTO places
    Database-->>PlaceModel: return confirmation
    PlaceModel-->>API: return new place object
    API-->>User: 201 Created
