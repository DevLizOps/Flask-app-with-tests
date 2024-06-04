# Flask-app-with-tests

Esta es una aplicación desarrollada en código Python usando el framework Flask. 

### ¿En qué consiste la aplicación?

Se trata de un formulario de contacto, con dos test unitarios de ejemplo utilizando Unittest como herramienta de testeo.

### **REQUISITOS TÉCNICOS**

Necesitará un servidor web remoto en el que desplegar la aplicación que permita el tráfico por el **puerto 5000**.

> Note que los comandos que se proporcionan están pensados para una distribución CentOS. En caso de estar usando alguna distribución basada en Debian, cambie 'yum' por 'apt-get'.

Siga los siguientes pasos para para poder desplegar la aplicación:

### **PASO 1:**

Abra una terminal y clone este repositorio en su servidor con el siguiente comando:

    git clone https://github.com/LizzyMaken/Flask-app-with-tests.git

Muévase al directorio de la aplicación:

    cd Flask-app-with-tests
  
### **PASO 2:**

Instale, si no lo tiene ya, python.

    sudo yum install -y python3-pip

Si lo desea, puede comprobar la versión que tiene instalada.

    python3 --version

### **PASO 3:**

Instale el framework Flask:

    pip3 install Flask

### **PASO 4:**

Pruebe la aplicación.

Primero despliegue la aplicación:

    python3 app.py

Luego abra el navegador y entre a su servidor por el puerto 5000. Por ejemplo: http://174.129.76.51:5000

### **PASO 5:**

Ejecute las pruebas unitarias con:

    python3 test_app.py

El resultado de las pruebas se imprimirá por pantalla.
