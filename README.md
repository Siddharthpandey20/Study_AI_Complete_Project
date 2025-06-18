# 🚀 Smart Study Tool

> A modern, AI-powered learning platform for effective studying

[![GitHub stars](https://img.shields.io/github/stars/yourusername/smart-study-tool)](https://github.com/yourusername/smart-study-tool/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/yourusername/smart-study-tool)](https://github.com/yourusername/smart-study-tool/network)
[![GitHub issues](https://img.shields.io/github/issues/yourusername/smart-study-tool)](https://github.com/yourusername/smart-study-tool/issues)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## 📋 Table of Contents

- [✨ Features](#-features)
- [🛠️ Tech Stack](#️-tech-stack)
- [📦 Prerequisites](#-prerequisites)
- [🚀 Quick Start](#-quick-start)
- [⚙️ Environment Setup](#️-environment-setup)
- [🏃‍♂️ Running the Application](#️-running-the-application)
- [📸 Screenshots](#-screenshots)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👨‍💻 Author](#-author)

## ✨ Features

- 🔐 **Authentication & Authorization** - Secure user authentication with JWT
- 📱 **Responsive Design** - Mobile-first, responsive UI that works on all devices
- ⚡ **Real-time Updates** - Live data updates using WebSockets
- 🎨 **Modern UI/UX** - Clean, intuitive interface with smooth animations
- 🔍 **Search & Filter** - Advanced search and filtering capabilities
- 📊 **Analytics Dashboard** - Comprehensive data visualization
- 🔒 **Data Security** - Encrypted data storage and secure API endpoints
- 🌙 **Dark Mode** - Toggle between light and dark themes
- **Auto Flashcards**: AI-generated Q&A cards with difficulty levels
- **Interactive MCQs**: Quiz-style questions with instant feedback
- **Smart Explanations**: Detailed explanations for each answer
- **Visual Learning**: Convert notes into beautiful mind maps
- **Interactive Nodes**: Clickable, hierarchical topic structure
- **Color-Coded**: Different colors for different topic levels
- **Step-by-Step**: Personalized learning sequences
- **Time Estimates**: Realistic time planning for each step
- **Prerequisites**: Clear dependency mapping
- **🔴 RED**: Must memorize (critical facts, formulas)
- **🟡 YELLOW**: Good to know (important concepts)  
- **🟢 GREEN**: Bonus/Extra (interesting additions)
- **AI Classification**: Automatic importance detection
- **Question Prediction**: Most likely exam questions
- **Probability Scores**: AI-calculated likelihood (0-100%)
- **Question Types**: Short answer, Long answer, HOTS
- **Smart Categories**: Visual badges for each type

## 🛠️ Tech Stack

### Frontend
- **React** - UI library for building user interfaces
- **Next.js** - React framework for production
- **TypeScript** - Type-safe JavaScript
- **Tailwind CSS** - Utility-first CSS framework
- **Framer Motion** - Animation library

### Backend
- **Node.js** - JavaScript runtime
- **Express.js** - Web application framework
- **MongoDB** / **PostgreSQL** - Database
- **Mongoose** / **Prisma** - Database ORM
- **JWT** - Authentication tokens
- **Socket.io** - Real-time communication
- **FastAPI** - High-performance web framework for Python
- **Google Gemini 1.5 Flash** - AI engine for intelligent prompting and content analysis

### DevOps & Tools
- **Docker** - Containerization
- **GitHub Actions** - CI/CD
- **ESLint** - Code linting
- **Prettier** - Code formatting

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Node.js** (v16.0.0 or higher)
- **npm** (v7.0.0 or higher) or **yarn**
- **Git**
- **MongoDB** or **PostgreSQL** (depending on your setup)
- **Python** (3.8 or higher)
- **pip** (Python package installer)

```bash
# Check versions
node --version
npm --version
git --version
python --version
pip --version
```

## 🚀 Quick Start

### 1. Clone the Repository

```bash
# Clone the repository
git clone https://github.com/yourusername/smart-study-tool.git

# Navigate to project directory
cd smart-study-tool
```

### 2. Install Dependencies

```bash
# Install backend dependencies
pip install -r requirements.txt

# Install frontend dependencies
npm install

# Or using yarn
yarn install
```

### 3. Environment Configuration

```bash
# Copy environment example file
cp .env.example .env

# Edit the .env file with your actual values
nano .env  # or use your preferred editor
```

### 4. Database Setup

```bash
# For MongoDB (if using)
# Make sure MongoDB is running on your system

# For PostgreSQL (if using)
# Create database and run migrations
npm run db:migrate

# Seed the database (optional)
npm run db:seed
```

### 5. Start the Application

```bash
# Development mode
npm run dev

# Or using yarn
yarn dev
```

🎉 **Success!** Your application should now be running at `http://localhost:3000`

## ⚙️ Environment Setup

Create a `.env` file in the root directory and configure the following variables:

### Required Environment Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `DATABASE_URL` | Database connection string | `mongodb://localhost:27017/myapp` |
| `JWT_SECRET` | Secret key for JWT tokens | `your-super-secret-jwt-key` |
| `API_KEY` | Third-party API key | `your-api-key-here` |
| `PORT` | Application port | `3000` |

### Optional Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `NODE_ENV` | Environment mode | `development` |
| `REDIS_URL` | Redis connection string | `redis://localhost:6379` |
| `SMTP_HOST` | Email server host | `smtp.gmail.com` |

> ⚠️ **Important**: Never commit your `.env` file to version control. It contains sensitive information.

## 🏃‍♂️ Running the Application

### Development Mode

```bash
# Start development server
npm run dev

# Start with specific port
PORT=4000 npm run dev
```

### Production Mode

```bash
# Build the application
npm run build

# Start production server
npm start
```

### Docker (Optional)

```bash
# Build Docker image
docker build -t smart-study-tool .

# Run container
docker run -p 3000:3000 smart-study-tool
```

## 📸 Screenshots

### Dashboard
![Dashboard](screenshots/dashboard.png)

### Mobile View
![Mobile](screenshots/mobile.png)

### Dark Mode
![Dark Mode](screenshots/dark-mode.png)

## 🧪 Testing

```bash
# Run all tests
npm test

# Run tests in watch mode
npm run test:watch

# Run tests with coverage
npm run test:coverage
```

## 📁 Project Structure

```
smart-study-tool/
├── 📁 src/
│   ├── 📁 components/        # Reusable UI components
│   ├── 📁 pages/            # Application pages
│   ├── 📁 hooks/            # Custom React hooks
│   ├── 📁 utils/            # Utility functions
│   ├── 📁 styles/           # Global styles
│   └── 📁 types/            # TypeScript type definitions
├── 📁 public/               # Static assets
├── 📁 docs/                 # Documentation
├── 📄 .env.example          # Environment variables example
├── 📄 .gitignore           # Git ignore rules
├── 📄 package.json         # Project dependencies
└── 📄 README.md            # Project documentation
```

## 🐛 Troubleshooting

### Common Issues

1. **Port already in use**
   ```bash
   # Kill process using port 3000
   npx kill-port 3000
   ```

2. **Database connection issues**
   ```bash
   # Check if database is running
   # MongoDB: mongod --version
   # PostgreSQL: pg_ctl status
   ```

3. **Module not found errors**
   ```bash
   # Clear node_modules and reinstall
   rm -rf node_modules package-lock.json
   npm install
   ```

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### Development Workflow

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Your Name**
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your LinkedIn](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

## 🙏 Acknowledgments

- [React](https://reactjs.org/) - The web framework used
- [Node.js](https://nodejs.org/) - Backend runtime
- [MongoDB](https://www.mongodb.com/) - Database
- Contributors and the open-source community

---

<div align="center">
  <p>Made with ❤️ by <a href="https://github.com/yourusername">Your Name</a></p>
  <p>⭐ Star this repository if you found it helpful!</p>
</div>
