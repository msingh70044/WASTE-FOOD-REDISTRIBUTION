# Share Bite - Food Recycling App

## Overview
Share Bite is a food recycling application designed to connect NGOs with restaurants that have excess edible food. The app facilitates the donation of surplus food to NGOs, ensuring that it reaches those in need while reducing food waste.

## Features
- Connects NGOs with restaurants to facilitate food donations.
- Provides a user-friendly interface for NGOs, restaurants, fund donors, and admins.
- Displays categories of food details on the homepage.
- Includes pages for login, privacy policy, terms and conditions, and contact information.

## Project Structure
```
share-bite
├── app
│   ├── __init__.py
│   ├── routes.py
│   ├── models.py
│   ├── forms.py
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── login.html
│       ├── privacy.html
│       ├── terms.html
│       └── contact.html
├── static
│   ├── css
│   │   └── styles.css
│   └── js
│       └── scripts.js
├── config.py
├── requirements.txt
└── README.md
```

## Installation
1. Clone the repository:
   ```
   git clone <repository-url>
   ```
2. Navigate to the project directory:
   ```
   cd share-bite
   ```
3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```
   python app/__init__.py
   ```
2. Open your web browser and go to `http://localhost:5000` to access the Share Bite application.

## Contributing
Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
