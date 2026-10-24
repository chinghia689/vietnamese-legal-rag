# 🏛️ Chatbot Luật Việt Nam - RAG Web Application

<div align="center">

**Hệ thống chatbot tư vấn pháp luật công nghệ thông tin sử dụng RAG (Retrieval-Augmented Generation) và LLM**

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)](https://fastapi.tiangolo.com/)
[![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)](https://reactjs.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![LangChain](https://img.shields.io/badge/🦜_LangChain-000000?style=for-the-badge)](https://www.langchain.com/)

</div>

---

## 📋 Mục lục

- [Tính năng](#-tính-năng)
- [Cài đặt nhanh với Docker](#-cài-đặt-nhanh-với-docker)
- [Cài đặt thủ công](#-cài-đặt-thủ-công)
- [Cấu trúc dự án](#-cấu-trúc-dự-án)
- [Tech Stack](#-tech-stack)
- [Cấu hình](#-cấu-hình)
- [API Documentation](#-api-documentation)
- [Development](#-development)
- [Deployment](#-deployment)
- [Văn bản luật được hỗ trợ](#-văn-bản-luật-được-hỗ-trợ)
- [Troubleshooting](#-troubleshooting)
- [Đóng góp](#-đóng-góp)
- [License](#-license)

---

## 🚀 Tính năng

- ✅ **Chat AI thông minh**: Trả lời câu hỏi về luật công nghệ thông tin Việt Nam
- ✅ **RAG Pipeline**: Hybrid retrieval kết hợp ChromaDB (vector) và BM25 (sparse)
- ✅ **Web Interface hiện đại**: React + Vite với glassmorphism design
- ✅ **Dark/Light Mode**: Chuyển đổi theme dễ dàng
- ✅ **Responsive Design**: Hoạt động tốt trên mọi thiết bị
- ✅ **Markdown Support**: Hiển thị câu trả lời định dạng đẹp
- ✅ **Docker Support**: Triển khai dễ dàng với Docker và Docker Compose
- ✅ **Desktop App**: Giao diện CustomTkinter (tùy chọn)

---

## 🐳 Cài đặt nhanh với Docker

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/) (phiên bản 20.10+)
- [Docker Compose](https://docs.docker.com/compose/install/) (phiên bản 2.0+)
- [Groq API Key](https://console.groq.com/keys) (miễn phí)

### Bước 1: Clone repository

```bash
git clone https://github.com/chinghia689/vietnamese-legal-rag.git
cd vietnamese-legal-rag
```

### Bước 2: Cấu hình environment

```bash
# Tạo file .env từ template
cp .env.example .env

# Chỉnh sửa .env và thêm API key của bạn
nano .env  # hoặc dùng editor yêu thích
```

Thêm Groq API key vào file `.env`:
```env
GROQ_API_KEY=your_groq_api_key_here
```

### Bước 3: Khởi chạy với Docker Compose

```bash
# Build và start tất cả services
docker-compose up --build

# Hoặc chạy trong background
docker-compose up -d --build
```

### Bước 4: Truy cập ứng dụng

- **Frontend**: http://localhost:3000
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

### Dừng services

```bash
# Dừng containers
docker-compose down

# Dừng và xóa volumes (dữ liệu ChromaDB)
docker-compose down -v
```

### Development mode với hot-reload

Để chạy frontend với hot-reload trong development:

```bash
docker-compose --profile dev up frontend-dev
```

Frontend sẽ chạy tại: http://localhost:5173

---

## 💻 Cài đặt thủ công

### Prerequisites

- Python 3.11+
- Node.js 20+
- npm hoặc yarn

### Backend Setup

```bash
# 1. Cài đặt dependencies
pip install -r requirements.txt

# 2. Tạo file .env
cp .env.example .env
# Chỉnh sửa .env và thêm GROQ_API_KEY

# 3. Đảm bảo có văn bản luật trong thư mục data/
ls data/

# 4. Chạy server
python main.py
```

Backend sẽ chạy tại: `http://localhost:8000`

### Frontend Setup

```bash
# 1. Di chuyển vào thư mục frontend
cd frontend

# 2. Cài đặt dependencies
npm install

# 3. (Tùy chọn) Cấu hình API URL
echo "VITE_API_URL=http://localhost:8000" > .env

# 4. Chạy development server
npm run dev
```

Frontend sẽ chạy tại: `http://localhost:5173`

---

## 🏗️ Cấu trúc dự án

```
vietnamese-legal-rag/
├── 📁 rag/                          # RAG pipeline modules
│   ├── load_split.py                # Document loader & text splitter
│   ├── embedding.py                 # Vietnamese embeddings (HuggingFace)
│   ├── retriever.py                 # Hybrid retrieval (ChromaDB + BM25)
│   ├── chain.py                     # LLM chain configuration
│   ├── graph.py                     # RAG graph workflow (LangGraph)
│   └── state.py                     # State management
│
├── 📁 frontend/                     # React web interface
│   ├── src/
│   │   ├── components/              # React components
│   │   │   ├── ChatInterface.tsx    # Main chat interface
│   │   │   └── MessageBubble.tsx    # Message display component
│   │   ├── services/                # API service layer
│   │   │   └── api.ts               # Axios API client
│   │   ├── App.tsx                  # Root component
│   │   └── index.css                # Global styles + design system
│   ├── Dockerfile                   # Production build
│   ├── Dockerfile.dev               # Development build
│   └── package.json
│
├── 📁 data/                         # Law documents (.docx)
│   ├── Luat-An-ninh-mang.docx
│   ├── Luat-An-toan-thong-tin-mang.docx
│   ├── Luat-Chuyen-giao-cong-nghe.docx
│   ├── Luat-Cong-nghe-thong-tin.docx
│   ├── Luat-Khoa-hoc-cong-nghe.docx
│   └── Luat-Tri-tue-nhan-tao.docx
│
├── 📁 chroma_db/                    # Vector database (auto-generated)
│
├── 📄 main.py                       # FastAPI backend entry point
├── 📄 client_chatbox_app.py         # Desktop app (CustomTkinter)
├── 📄 Dockerfile                    # Backend Docker image
├── 📄 docker-compose.yml            # Multi-service orchestration
├── 📄 .env.example                  # Environment variables template
├── 📄 requirements.txt              # Python dependencies
└── 📄 README.md                     # This file
```

---

## 🛠️ Tech Stack

### Backend

| Technology | Purpose | Version |
|-----------|---------|---------|
| **FastAPI** | Web framework | Latest |
| **LangChain** | RAG orchestration | Latest |
| **LangGraph** | Workflow management | Latest |
| **ChromaDB** | Vector database | Latest |
| **BM25** | Sparse retrieval | `rank_bm25` |
| **Groq** | LLM provider (Llama 3.1 70B) | Latest |
| **HuggingFace** | Vietnamese embeddings | `keepitreal/vietnamese-sbert` |
| **Transformers** | Model loading | Latest |
| **PyTorch** | Deep learning backend | Latest |
| **Uvicorn** | ASGI server | Latest |

### Frontend

| Technology | Purpose | Version |
|-----------|---------|---------|
| **React 19** | UI library | 19.2.0 |
| **TypeScript** | Type safety | 5.9.3 |
| **Vite 7** | Build tool | 7.2.4 |
| **Axios** | HTTP client | 1.13.2 |
| **react-markdown** | Markdown rendering | 10.1.0 |
| **lucide-react** | Icon library | 0.562.0 |

### DevOps

- **Docker** & **Docker Compose**: Containerization
- **Nginx**: Production web server
- **Git**: Version control

---

## 🔧 Cấu hình

### Environment Variables

#### Backend (`.env`)

```env
# Required: Groq API Key for LLM
GROQ_API_KEY=your_groq_api_key_here

# Optional: Google API Key (for alternative embeddings)
GOOGLE_API_KEY=your_google_api_key_here
```

**Lấy Groq API Key:**
1. Truy cập https://console.groq.com/keys
2. Đăng ký tài khoản miễn phí
3. Tạo API key mới
4. Copy và paste vào file `.env`

#### Frontend (`.env` - optional)

```env
# Backend API URL
VITE_API_URL=http://localhost:8000
```

### CORS Configuration

Backend cho phép requests từ:
- `http://localhost:5173` (Vite dev server)
- `http://localhost:3000` (Production/Docker)

Để thêm origins khác, chỉnh sửa `main.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://your-domain.com"],  # Thêm domain của bạn
    ...
)
```

---

## 📚 Văn bản luật được hỗ trợ

Hệ thống hỗ trợ 6 văn bản luật về công nghệ thông tin của Việt Nam:

1. **Luật An ninh mạng** - Bảo vệ an ninh quốc gia trong không gian mạng
2. **Luật An toàn thông tin mạng** - An toàn, bảo mật thông tin trên mạng
3. **Luật Chuyển giao công nghệ** - Quy định về chuyển giao công nghệ
4. **Luật Công nghệ thông tin** - Khung pháp lý cho ngành CNTT
5. **Luật Khoa học công nghệ** - Hoạt động khoa học và công nghệ
6. **Luật Trí tuệ nhân tạo** - Quy định về AI và ứng dụng

Các file được lưu ở định dạng `.docx` trong thư mục `data/`.

---

## 📝 API Documentation

### Swagger UI

Truy cập tài liệu API tương tác tại: **http://localhost:8000/docs**

### Endpoints

#### POST `/chat`

Gửi câu hỏi và nhận câu trả lời từ chatbot.

**Request:**
```json
{
  "question": "Tuổi nghỉ hưu theo luật lao động là bao nhiêu?"
}
```

**Response:**
```json
{
  "answer": "Theo quy định tại Điều 169, Bộ luật Lao động 2019:\n\n- Nam: 60 tuổi 3 tháng (năm 2022)\n- Nữ: 55 tuổi 4 tháng (năm 2022)\n\nTuổi nghỉ hưu tăng dần theo lộ trình..."
}
```

**cURL Example:**
```bash
curl -X POST http://localhost:8000/chat \
  -H "Content-Type: application/json" \
  -d '{"question": "Luật An ninh mạng quy định gì về bảo vệ dữ liệu?"}'
```

**Python Example:**
```python
import requests

response = requests.post(
    "http://localhost:8000/chat",
    json={"question": "AI được quy định như thế nào trong luật Việt Nam?"}
)
print(response.json()["answer"])
```

---

## 🎨 UI Features

### Design System

- **Glassmorphism**: Giao diện hiện đại với hiệu ứng kính mờ
- **Gradient Accents**: Màu sắc gradient từ tím đến xanh lam
- **Smooth Animations**: Chuyển động mượt mà với CSS transitions
- **Responsive Layout**: Tối ưu cho desktop, tablet, và mobile

### User Experience

- **Auto-scroll**: Tự động cuộn xuống tin nhắn mới
- **Loading States**: Hiển thị trạng thái đang xử lý với animation
- **Copy Message**: Sao chép câu trả lời với một click
- **Keyboard Shortcuts**:
  - `Enter`: Gửi tin nhắn
  - `Shift + Enter`: Xuống dòng
- **Error Handling**: Thông báo lỗi rõ ràng và hữu ích

---

## 👨‍💻 Development

### Running in Development Mode

#### Backend Development

```bash
# Chạy với auto-reload
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Development

```bash
cd frontend
npm run dev
```

### Code Quality

```bash
# Frontend linting
cd frontend
npm run lint

# Type checking
npm run build  # TypeScript được check khi build
```

### Adding New Law Documents

1. Thêm file `.docx` vào thư mục `data/`
2. Restart backend để load và index document mới
3. Document sẽ tự động được xử lý và thêm vào vector database

---

## 🚀 Deployment

### Build Production Images

#### Backend

```bash
docker build -t rag-backend:latest -f Dockerfile .
```

#### Frontend

```bash
docker build -t rag-frontend:latest -f frontend/Dockerfile ./frontend
```

### Deploy with Docker Compose

```bash
# Production deployment
docker-compose up -d --build

# Check service status
docker-compose ps

# View logs
docker-compose logs -f backend
docker-compose logs -f frontend
```

### Manual Production Build

#### Frontend

```bash
cd frontend
npm run build  # Output: dist/
```

Serve với nginx hoặc host tĩnh:

```nginx
server {
    listen 80;
    server_name yourdomain.com;
    root /path/to/frontend/dist;

    location / {
        try_files $uri $uri/ /index.html;
    }
}
```

#### Backend

```bash
# Production server với Gunicorn
gunicorn main:app -w 4 -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:8000

# Hoặc với Uvicorn
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Environment Variables cho Production

```env
# .env (production)
GROQ_API_KEY=production_key_here
GOOGLE_API_KEY=production_key_here

# Có thể thêm:
# LOG_LEVEL=info
# MAX_WORKERS=4
# DATABASE_URL=...
```

---

## 🔍 Troubleshooting

### Docker Issues

#### Problem: "Cannot connect to Docker daemon"
```bash
# Solution: Start Docker service
sudo systemctl start docker

# Hoặc add user vào docker group
sudo usermod -aG docker $USER
newgrp docker
```

#### Problem: "Port already in use"
```bash
# Solution: Kill process using port
sudo lsof -ti:8000 | xargs kill -9
sudo lsof -ti:5173 | xargs kill -9

# Hoặc change ports trong docker-compose.yml
```

#### Problem: "No space left on device"
```bash
# Solution: Clean up Docker
docker system prune -a --volumes
```

### Backend Issues

#### Problem: "Not key" error
**Cause**: Missing `GROQ_API_KEY` in `.env`
**Solution**:
```bash
cp .env.example .env
# Add your API key to .env
```

#### Problem: ChromaDB initialization error
**Cause**: Corrupted vector database
**Solution**:
```bash
# Remove ChromaDB directory
rm -rf chroma_db/
# Restart backend to rebuild index
```

#### Problem: "No documents found"
**Cause**: Empty `data/` directory
**Solution**: Ensure `.docx` files exist in `data/`

### Frontend Issues

#### Problem: "Network Error" in browser
**Cause**: Backend not running or CORS issue
**Solution**:
```bash
# Check backend is running
curl http://localhost:8000/docs

# Check CORS settings in main.py
```

#### Problem: Build fails with TypeScript errors
**Solution**:
```bash
cd frontend
rm -rf node_modules package-lock.json
npm install
npm run build
```

### Performance Issues

#### Problem: Slow first response
**Cause**: Embedding model loading on first request
**Solution**: Normal behavior. Subsequent requests will be faster.

#### Problem: High memory usage
**Cause**: Large ML models in memory
**Solution**:
- Reduce Docker memory limits in `docker-compose.yml`
- Use smaller embedding models
- Consider GPU acceleration

---

## 🤝 Đóng góp

Mọi đóng góp đều được hoan nghênh!

### Contribute Flow

1. **Fork** repository
2. **Clone** fork của bạn
3. **Tạo branch** mới: `git checkout -b feature/amazing-feature`
4. **Commit** changes: `git commit -m 'Add amazing feature'`
5. **Push** to branch: `git push origin feature/amazing-feature`
6. **Tạo Pull Request**

### Development Guidelines

- Follow existing code style
- Write clear commit messages
- Add comments cho code phức tạp
- Test thoroughly trước khi submit PR

---

## 📄 License

MIT License

Copyright (c) 2026 vietnamese-legal-rag

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

---

## 👨‍💻 Tác giả

**Dự án đồ án tốt nghiệp**: Hệ thống RAG cho tư vấn luật Việt Nam

### Contact

- 📧 Email: your.email@example.com
- 🔗 GitHub: [@yourusername](https://github.com/yourusername)

---

## 🌟 Acknowledgments

- [LangChain](https://www.langchain.com/) - RAG framework
- [Groq](https://groq.com/) - Ultra-fast LLM inference
- [ChromaDB](https://www.trychroma.com/) - Vector database
- [FastAPI](https://fastapi.tiangolo.com/) - Modern web framework
- [React](https://reactjs.org/) - UI library

---

<div align="center">

### ⭐ Nếu project này hữu ích, hãy cho một star!

Made with ❤️ for Vietnamese Legal Tech

</div>
