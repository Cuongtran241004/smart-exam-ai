#!/bin/bash

echo "🚀 Building and Testing Intelligent Online Exam Proctoring System API"
echo "=================================================================="

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

echo "✅ Docker and Docker Compose are installed"

# Build the Docker image
echo "🔨 Building Docker image..."
docker-compose build

if [ $? -ne 0 ]; then
    echo "❌ Docker build failed"
    exit 1
fi

echo "✅ Docker image built successfully"

# Start the application
echo "🚀 Starting the application..."
docker-compose up -d

# Wait for the application to start
echo "⏳ Waiting for application to start..."
sleep 10

# Check if the application is running
echo "🔍 Checking application health..."
for i in {1..30}; do
    if curl -f http://localhost:8000/health &> /dev/null; then
        echo "✅ Application is running and healthy"
        break
    fi
    
    if [ $i -eq 30 ]; then
        echo "❌ Application failed to start or is not healthy"
        docker-compose logs
        docker-compose down
        exit 1
    fi
    
    echo "⏳ Waiting... ($i/30)"
    sleep 2
done

# Run tests
echo "🧪 Running tests..."
python test_api.py

if [ $? -ne 0 ]; then
    echo "❌ Tests failed"
    docker-compose down
    exit 1
fi

echo "✅ All tests passed!"

# Show application info
echo ""
echo "🎉 Application is ready!"
echo "📱 API Documentation: http://localhost:8000/docs"
echo "🔧 Health Check: http://localhost:8000/health"
echo "🧪 Test UI: Open test_ui.html in your browser"
echo ""
echo "To stop the application, run: docker-compose down"
echo "To view logs, run: docker-compose logs -f" 