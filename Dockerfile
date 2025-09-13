FROM python:3.13-slim-trixie
COPY --from=ghcr.io/astral-sh/uv:0.8.13 /uv /uvx /bin/

# Use exact Python base image digest
# FROM python:3.13-slim-trixie@sha256:27f90d79cc85e9b7b2560063ef44fa0e9eaae7a7c3f5a9f74563065c5477cc24
# Copy pinned uv binary from specific digest
# COPY --from=ghcr.io/astral-sh/uv:0.8.11@sha256:8101ad825250a114e7bef89eefaa73c31e34e10ffbe5aff01562740bac97553c /uv /uvx /bin/


WORKDIR /app

COPY pyproject.toml /app/pyproject.toml
COPY uv.lock /app/uv.lock

RUN uv sync --locked

# Make sure the project venv is the default
ENV PATH="/app/.venv/bin:$PATH"

# copy app file
COPY api_docker_s3.py /app/api_docker_s3.py

# expose port
EXPOSE 8080

CMD ["uvicorn", "api_docker_s3:api", "--host", "0.0.0.0", "--port", "8080"]


# docker build -t penguin_model .
# docker run --rm -d -p 8080:8080 --name penguin_model --env-file .env penguin_model

