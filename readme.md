# **Curso: microservicios con AWS, Docker y Python**

## **Descripción del Curso**
Este curso intensivo de seis semanas está diseñado para estudiantes de nivel intermedio que desean aprender a desarrollar y gestionar microservicios utilizando Python, Docker y AWS. El curso combina teoría y práctica diaria, con proyectos semanales y un proyecto final para aplicar todos los conocimientos adquiridos.

## **Semana 1: Introducción a Microservicios y Docker**

### **[Día 1: Crear un Microservicio Sencillo con Flask](/semana-1/dia-1/readme.md)**
- **[Teoría](/semana-1/dia-1/teoria.md)**: Introducción a los microservicios y Flask.
- **[Práctica](/semana-1/dia-1/practica/)**: Crear un microservicio sencillo con Python y Flask y dockerizarlo.
  - Crear un entorno virtual.
  - Instalar Flask.
  - Crear un endpoint simple.
  - Escribir un Dockerfile.
  - Construir y ejecutar la imagen Docker.

### **[Día 2: Crear un Microservicio con FastAPI](/semana-1/dia-2/readme.md)**
- **[Teoría](/semana-1/dia-2/teoria.md)**: Introducción a FastAPI.
- **[Práctica](/semana-1/dia-2/practica/)**: Crear un microservicio con Python y FastAPI y dockerizarlo.
  - Crear un entorno virtual.
  - Instalar FastAPI y Uvicorn.
  - Crear un endpoint simple.
  - Escribir un Dockerfile.
  - Construir y ejecutar la imagen Docker.

### **[Día 3: Conectar Microservicios con Docker Compose](/semana-1/dia-3/readme.md)**
- **[Teoría](/semana-1/dia-3/teoria.md)**: Introducción a Docker Compose.
- **[Práctica](/semana-1/dia-3/practica/)**: Conectar los microservicios creados con Docker Compose.
  - Escribir un archivo docker-compose.yml.
  - Configurar la comunicación entre los servicios.
  - Ejecutar los servicios con Docker Compose.

### **[Día 4: Testing de Microservicios](#)**
- **[Teoría](#)**: Conceptos básicos de testing en microservicios.
- **[Práctica](#)**: Escribir pruebas unitarias y de integración para los microservicios.
  - Configurar pytest.
  - Escribir pruebas unitarias.
  - Escribir pruebas de integración.
  - Ejecutar las pruebas.

### **[Día 5: Práctica Integradora](#)**
- **[Teoría](#)**: Revisión de conceptos clave.
- **[Práctica](#)**: Mejorar los microservicios con técnicas avanzadas de Docker.
  - Optimización de Dockerfiles.
  - Configuración de variables de entorno.
  - Gestión de secretos con Docker.

### **[Día 6-7: Proyecto Semanal](#)**
- **[Teoría](#)**: No aplica.
- **[Práctica](#)**: Consolidar los microservicios en un proyecto completo.
  - Desplegar los microservicios en un entorno local.
  - Realizar pruebas de comunicación y rendimiento.
  - Documentar el proceso y los resultados.

## **Semana 2: Introducción a AWS y Despliegue de Microservicios**

### **[Día 1: Conceptos Básicos de AWS](#)**
- **[Teoría](#)**: Introducción a AWS y sus servicios principales.
- **[Práctica](#)**: Configurar una cuenta de AWS y explorar la consola.
  - Crear una cuenta de AWS.
  - Configurar IAM para acceso seguro.
  - Explorar servicios como EC2, S3 y RDS.

### **[Día 2: Despliegue en EC2](#)**
- **[Teoría](#)**: Introducción a EC2 y despliegue de aplicaciones.
- **[Práctica](#)**: Desplegar un microservicio en una instancia EC2.
  - Crear una instancia EC2.
  - Configurar la instancia con Docker.
  - Desplegar un microservicio en EC2.

### **[Día 3: Despliegue en ECS/EKS](#)**
- **[Teoría](#)**: Introducción a ECS y EKS.
- **[Práctica](#)**: Desplegar microservicios en ECS.
  - Crear un cluster ECS.
  - Definir tareas y servicios.
  - Desplegar microservicios en ECS.

### **[Día 4: Lambda y API Gateway](#)**
- **[Teoría](#)**: Introducción a AWS Lambda y API Gateway.
- **[Práctica](#)**: Crear funciones Lambda y exponerlas con API Gateway.
  - Crear una función Lambda.
  - Configurar API Gateway.
  - Integrar Lambda con API Gateway.

### **[Día 5: Práctica Integradora](#)**
- **[Teoría](#)**: Revisión de conceptos clave.
- **[Práctica](#)**: Integrar servicios AWS en un proyecto.
  - Configurar un flujo de trabajo con EC2, ECS y Lambda.
  - Optimizar el despliegue y la comunicación entre servicios.

### **[Día 6-7: Proyecto Semanal](#)**
- **[Teoría](#)**: No aplica.
- **[Práctica](#)**: Desplegar un sistema de microservicios completo en AWS.
  - Crear un entorno de producción en AWS.
  - Desplegar todos los microservicios.
  - Realizar pruebas de carga y rendimiento.

## **Semana 3: CI/CD y Monitoreo**

### **[Día 1: Introducción a CI/CD](#)**
- **[Teoría](#)**: Conceptos básicos de CI/CD.
- **[Práctica](#)**: Configurar un pipeline básico de CI/CD.
  - Crear un repositorio en GitHub/GitLab.
  - Configurar una acción de CI para pruebas automáticas.
  - Configurar una acción de CD para despliegue automático.

### **[Día 2: Jenkins para CI/CD](#)**
- **[Teoría](#)**: Introducción a Jenkins.
- **[Práctica](#)**: Configurar Jenkins para un proyecto de microservicios.
  - Instalar y configurar Jenkins.
  - Crear un pipeline Jenkins para pruebas y despliegue.
  - Integrar Jenkins con AWS.

### **[Día 3: Monitoreo con AWS CloudWatch](#)**
- **[Teoría](#)**: Introducción a AWS CloudWatch.
- **[Práctica](#)**: Configurar monitoreo básico con CloudWatch.
  - Crear alarmas y dashboards.
  - Configurar logs y métricas para microservicios.
  - Integrar CloudWatch con los microservicios.

### **[Día 4: Prometheus y Grafana](#)**
- **[Teoría](#)**: Introducción a Prometheus y Grafana.
- **[Práctica](#)**: Configurar monitoreo avanzado con Prometheus y Grafana.
  - Instalar y configurar Prometheus.
  - Crear dashboards en Grafana.
  - Integrar Prometheus con microservicios.

### **[Día 5: Práctica Integradora](#)**
- **[Teoría](#)**: Revisión de conceptos clave.
- **[Práctica](#)**: Crear un sistema completo de CI/CD y monitoreo.
  - Integrar Jenkins con Prometheus y Grafana.
  - Configurar alertas y monitoreo para todo el sistema.

### **[Día 6-7: Proyecto Semanal](#)**
- **[Teoría](#)**: No aplica.
- **[Práctica](#)**: Implementar un flujo completo de CI/CD y monitoreo para un sistema de microservicios.
  - Configurar y desplegar el pipeline de CI/CD.
  - Configurar y desplegar el sistema de monitoreo.
  - Documentar y probar todo el sistema.

## **Semana 4: Seguridad y Gestión de Configuraciones**

### **[Día 1: Prácticas de Seguridad](#)**
- **[Teoría](#)**: Conceptos básicos de seguridad en microservicios.
- **[Práctica](#)**: Implementar prácticas de seguridad en microservicios.
  - Configurar políticas de IAM.
  - Usar roles y permisos adecuados.
  - Implementar HTTPS.

### **[Día 2: Gestión de Secretos](#)**
- **[Teoría](#)**: Introducción a la gestión de secretos.
- **[Práctica](#)**: Implementar gestión de secretos con AWS Secrets Manager.
  - Configurar AWS Secrets Manager.
  - Integrar la gestión de secretos en microservicios.
  - Probar la recuperación segura de secretos.

### **[Día 3: Configuración de Servicios](#)**
- **[Teoría](#)**: Introducción a la configuración de servicios.
- **[Práctica](#)**: Configurar servicios con AWS Systems Manager Parameter Store.
  - Configurar Parameter Store.
  - Integrar Parameter Store en microservicios.
  - Probar la recuperación de configuraciones.

### **[Día 4: Despliegues Seguros](#)**
- **[Teoría](#)**: Despliegues seguros y estrategias de despliegue.
- **[Práctica](#)**: Implementar despliegues seguros (blue-green, canary releases).
  - Configurar blue-green deployments.
  - Configurar canary releases.
  - Probar despliegues seguros en microserv

icios.

### **[Día 5: Práctica Integradora](#)**
- **[Teoría](#)**: Revisión de conceptos clave.
- **[Práctica](#)**: Mejorar la seguridad y gestión de configuraciones en microservicios.
  - Implementar todas las prácticas de seguridad.
  - Integrar la gestión de secretos y configuraciones.

### **[Día 6-7: Proyecto Semanal](#)**
- **[Teoría](#)**: No aplica.
- **[Práctica](#)**: Desplegar un sistema de microservicios seguro y bien configurado.
  - Revisar y mejorar la seguridad del sistema.
  - Documentar y probar todas las configuraciones y prácticas de seguridad.

## **Semana 5: Escalabilidad, Alta Disponibilidad y Mensajería**

### **[Día 1: Introducción a la Escalabilidad](#)**
- **[Teoría](#)**: Conceptos básicos de escalabilidad.
- **[Práctica](#)**: Implementar escalabilidad básica en microservicios.
  - Configurar autoescalado en EC2.
  - Probar la escalabilidad automática.

### **[Día 2: Load Balancers (ELB/ALB)](#)**
- **[Teoría](#)**: Introducción a ELB y ALB.
- **[Práctica](#)**: Configurar ELB/ALB para microservicios.
  - Configurar un load balancer.
  - Integrar el load balancer con microservicios.
  - Probar la distribución de carga.

### **[Día 3: Alta Disponibilidad](#)**
- **[Teoría](#)**: Conceptos de alta disponibilidad.
- **[Práctica](#)**: Implementar alta disponibilidad en microservicios.
  - Configurar replicación en RDS.
  - Configurar failover automático.
  - Probar la alta disponibilidad.

### **[Día 4: Mensajería con Kafka y SQS](#)**
- **[Teoría](#)**: Introducción a Kafka y Amazon SQS.
- **[Práctica](#)**: Implementar mensajería en microservicios.
  - Configurar Kafka.
  - Configurar SQS.
  - Integrar Kafka y SQS en microservicios.
  - Probar la mensajería entre microservicios.

### **[Día 5: SNS y MQ](#)**
- **[Teoría](#)**: Introducción a Amazon SNS y MQ.
- **[Práctica](#)**: Implementar notificaciones y colas de mensajes.
  - Configurar SNS.
  - Configurar MQ.
  - Integrar SNS y MQ en microservicios.
  - Probar las notificaciones y colas de mensajes.

### **[Día 6-7: Proyecto Semanal](#)**
- **[Teoría](#)**: No aplica.
- **[Práctica](#)**: Desplegar un sistema de microservicios escalable, altamente disponible y con mensajería.
  - Implementar todas las estrategias de escalabilidad y alta disponibilidad.
  - Integrar mensajería con Kafka, SQS, SNS y MQ.
  - Documentar y probar el sistema completo.

## **Semana 6: Tracing y Despliegues Avanzados**

### **[Día 1: Introducción a Tracing y Profiling](#)**
- **[Teoría](#)**: Conceptos básicos de tracing y profiling.
- **[Práctica](#)**: Implementar tracing básico con AWS X-Ray.
  - Configurar AWS X-Ray.
  - Integrar X-Ray con microservicios.
  - Probar tracing y profiling.

### **[Día 2: Tracing Avanzado](#)**
- **[Teoría](#)**: Estrategias avanzadas de tracing.
- **[Práctica](#)**: Implementar tracing avanzado en microservicios.
  - Configurar tracing para múltiples servicios.
  - Analizar trazas y optimizar el rendimiento.
  - Probar tracing avanzado.

### **[Día 3: Despliegues Blue-Green](#)**
- **[Teoría](#)**: Estrategias de despliegue blue-green.
- **[Práctica](#)**: Implementar blue-green deployments en microservicios.
  - Configurar blue-green deployments en ECS.
  - Probar despliegues blue-green.

### **[Día 4: Despliegues Canary](#)**
- **[Teoría](#)**: Estrategias de despliegue canary.
- **[Práctica](#)**: Implementar canary releases en microservicios.
  - Configurar canary releases en ECS.
  - Probar despliegues canary.

### **[Día 5: Práctica Integradora](#)**
- **[Teoría](#)**: Revisión de conceptos clave.
- **[Práctica](#)**: Implementar tracing y despliegues avanzados en microservicios.
  - Configurar tracing completo para el sistema.
  - Implementar y probar despliegues blue-green y canary.

### **[Día 6-7: Proyecto Semanal](#)**
- **[Teoría](#)**: No aplica.
- **[Práctica](#)**: Desplegar un sistema de microservicios con tracing y despliegues avanzados.
  - Revisar y mejorar el tracing del sistema.
  - Documentar y probar todas las estrategias de despliegue avanzado.
