# We start from a base Python image
FROM python
# We add the files from our current directory to a directory named "app" in the container
ADD . /app
# We set the working directory to /app
WORKDIR /app
# We install the Python packages listed in requirements.txt using pip
RUN pip install -r requirements.txt