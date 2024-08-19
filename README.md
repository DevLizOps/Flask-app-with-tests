# Flask-app-with-tests

Esta es una aplicación desarrollada en código Python usando el framework Flask. 

### ¿En qué consiste la aplicación?

Se trata de un formulario de contacto, con dos test unitarios de ejemplo utilizando Unittest como herramienta de testeo.

### **REQUISITOS TÉCNICOS**

Necesitará un servidor web remoto en el que desplegar la aplicación que permita el tráfico por el **puerto 5000**.

> Note que los comandos que se proporcionan están pensados para una distribución CentOS. En caso de estar usando alguna distribución basada en Debian, cambie 'yum' por 'apt-get'.

Siga los siguientes pasos para para poder desplegar la aplicación:

### **PASO 1: clone el repositorio**

Abra una terminal y clone este repositorio en su servidor con el siguiente comando:

    git clone https://github.com/DevLizOps/Flask-app-with-tests.git

Muévase al directorio de la aplicación:

    cd Flask-app-with-tests
  
### **PASO 2: instale la versión más reciente de Python**

    sudo yum install -y python3-pip

Si lo desea, puede comprobar la versión que tiene instalada.

    python3 --version

### **PASO 3: instale Flask**

    pip3 install Flask

### **PASO 4: pruebe la aplicación**

Primero despliegue la aplicación:

    python3 app.py

Luego abra el navegador y entre a su servidor por el puerto 5000. Por ejemplo: http://174.129.76.51:5000

Pruebe el formulario y vea la respuesta del servidor.

### **PASO 5: ejecute los tests**

Si tiene su aplicación aún desplegada, puede salir del proceso tecleando `crlt + C`. Para ejecutar las pruebas unitarias, escriba el comando:

    python3 test_app.py

Este comando hará que se ejecute el archivo de pruebas. El resultado de las mismas se imprimirá por pantalla.
