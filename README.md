# Virtual Study Group Web Application

## Video Demo: [Link](URL HERE)

## Overview

This web application is designed to help students create, manage, and collaborate in virtual study groups. It provides a comprehensive platform for academic collaboration, resource sharing, and group study coordination.

## Features

- **User Authentication**
  - Secure sign-up and login system
  - Role-based access control
  - User profile management

- **Group Management**
  - Create and join study groups
  - Invite members via email or unique group codes
  - Manage group settings and permissions

- **Meeting Scheduler**
  - Schedule group study sessions
  - Meeting link generation (google meet/ zoom)

- **Resource Sharing**
  - Upload and share study materials
  - Easy resource discovery

- **Communication Tools**
  - Group chat and discussion forum
  - Real-time messaging
  - Collaborative communication

- **Progress Tracking**
  - Individual and group study goal tracking
  - Performance insights
  - Motivation and accountability features

- **Notifications**
  - In-app notifications

## Tech Stack

### Backend

- Flask
- Flask-SQLAlchemy
- Flask-WTF
- Flask-Login

### Frontend

- HTML
- CSS
- Bootstrap
- JavaScript

### Database

- SQLite3 (SQLAlchemy)

### File Storage

- Local Storage

## Files

## Prerequisites

- Python 3.8+
- pip
- Virtual environment (recommended)

## Installation

1. Clone the repository

   ```bash
   git clone https://github.com/Bryanf20/cs50-final-project.git
   cd virtual-study-group
   ```

2. Create a virtual environment

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Set up environment variables
   - Create a `.env` file
   - Add necessary configuration variables

5. Initialize the database

   ```bash
   flask db upgrade
   ```

6. Run the application

   ```bash
   cd virtual-study-group
   flask run
   ```

## Configuration

- Configure database settings in `.env`
- Set up email services for notifications
- Configure file storage options

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Future Works

### Deployment

- Recommended platforms: Heroku, AWS, DigitalOcean
- Use PostgreSQL for production
- Configure environment-specific settings

### Security Considerations

- Implement HTTPS
- Use strong password hashing
- Implement proper access controls
- Regular security audits

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Contact

Bryan .F - <fongangbryan@gmail.com>

Project Link: [https://github.com/Bryanf20/cs50-final-project](https://github.com/Bryanf20/cs50-final-project)

## Acknowledgements

- Flask
- Bootstrap
- SQLAlchemy
- ChatGPT
