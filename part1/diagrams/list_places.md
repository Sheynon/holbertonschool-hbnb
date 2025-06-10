sequenceDiagram
    participant User
    participant API
    participant PlaceModel
    participant Database

    User->>API: GET /places?city_id=xyz
    API->>PlaceModel: get_places_by_city(city_id)
    PlaceModel->>Database: SELECT * FROM places WHERE city_id=xyz
    Database-->>PlaceModel: return place list
    PlaceModel-->>API: return place data
    API-->>User: 200 OK + places list
