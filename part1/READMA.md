# High-Level Package Diagram – HBnB Application

## 📊 Three-Layer Architecture Overview

This diagram represents the high-level architecture of the HBnB application using a **three-layer structure**. It also shows how the **Facade design pattern** facilitates communication between these layers.

---

## 🧱 Layer Descriptions

### 🟩 Presentation Layer
- **Role**: Handles user interaction through the **Command-Line Interface (CLI)** or **RESTful API**.
- **Components**:
  - `APIService`: Exposes HTTP endpoints.
  - `CLIService`: Provides command-line features for development and testing.
- **Communication**: This layer does **not access models or storage directly** — it communicates through the **`HBNBFacade` interface**.

---

### 🟦 Business Logic Layer
- **Role**: Contains the **application's core logic and rules**, manipulating data and enforcing behavior.
- **Components**:
  - Models: `User`, `Place`, `Review`, `Amenity`
  - `HBNBFacade`: A unified interface that coordinates logic and storage operations.
- **Communication**: It interacts with the **Persistence Layer** to store and retrieve data.

---

### 🟨 Persistence Layer
- **Role**: Responsible for **data storage and retrieval**, either via files or a database.
- **Components**:
  - `FileStorage`: JSON-based storage engine.
  - `DBStorage`: SQL-based storage engine (e.g., MySQL).
- **Communication**: Only accessed by the Business Logic Layer (not directly by the Presentation Layer).

---

## 🧩 Facade Pattern Explanation

The **Facade Pattern** is implemented through the `HBNBFacade` class in the Business Logic Layer. It:

- Provides a **single entry point** for the presentation layer.
- Hides the complexity of the system (models, storage).
- Improves **modularity, readability**, and **maintainability**.

---

## 📁 Folder Structure for Submission

