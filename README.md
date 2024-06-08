
# Mazoon Aluminum

## Installation

### Virtual Environment Setup

#### Windows

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   ```bash
   .venv\Scripts\activate
   ```

#### Linux

1. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```
2. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

### Cleaning the Environment

If you want to clear the environment:

1. Uninstall all packages:
   ```bash
   pip uninstall -r requirements.txt -y
   ```
2. Purge the pip cache:
   ```bash
   pip cache purge
   ```

### Upgrading pip

To upgrade pip:

```bash
python -m pip install --upgrade pip
```

### Installing Requirements

#### Windows

1. Install the requirements:
   ```bash
   pip install -r .\requirements.txt
   ```

#### Linux

1. Install the requirements:
   ```bash
   pip install -r ./requirements.txt
   ```

### Installing Bootstrap

To install Bootstrap using npm:

```bash
npm install
```

### Run Development Server

To run the development server:

```bash
python manage.py runserver
```

### Migrate

To apply database migrations:

```bash
python manage.py migrate
```

### Make Messages

To create translation messages:

```bash
django-admin makemessages -l ar
```

### Compile Messages

To compile translation messages:

#### Windows

```bash
py .\manage.py compilemessages
```

#### Linux

```bash
python manage.py compilemessages
```


## update repo in VPS
#### Make settings.py assume unchanged
```bash
git update-index --assume-unchanged mazoon_aluminum/settings.py
```
#### Pull the latest changes from GitHub, assuming the default branch is 'master'
```bash
git pull origin master
```

#### Revert the assume-unchanged setting
```bash
git update-index --no-assume-unchanged mazoon_aluminum/settings.py
```