FROM python:3.9
ENV PYTHONUNBUFFERED=1

# Needed for django translation generation
RUN apt update
RUN apt install gettext -y



# Fixes django dev server failing on postgresql not ready
COPY ./scripts/wait-for /tmp
RUN mv tmp/wait-for /bin/wait-for
RUN chmod +x /bin/wait-for


# Real Service Contents
WORKDIR /apiservice

COPY ./xrate_provider .
COPY ./requirements.txt .

RUN pip install -r requirements.txt
