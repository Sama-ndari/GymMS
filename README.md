# GymMS - Sports Facility Management System

A comprehensive and modern gym management system built with Django 5.0, featuring a premium 2025 UI design with glassmorphism effects and advanced functionality for managing gym operations, memberships, equipment, and coaching services.

## 🏋️ Features

### Core Management
- **Member Management**: Complete member registration, profile management, and subscription tracking
- **Coach Management**: Coach profiles, specializations, and schedule management
- **Equipment Management**: Track gym equipment, maintenance schedules, and availability
- **Subscription Management**: Flexible membership plans and billing management
- **Session Management**: Book and manage training sessions
- **Progress Tracking**: Monitor member fitness progress and achievements

### Modern UI/UX
- **Premium 2025 Design**: Glassmorphism effects, gradient backgrounds, and smooth animations
- **Responsive Design**: Optimized for desktop, tablet, and mobile devices
- **Interactive Dashboard**: Real-time statistics and data visualization
- **Dark Theme Elements**: Modern footer with premium styling
- **Accessibility**: WCAG compliant with proper focus states and ARIA labels

### Technical Features
- **Role-based Access Control**: Different permissions for admins, coaches, and members
- **Secure Authentication**: Custom authentication middleware and session management
- **Database Optimization**: MySQL with utf8mb4 charset for full Unicode support
- **Environment Configuration**: Secure configuration management with .env files

## 📋 Prerequisites

Before setting up the project, ensure you have the following installed:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **MySQL 8.0+** - [Download MySQL](https://dev.mysql.com/downloads/)
- **pip** - Python package installer (comes with Python)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **virtualenv** - For creating isolated Python environments

### System-Specific Requirements

**Linux/macOS:**
```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv mysql-server git

# macOS (with Homebrew)
brew install python mysql git
```

**Windows:**
- Install Python from the official website
- Install MySQL Community Server
- Install Git for Windows
- Use Command Prompt or PowerShell for commands

## 🚀 Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Sama-ndari/GymMS.git
cd GymMS
```

### 2. Create Virtual Environment

**Linux/macOS:**
```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows:**
```cmd
python -m venv .venv
.venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## 🗄️ Database Setup

### 1. Create MySQL Database

```sql
-- Login to MySQL as root
mysql -u root -p

-- Create database
CREATE DATABASE gym_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Create user (optional, for security)
CREATE USER 'samandari'@'localhost' IDENTIFIED BY '123456789';
GRANT ALL PRIVILEGES ON gym_db.* TO 'samandari'@'localhost';
FLUSH PRIVILEGES;
EXIT;
```

### 2. Configure Environment Variables

Create a `.env` file in the project root:

```bash
# Copy the example file (if available) or create new
touch .env
```

Add the following configuration to your `.env` file:

```env
# Django Configuration
SECRET_KEY=your-super-secret-key-here-change-this-in-production
DEBUG=True

# Database Configuration
DB_NAME=gymms_db
DB_USER=gymms_user
DB_PASSWORD=your_secure_password
DB_HOST=localhost
DB_PORT=3306
```

**⚠️ Important**: Never commit your `.env` file to version control. It's already included in `.gitignore`.

### 3. Run Database Migrations

```bash
# Create migration files
python manage.py makemigrations

# Apply migrations
python manage.py migrate
```

### 4. Load Sample Data (Optional)

```bash
# If fixtures are available
python manage.py loaddata sample_data.json
```

## 🔄 Reset and Load Default Data

For a clean and consistent testing environment, use the provided script to reset your database and populate it with a complete set of default data. This is the recommended way to get started.

### 1. Run the Data Loader Script

This script will first ask for confirmation, then **delete all existing data**, and finally create a fresh set of test accounts and records.

```bash
# Make sure your virtual environment is active
source .venv/bin/activate

# Run the script
python load_default_data.py
```

Follow the prompt by typing `yes` to confirm the database reset.
## 🏃‍♂️ Running the Application

### 1. Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create an admin account.

### 2. Start Development Server

**With Virtual Environment (Recommended):**
```bash
# Make sure virtual environment is activated
.venv/bin/python manage.py runserver
```

**Standard Method:**
```bash
python manage.py runserver
```

The application will be available at:
- **Main Site**: http://127.0.0.1:8000/
- **Admin Panel**: http://127.0.0.1:8000/admin/

### 3. Access the Application

1. Open your browser and navigate to `http://127.0.0.1:8000/`
2. Use the superuser credentials to access the admin panel
3. Start managing your gym operations!

## 🧪 Default Testing Accounts

After running the `load_default_data.py` script, the following accounts will be available for testing:

### Administrator Accounts

| Name      | Email                 | Password | Role        |
|-----------|-----------------------|----------|-------------|
| Samandari | samandari@gmail.com   | `sam123`  | Super Admin |
| GrandBB   | gdbb@gmail.com        | `gdbb123`  | Admin       |

### Coach Accounts

| Name           | Email                     | Password    | Specialty              |
|----------------|---------------------------|-------------|------------------------|
| Marie Dubois   | marie.dubois@gymms.com    | `marie123`  | Cardio et Endurance    |
| Pierre Martin  | pierre.martin@gymms.com   | `pierre123` | Yoga et Pilates        |
| Sophie Laurent | sophie.laurent@gymms.com  | `sophie123` | CrossFit et HIIT       |
| Thomas Bernard | thomas.bernard@gymms.com  | `thomas123` | Préparation physique   |

### Client Accounts

| Name         | Email                  | Password   |
|--------------|------------------------|------------|
| Jean Dupont  | jean.dupont@email.com  | `jean123`  |
| Alice Martin | alice.martin@email.com | `alice123` |
| Bob Wilson   | bob.wilson@email.com   | `bob123`   |
| Emma Garcia  | emma.garcia@email.com  | `emma123`  |

### Notes on Default Data
- **Activation**: All accounts are created as **active** and ready for immediate login.
- **Assignments**: Sample coach-client assignments are pre-approved.
- **Subscriptions**: Clients have a mix of active and expired subscriptions for testing.
- **Security**: These are weak passwords for testing only. **Do not use them in production.**

## 📝 Important Notes

### Security
- **Never commit `.env` files** to version control
- Change the `SECRET_KEY` in production
- Use strong passwords for database users
- Set `DEBUG=False` in production
- **Change default credentials** in production environments
- All test accounts should be deactivated or removed before deployment

### Platform Compatibility
- **Linux/macOS**: Full support with native commands
- **Windows**: Supported with minor command differences
- **Database**: MySQL backend required (SQLite not recommended for production)

### Development
- The project uses Django 5.0+ with modern Python features
- Bootstrap 5 and FontAwesome for UI components
- Custom CSS with 2025 design trends

## 🤝 Contributing

We welcome contributions to improve GymMS! Please follow these guidelines:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Development Setup
- Follow the installation instructions above
- Create a separate branch for your changes
- Test thoroughly before submitting
- Follow Django and Python best practices

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Samandari**
- GitHub: [@Sama-ndari](https://github.com/Sama-ndari)
- Project Link: [GymMS](https://github.com/Sama-ndari/GymMS)

---

⭐ If you find this project helpful, please consider giving it a star on GitHub!