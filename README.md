# -Browser-Fingerprint-Collector
A lightweight Flask application that collects and analyzes browser fingerprints for research and analytics purposes.

## Overview

This application demonstrates browser fingerprinting techniques by collecting various browser and system characteristics from visitors. It includes a real-time dashboard to visualize collected data and analyze user patterns.

## Features

- **Automatic Fingerprint Collection**: Collects browser data automatically when users visit the site
- **Real-time Dashboard**: Visualizes collected fingerprints with interactive charts
- **RESTful API**: Provides endpoints for data collection and retrieval
- **In-memory Storage**: Simple data persistence (easily replaceable with database)
- **Responsive Design**: Works across different devices and screen sizes

## Collected Data Points

The application collects the following browser fingerprint data:

- **User Agent**: Browser and OS information
- **Language**: Browser language settings
- **Platform**: Operating system platform
- **Screen Resolution**: Display dimensions
- **Color Depth**: Display color capability
- **Timezone**: User's timezone setting
- **Plugins**: Installed browser plugins
- **Timestamp**: When the data was collected

## Project Structure

```
browser-fingerprinting/
│
├── app.py                 # Main Flask application
├── templates/
│   ├── index.html        # Main collection page
│   └── dashboard.html    # Analytics dashboard
└── README.md            # This file
```

## Installation

1. **Clone or download the project files**

2. **Install required dependencies**:
   ```bash
   pip install flask
   ```

3. **Run the application**:
   ```bash
   python app.py
   ```

4. **Access the application**:
   - Main page: http://localhost:5000
   - Dashboard: http://localhost:5000/dashboard
   - API endpoint: http://localhost:5000/fingerprints

## API Endpoints

### GET /
- **Description**: Main fingerprint collection page
- **Response**: HTML page that automatically collects visitor fingerprints

### GET /dashboard
- **Description**: Analytics dashboard showing collected data
- **Response**: HTML page with charts and visualizations

### POST /collect
- **Description**: Endpoint for submitting fingerprint data
- **Content-Type**: application/json
- **Request Body**: JSON object with fingerprint data
- **Response**: JSON confirmation with received data

### GET /fingerprints
- **Description**: Retrieve all collected fingerprints
- **Response**: JSON array of all fingerprint objects

## Usage Examples

### Viewing Collected Data
Visit `http://localhost:5000/fingerprints` to see all collected fingerprints in JSON format.

### Manual Data Submission
```javascript
fetch('/collect', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
        userAgent: navigator.userAgent,
        language: navigator.language,
        platform: navigator.platform,
        screenResolution: `${screen.width}x${screen.height}`,
        colorDepth: screen.colorDepth,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        plugins: Array.from(navigator.plugins).map(p => p.name)
    })
});
```

## Development

### Adding New Fingerprint Data Points

1. **Update the JavaScript collection code** in `templates/index.html`:
   ```javascript
   const fingerprint = {
       // existing fields...
       newField: /* collection logic */
   };
   ```

2. **Update dashboard visualizations** in `templates/dashboard.html` as needed

### Database Integration

To replace in-memory storage with a database:

1. **Install database dependencies** (e.g., SQLAlchemy for SQLite/PostgreSQL)
2. **Replace the fingerprints list** with database models
3. **Update the collect() and view() functions** to use database operations

Example with SQLite:
```python
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///fingerprints.db'
db = SQLAlchemy(app)

class Fingerprint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_agent = db.Column(db.Text)
    # ... other fields
```

## Security Considerations

- **Privacy**: This application collects potentially sensitive browser information
- **Consent**: Consider implementing user consent mechanisms
- **Data Protection**: Implement appropriate data retention and deletion policies
- **Rate Limiting**: Add rate limiting to prevent abuse
- **HTTPS**: Use HTTPS in production to protect data in transit

## Legal and Ethical Considerations

- **Transparency**: Inform users about data collection
- **Purpose Limitation**: Only collect data necessary for your specific use case
- **Compliance**: Ensure compliance with relevant privacy laws (GDPR, CCPA, etc.)
- **Opt-out**: Consider providing opt-out mechanisms

## Production Deployment

For production deployment:

1. **Set debug=False** in app.py
2. **Use a production WSGI server** (e.g., Gunicorn, uWSGI)
3. **Implement proper database storage**
4. **Add authentication** for dashboard access
5. **Set up proper logging**
6. **Configure environment variables** for sensitive settings

Example production setup:
```bash
pip install gunicorn
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is provided for educational and research purposes. Please ensure compliance with applicable privacy laws and ethical guidelines when using browser fingerprinting techniques.

## Troubleshooting

### Common Issues

1. **Port already in use**: Change the port in app.py or kill the process using port 5000
2. **Template not found**: Ensure the templates/ directory exists with the HTML files
3. **Chart not displaying**: Verify Chart.js CDN is accessible and data is being passed correctly

### Debug Mode

The application runs in debug mode by default for development. Error messages and stack traces will be displayed in the browser to help with troubleshooting.

## Future Enhancements

- Add more sophisticated fingerprinting techniques (Canvas, WebGL, Audio)
- Implement user tracking across sessions
- Add export functionality for collected data
- Create more detailed analytics and reporting
- Add real-time updates to the dashboard
- Implement data anonymization features
