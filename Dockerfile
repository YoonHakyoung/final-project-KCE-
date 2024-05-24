# Stage 1: Build React app
FROM node:16 as build

WORKDIR /app
COPY react-app/package.json react-app/yarn.lock ./
RUN yarn install
COPY react-app/ ./
RUN yarn build

# Stage 2: Serve the app using FastAPI and Uvicorn
FROM python:3.8:alpine

WORKDIR /app

COPY fastapi-app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY fastapi-app/ /app
COPY --from=build /app/build /app/static

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
