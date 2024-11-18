
# **Shop Finding and Navigation System**

### **Course**: Data Structures & Algorithms - COMP1002/5008  
**Technologies**: Graphs, Depth-First Search (DFS), Breadth-First Search (BFS), Hash Tables, Heaps  
**Duration**: September 2023 - October 2023
**Purpose**: Academic Assignment- DSA- Curtin University

---

## **Project Overview**
The **Shop Finding and Navigation System** is a comprehensive project designed to simulate and manage a network of shops in a shopping center or mall. This system utilizes various data structures to efficiently model, search, and navigate through a network of shops. It includes functionalities for graph traversal, shop information retrieval, and ratings management, providing a robust solution for shop navigation and management.

---

## **Key Features and Contributions**

### 1. **Graph Representation**
- Utilized graph data structures (nodes and edges) to model shops and their connections.
- Built an adjacency list to visualize the network of shops and pathways.

### 2. **Node Operations**
- **Add, Delete, and Update**: Functionality for managing shop nodes (stores) with attributes like:
  - **Shop Number**: Unique identifier for each shop.
  - **Name**: Name of the shop.
  - **Category**: Type of store (e.g., clothing, electronics).
  - **Location**: Coordinates or section within the mall.
  - **Customer Rating**: Average rating provided by customers.

### 3. **Edge Operations**
- **Add, Delete, and Update**: Functionality for managing connections (edges) between shops.
- Allows for dynamic modifications to the shopping network.

### 4. **Graph Traversal (DFS & BFS)**
- Developed algorithms for **Depth-First Search (DFS)** and **Breadth-First Search (BFS)** to:
  - Compute paths between shops.
  - Determine the shortest path, comparing results from both algorithms.

### 5. **Instant Shop Search & Information Retrieval**
- Integrated a **hash table** to quickly search for shops by category.
- Enables users to efficiently retrieve detailed information about specific shops.

### 6. **Ratings Management with Heaps**
- Implemented a **max-heap data structure** to manage shop ratings.
- Allows users to view and sort shops within a category based on their ratings.

### 7. **Error Handling & Real-Time Updates**
- Incorporated error checking to ensure system integrity.
- Supports real-time updates as new shops are added, removed, or when connections between shops change.

---

## **Technologies & Algorithms Used**
- **Data Structures**: Graphs, Hash Tables, Heaps
- **Algorithms**: Depth-First Search (DFS), Breadth-First Search (BFS)
- **Programming Language**: Python

---

## **How to Run the Project**
1. Clone this repository:
    ```bash
    git clone https://github.com/SanjanaJayaramM93/Shop-Finding-Navigation-System.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Shop-Finding-Navigation-System
    ```
3. Install the necessary dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the main script:
    ```bash
    python main.py
    ```

---

## **Future Enhancements**
- Implement additional algorithms for optimized pathfinding, such as Dijkstra’s or A*.
- Enhance the user interface with a graphical representation of the mall and shops.
- Add support for real-time user feedback and ratings via a web-based interface.

---

## **Contributors**
- Sanjana Jayaram Mottemmal (https://github.com/SanjanaJayaramM93)

---

## **License**
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
