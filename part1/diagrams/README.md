# Sequence Diagrams for HBnB API Calls

## Objective

This document presents four sequence diagrams that illustrate how the HBnB application handles specific API calls. Each diagram shows the flow of information between the three main layers:

- **Presentation Layer**: Responsible for receiving API requests (e.g., HTTP endpoints).
- **Business Logic Layer**: Validates, processes data, and applies application rules (e.g., models).
- **Persistence Layer**: Manages data storage and retrieval (e.g., database).

These diagrams help visualize how components interact to fulfill user requests.

---

## Sequence Diagrams

### 1. `user_registration.md`
**Use Case**: A new user signs up for an account.  
**Flow**:
- The client sends a registration request to the API.
- The API validates and forwards the request to the User Model.
- The User Model saves the new user in the database.
- A success or failure response is returned.

---

### 2. `place_creation.md`
**Use Case**: A registered user creates a new place listing.  
**Flow**:
- The API receives the creation request with the place data.
- The Place Model validates and processes the data.
- The new place is saved to the database.
- A success response with the created place is returned.

---

### 3. `review_submission.md`
**Use Case**: A user submits a review for an existing place.  
**Flow**:
- The API receives the review data.
- The Review Model validates the review and ensures the place exists.
- The review is stored in the database.
- A confirmation is returned to the user.

---

### 4. `list_places.md`
**Use Case**: A user requests a list of places, possibly with filters.  
**Flow**:
- The API receives a GET request.
- The Place Model fetches the list of places based on criteria.
- The results are returned from the database.
- The list is returned as a JSON response to the user.

---

## How to View the Diagrams

Each `.md` file uses **Mermaid.js** syntax.

### Option 1: Visualize in VS Code
- Install the [Markdown Preview Mermaid Support](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid) extension.
- Open the file and preview it with `Ctrl+Shift+V`.

### Option 2: Use Online Tool
- Copy the Mermaid code into [https://mermaid.live](https://mermaid.live/).
- You will see a live-rendered diagram.

---

## Purpose of These Diagrams

These diagrams are intended to:
- Clarify system behavior for each API call.
- Serve as technical documentation.
- Help with debugging, implementation, and communication between team members.

---

## Next Steps

- Add the diagrams to your project repository under `part1/diagrams/`.
- Include the diagrams as part of your project documentation.
- Use them to refine your understanding of the backend architecture.


