# Laboratorio 2: Aplicación Servidor y protocolo HFTP

## Redes y Sistemas Distribuidos 2021

### Integrantes del grupo:

- Facundo Buc
- Agustin Silva Fiorentino
- Alejandro Claudio Spitale

### Estructuración y tomas de decisiones del servidor

El servidor esta compuesto por dos clases llamadas "Server" y "Connection", en la primera clase esta implementada todo lo referido a la conexión, aceptación y manipulación del cliente ingresante al socket, donde los pedidos son esperados 1 por 1 hasta completar todos los pedidos. En la segunda clase tenemos implementada todo lo referido a la manipulación de comandos y posibles errores de los mismos, recorriendo una queue de comandos por cada cliente hasta satisfacer dicho cliente.

### Dificultades encontradas en el proceso

Tuvimos muchas dificultades en un principio en entender la estructura general del servidor y que tenían que hacer cada función, pudimos solventarlo viendo las preguntas que los compañeros realizaron en zulip y a prueba y error, también viendo el archivo cliente y server-test, para darnos una idea de como el servidor y el cliente se comunican.

### Información sobre la realización del laboratorio

Nosotros optamos por usar la herramienta "live share" del IDE Visual Studio Code, y también discord como canal de comunicación de voz, así conseguimos realizar todo el laboratorio, es decír, debartimos todo el tiempo las decisiones a tomar entre los 3 integrantes y debatiendo diferentes ideas para la implementación del mismo. Los push fueron realizados por Facundo porque él fue quien hosteo dicha herramienta.