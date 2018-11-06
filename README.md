# meetforacause
This application was created in under 24 hours at Athena IEEE Women's Hackathon held at NITK Surathkal.

## Installation
Enter the following commands in your terminal

### Install components 
```bash
sudo apt-get update
sudo apt-get install python-pip
```
### Clone the repository
```git clone https://github.com/Namrata7199/meetforacause```

### Set up Virtual Environment and Install Requirements
```bash
python3 -m venv meetup
source meetup/bin/activate
cd meetforacause
pip install -r requirements.txt
```
### Generate Google Maps API Key
- Generate an API key for Places API or Maps JavaScript API at ```https://console.cloud.google.com/google/maps-apis``` 
- Paste the key in ```meetup/views.py``` and ```templates/event_details.html```

### Migrate Database and Run
```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
