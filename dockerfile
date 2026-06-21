FROM python:3.14

WORKDIR /app_mi_stats_spotify

COPY . .

ENV VIRTUAL_ENV=/app_mi_stats_spotify/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN python -m venv $VIRTUAL_ENV

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

CMD reflex run --env prod --backend-only