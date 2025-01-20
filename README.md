# 90-North
 
# Chat Application

This is a chat application built using Django and Django Channels, providing real-time messaging capabilities. Users can sign up, log in, and chat with each other while storing messages in a database.

## Features

- User authentication (signup and login)
- Real-time messaging using WebSockets
- Display of old messages in the chat interface
- User-friendly interface with a responsive design
- Differentiation between sent and received messages

## Technologies Used

- **Django**: Web framework for building the application
- **Django Channels**: For handling WebSocket connections
- **jQuery**: For DOM manipulation and handling WebSocket events
- **SQLite**: Default database (can be configured to use PostgreSQL or MySQL)

## Setup Instructions

### Prerequisites

- Python 3.6 or higher
- Django
- Django Channels

### Installation

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd chat_app