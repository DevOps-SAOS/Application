# Math Exercise Generator Application

A comprehensive web application for generating and practicing mathematical exercises, built with Node.js, Express, and modern web technologies. The application includes full DevOps automation with Docker, Ansible, and AWS deployment capabilities.

## 🚀 Features

- **Interactive Math Exercises**: Generate random mathematical problems for addition, subtraction, multiplication, and division
- **Real-time Feedback**: Immediate validation of user answers with visual feedback
- **Responsive Design**: Modern, mobile-friendly user interface
- **Multi-language Support**: Hebrew interface with extensible language support
- **Docker Containerization**: Easy deployment and scaling
- **Automated Infrastructure**: Complete AWS infrastructure provisioning with Ansible
- **CI/CD Ready**: Automated deployment pipeline support

## 🏗️ Architecture

```
Application/
├── src/                    # Frontend source files
│   ├── index.html         # Main HTML template
│   ├── script.js          # JavaScript logic
│   └── style.css          # Styling
├── server.js              # Express.js backend server
├── Dockerfile             # Docker container configuration
├── docker-compose.yml     # Multi-container orchestration
├── ansible/               # Infrastructure automation
│   ├── deploy_server_app.yml
│   ├── destroy_everything.yml
│   └── group_vars/        # Environment variables
└── package.json           # Node.js dependencies
```

## 🛠️ Technology Stack

### Frontend

- **HTML5**: Semantic markup with modern standards
- **CSS3**: Responsive design with modern styling
- **JavaScript (ES6+)**: Interactive functionality and exercise generation

### Backend

- **Node.js**: JavaScript runtime environment
- **Express.js**: Web application framework
- **Static File Serving**: Efficient delivery of frontend assets

### DevOps & Infrastructure

- **Docker**: Application containerization
- **Docker Compose**: Multi-container orchestration
- **Ansible**: Infrastructure automation and configuration management
- **AWS**: Cloud infrastructure (EC2, VPC, Security Groups)
- **Ubuntu**: Server operating system

## 📋 Prerequisites

Before running this application, ensure you have the following installed:

- **Node.js** (v18 or higher)
- **npm** (Node Package Manager)
- **Docker** and **Docker Compose**
- **Ansible** (for infrastructure deployment)
- **AWS CLI** configured with appropriate credentials
- **SSH key pair** for AWS EC2 instances

## 🚀 Quick Start

### Local Development

1. **Clone the repository**

   ```bash
   git clone <your-repository-url>
   cd Application
   ```

2. **Install dependencies**

   ```bash
   npm install
   ```

3. **Start the development server**

   ```bash
   npm start
   ```

4. **Open your browser**
   Navigate to `http://localhost:3000`

### Docker Deployment

1. **Build and run with Docker Compose**

   ```bash
   docker-compose up -d
   ```

2. **Access the application**
   Open your browser to `http://localhost:80`

## 🐳 Docker Configuration

### Dockerfile

The application uses a multi-stage Docker build process:

- **Base Image**: Node.js 20 Alpine for optimal size
- **Dependencies**: Installed from package.json
- **Application**: Copied and configured for production

### Docker Compose

- **Port Mapping**: 80:3000 (host:container)
- **Environment**: Production configuration
- **Container Name**: `math_exercise_app`

## ☁️ AWS Infrastructure Deployment

### Automated Setup with Ansible

The project includes comprehensive Ansible playbooks for automated AWS infrastructure provisioning:

#### Prerequisites

- Configure AWS credentials
- Set up SSH key pairs
- Install required Ansible collections

#### Deployment Steps

1. **Configure environment variables**

   ```bash
   # Edit ansible/group_vars/env
   vpc_name: "math-app-vpc"
   aws_region: "us-east-1"
   server_type: "t3.micro"
   ```

2. **Run the deployment playbook**
   ```bash
   ansible-playbook ansible/deploy_server_app.yml
   ```

#### Infrastructure Components Created

- **VPC**: Custom virtual private cloud
- **Subnets**: Public and private network segments
- **Internet Gateway**: External connectivity
- **Route Tables**: Network routing configuration
- **Security Groups**: Firewall rules (HTTP, SSH)
- **EC2 Instance**: Ubuntu server with Docker
- **EBS Volume**: Persistent storage

### Manual Infrastructure Setup

If you prefer manual setup:

1. **Create VPC and networking components**
2. **Launch EC2 instance with Ubuntu**
3. **Configure security groups**
4. **Install Docker and dependencies**
5. **Deploy application**

## 🔧 Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
NODE_ENV=production
PORT=3000
AWS_REGION=us-east-1
DOCKER_USER=your-dockerhub-username
DOCKER_TOKEN=your-dockerhub-token
```

### Ansible Variables

Configure `ansible/group_vars/env`:

```yaml
vpc_name: "math-app-vpc"
network: "10.0.0.0/16"
subnet_public: "10.0.1.0/24"
aws_region: "us-east-1"
server_type: "t3.micro"
keypair: "your-keypair-name"
```

## 📱 Application Usage

### Exercise Types

- **Addition (+)**: Practice basic addition skills
- **Subtraction (-)**: Improve subtraction abilities
- **Multiplication (×)**: Master multiplication tables
- **Division (÷)**: Learn division concepts

### User Interface

1. Select the desired operation type
2. Click "Generate Exercise" to create a new problem
3. Enter your answer in the input field
4. Click "Check Answer" for immediate feedback
5. View results and continue practicing

## 🧪 Testing

### Python Test Script

The project includes `test_pass_gen.py` for testing password generation functionality.

### Manual Testing

- Test all mathematical operations
- Verify responsive design on different screen sizes
- Check error handling and edge cases

## 🔒 Security Considerations

- **Security Groups**: Restrict access to necessary ports only
- **SSH Keys**: Use key-based authentication for server access
- **Environment Variables**: Store sensitive data securely
- **Docker Security**: Run containers with minimal privileges

## 📊 Monitoring and Logging

### Application Logs

- Express.js server logs
- Docker container logs
- AWS CloudWatch integration (configurable)

### Health Checks

- HTTP endpoint monitoring
- Container health status
- Infrastructure availability

## 🚀 Deployment Pipeline

### Automated Workflow

1. **Code Push**: Triggers CI/CD pipeline
2. **Build**: Docker image creation
3. **Test**: Automated testing suite
4. **Deploy**: Ansible infrastructure provisioning
5. **Verify**: Health checks and monitoring

### Manual Deployment

```bash
# Build and push Docker image
docker build -t your-username/math_exercise_app:latest .
docker push your-username/math_exercise_app:latest

# Deploy with Ansible
ansible-playbook ansible/deploy_server_app.yml
```

## 🧹Cleanup

### Destroy Infrastructure

```bash
ansible-playbook ansible/destroy_everything.yml
```

### Remove Docker Resources

```bash
docker-compose down --volumes --remove-orphans
docker system prune -a
```
