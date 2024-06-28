# **Curso: Microservicios con AWS, Docker y Python**

## **Descripción del curso**
Este curso intensivo de seis semanas está diseñado para estudiantes de nivel intermedio interesados en desarrollar habilidades en la creación y gestión de microservicios utilizando Python, Docker y AWS. Cada semana se compone de cinco días de teoría y práctica, seguidos de dos días dedicados a un proyecto integrador. Los estudiantes aprenderán a utilizar frameworks como Flask y FastAPI, gestionarán aplicaciones multicontenedor con Docker Compose, y desplegarán aplicaciones en AWS utilizando diversas herramientas y servicios. El curso también cubre conceptos de CI/CD, monitoreo, logging, escalabilidad, y seguridad.

## **Semana 1: Introducción a Microservicios y Docker**

### **[Día 1: Microservicio con Python y Flask](/semana-1/dia-1/readme.md) - ✅ Completado**
- **[Teoría](/semana-1/dia-1/teoria.md)**: Introducción a microservicios y Flask.
- **[Práctica](/semana-1/dia-1/practica/)**: Crear un microservicio sencillo con Python y Flask y dockerizarlo.
  - Crear una aplicación básica con Flask.
  - Escribir un Dockerfile para la aplicación.
  - Construir y ejecutar la imagen Docker.

### **[Día 2: Microservicio con Python y FastAPI](#)**
- **[Teoría](#)**: Introducción a FastAPI.
- **[Práctica](#)**: Crear un microservicio sencillo con Python y FastAPI y dockerizarlo.
  - Crear una aplicación básica con FastAPI.
  - Escribir un Dockerfile para la aplicación.
  - Construir y ejecutar la imagen Docker.

### **[Día 3: Docker Compose para Microservicios](#)**
- **[Teoría](#)**: Introducción a Docker Compose.
- **[Práctica](#)**: Conectar microservicios con Docker Compose.
  - Crear un archivo docker-compose.yml.
  - Definir servicios para Flask y FastAPI.
  - Ejecutar y verificar la comunicación entre servicios.

### **[Día 4: Testing de Microservicios](#)**
- **[Teoría](#)**: Conceptos básicos de testing.
- **[Práctica](#)**: Escribir tests para los microservicios.
  - Crear tests unitarios y de integración.
  - Ejecutar tests con pytest.
  - Analizar resultados y realizar mejoras.

### **[Día 5: Monitoreo Básico con Docker](#)**
- **[Teoría](#)**: Introducción a técnicas básicas de monitoreo.
- **[Práctica](#)**: Implementar monitoreo básico en contenedores Docker.
  - Configurar logs en contenedores.
  - Utilizar herramientas básicas de monitoreo.
  - Analizar logs y métricas.

### **[Día 6 y 7: Proyecto Integrador - Semana 1](#)**
- **[Práctica](#)**: Desarrollar un proyecto integrador que conecte los microservicios de Flask y FastAPI.
  - Integrar microservicios en un flujo de trabajo.
  - Implementar mejoras basadas en testing.
  - Documentar el proyecto.

## **Semana 2: Introducción a AWS y Despliegue Básico**

### **[Día 1: Conceptos Básicos de AWS](#)**
- **[Teoría](#)**: Introducción a AWS (EC2, S3, RDS, IAM).
- **[Práctica](#)**: Crear y configurar una instancia EC2.
  - Lanzar una instancia EC2.
  - Configurar seguridad y acceso.
  - Desplegar una aplicación en EC2.

### **[Día 2: Despliegue de Microservicios en AWS](#)**
- **[Teoría](#)**: Despliegue básico de aplicaciones en AWS.
- **[Práctica](#)**: Desplegar microservicios usando EC2.
  - Configurar Docker en EC2.
  - Ejecutar contenedores Docker.
  - Verificar despliegue y conectividad.

### **[Día 3: AWS S3 y RDS](#)**
- **[Teoría](#)**: Uso de S3 y RDS en microservicios.
- **[Práctica](#)**: Integrar S3 y RDS con microservicios.
  - Configurar un bucket S3.
  - Conectar microservicios a RDS.
  - Almacenar y recuperar datos de S3 y RDS.

### **[Día 4: Seguridad en AWS](#)**
- **[Teoría](#)**: Prácticas de seguridad y gestión de IAM.
- **[Práctica](#)**: Configurar roles y políticas IAM.
  - Crear y asignar roles.
  - Configurar políticas de acceso.
  - Implementar prácticas de seguridad.

### **[Día 5: Monitoreo Básico con CloudWatch](#)**
- **[Teoría](#)**: Introducción a AWS CloudWatch.
- **[Práctica](#)**: Configurar monitoreo básico con CloudWatch.
  - Configurar métricas y logs.
  - Crear alertas básicas.
  - Analizar datos de monitoreo.

### **[Día 6 y 7: Proyecto Integrador - Semana 2](#)**
- **[Práctica](#)**: Desarrollar un proyecto integrador utilizando EC2, S3 y RDS.
  - Desplegar microservicios en EC2.
  - Integrar S3 y RDS en el proyecto.
  - Documentar y presentar el proyecto.

## **Semana 3: Servicios Específicos para Microservicios en AWS**

### **[Día 1: Introducción a AWS ECS/EKS](#)**
- **[Teoría](#)**: Conceptos de ECS y EKS.
- **[Práctica](#)**: Configurar un clúster ECS.
  - Crear y configurar un clúster ECS.
  - Definir tareas y servicios.
  - Desplegar microservicios en ECS.

### **[Día 2: AWS Lambda y API Gateway](#)**
- **[Teoría](#)**: Introducción a AWS Lambda y API Gateway.
- **[Práctica](#)**: Crear una función Lambda y exponerla con API Gateway.
  - Escribir una función Lambda en Python.
  - Configurar un endpoint en API Gateway.
  - Probar la integración.

### **[Día 3: Despliegue Avanzado](#)**
- **[Teoría](#)**: Despliegues avanzados (blue-green, canary releases).
- **[Práctica](#)**: Implementar un despliegue blue-green.
  - Configurar un entorno blue-green en ECS.
  - Realizar un despliegue sin tiempo de inactividad.
  - Validar el despliegue.

### **[Día 4: Monitoreo y Logging](#)**
- **[Teoría](#)**: Uso de AWS CloudWatch, Prometheus y Grafana.
- **[Práctica](#)**: Configurar monitoreo y logging.
  - Configurar CloudWatch para microservicios.
  - Integrar Prometheus y Grafana.
  - Visualizar métricas y logs.

### **[Día 5: Tracing y Profiling](#)**
- **[Teoría](#)**: Introducción a AWS X-Ray.
- **[Práctica](#)**: Implementar tracing y profiling.
  - Configurar AWS X-Ray.
  - Integrar X-Ray con microservicios.
  - Analizar trazas y perfiles.

### **[Día 6 y 7: Proyecto Integrador - Semana 3](#)**
- **[Práctica](#)**: Desarrollar un proyecto integrador utilizando ECS/EKS, Lambda y API Gateway.
  - Implementar despliegues avanzados.
  - Configurar monitoreo y logging.
  - Documentar y presentar el proyecto.

## **Semana 4: CI/CD y Despliegue Continuo**

### **[Día 1: Introducción a CI/CD](#)**
- **[Teoría](#)**: Conceptos de CI/CD.
- **[Práctica](#)**: Configurar un pipeline de CI/CD básico.
  - Configurar GitHub Actions.
  - Definir workflows.
  - Ejecutar y validar el pipeline.

### **[Día 2: Despliegue Continuo con AWS CodePipeline](#)**
- **[Teoría](#)**: Introducción a AWS CodePipeline.
- **[Práctica](#)**: Crear un pipeline con AWS CodePipeline.
  - Configurar fuentes y etapas.
  - Implementar despliegues automáticos.
  - Probar y validar el pipeline.

### **[Día 3: Integración con Docker Hub](#)**
- **[Teoría](#)**: Uso de Docker Hub para CI/CD.
- **[Práctica](#)**: Automatizar despliegues de imágenes Docker.
  - Configurar Docker Hub.
  - Integrar Docker Hub con CI/CD.
  - Desplegar automáticamente imágenes Docker.

### **[Día 4: Pruebas Automatizadas en CI/CD](#)**
- **[Teoría](#)**: Implementación de pruebas en CI/CD.
- **[Práctica](#)**: Configurar pruebas automatizadas.
  - Escribir

 tests para el pipeline.
  - Ejecutar pruebas en cada despliegue.
  - Analizar resultados y ajustar el pipeline.

### **[Día 5: Monitoreo de Pipelines CI/CD](#)**
- **[Teoría](#)**: Monitoreo y optimización de pipelines.
- **[Práctica](#)**: Implementar monitoreo en pipelines CI/CD.
  - Configurar alertas y métricas.
  - Analizar performance de pipelines.
  - Optimizar el pipeline basado en datos de monitoreo.

### **[Día 6 y 7: Proyecto Integrador - Semana 4](#)**
- **[Práctica](#)**: Desarrollar un proyecto integrador utilizando CI/CD.
  - Configurar un pipeline completo.
  - Implementar pruebas y despliegues automáticos.
  - Documentar y presentar el proyecto.

## **Semana 5: Escalabilidad y Alta Disponibilidad**

### **[Día 1: Introducción a ELB/ALB](#)**
- **[Teoría](#)**: Conceptos de balanceo de carga (ELB/ALB).
- **[Práctica](#)**: Configurar un Application Load Balancer.
  - Crear y configurar un ALB.
  - Integrar ALB con microservicios.
  - Probar el balanceo de carga.

### **[Día 2: Autoescalado de Servicios](#)**
- **[Teoría](#)**: Conceptos de autoescalado.
- **[Práctica](#)**: Configurar autoescalado en ECS.
  - Definir políticas de autoescalado.
  - Configurar métricas de escalado.
  - Probar y validar el autoescalado.

### **[Día 3: Despliegues de Alta Disponibilidad](#)**
- **[Teoría](#)**: Implementación de alta disponibilidad.
- **[Práctica](#)**: Configurar servicios de alta disponibilidad.
  - Implementar redundancia en ECS.
  - Configurar recuperación ante fallos.
  - Validar la alta disponibilidad.

### **[Día 4: Monitoreo de Escalabilidad](#)**
- **[Teoría](#)**: Monitoreo de escalabilidad con CloudWatch.
- **[Práctica](#)**: Configurar métricas de escalabilidad.
  - Definir métricas clave.
  - Configurar alarmas y notificaciones.
  - Monitorear y ajustar el escalado.

### **[Día 5: Optimización de Costos en AWS](#)**
- **[Teoría](#)**: Estrategias de optimización de costos.
- **[Práctica](#)**: Implementar optimización de costos.
  - Analizar uso de recursos.
  - Implementar estrategias de ahorro.
  - Monitorear y ajustar costos.

### **[Día 6 y 7: Proyecto Integrador - Semana 5](#)**
- **[Práctica](#)**: Desarrollar un proyecto integrador con alta disponibilidad y escalabilidad.
  - Implementar balanceo de carga y autoescalado.
  - Configurar monitoreo de escalabilidad.
  - Documentar y presentar el proyecto.

## **Semana 6: Seguridad y Mejores Prácticas**

### **[Día 1: Prácticas de Seguridad](#)**
- **[Teoría](#)**: Introducción a prácticas de seguridad.
- **[Práctica](#)**: Implementar prácticas de seguridad en microservicios.
  - Configurar HTTPS.
  - Gestionar secretos con AWS Secrets Manager.
  - Realizar auditorías de seguridad.

### **[Día 2: Gestión de Secretos y Configuraciones](#)**
- **[Teoría](#)**: Gestión de secretos y configuraciones.
- **[Práctica](#)**: Implementar AWS Secrets Manager y Parameter Store.
  - Configurar secretos y parámetros.
  - Integrar con microservicios.
  - Probar la gestión de secretos.

### **[Día 3: Seguridad en el Despliegue](#)**
- **[Teoría](#)**: Prácticas de seguridad en CI/CD.
- **[Práctica](#)**: Implementar seguridad en pipelines CI/CD.
  - Configurar autenticación y autorización.
  - Implementar escaneo de vulnerabilidades.
  - Probar la seguridad del pipeline.

### **[Día 4: Monitoreo y Auditoría de Seguridad](#)**
- **[Teoría](#)**: Monitoreo y auditoría de seguridad.
- **[Práctica](#)**: Implementar monitoreo de seguridad.
  - Configurar CloudTrail y CloudWatch.
  - Auditar acciones y accesos.
  - Probar la auditoría de seguridad.

### **[Día 5: Estrategias de Recuperación ante Desastres](#)**
- **[Teoría](#)**: Planificación de recuperación ante desastres.
- **[Práctica](#)**: Implementar estrategias de recuperación.
  - Configurar backups y restauraciones.
  - Implementar planes de recuperación.
  - Probar la recuperación ante desastres.

### **[Día 6 y 7: Proyecto Integrador - Semana 6](#)**
- **[Práctica](#)**: Desarrollar un proyecto integrador con foco en seguridad.
  - Implementar prácticas de seguridad y gestión de secretos.
  - Configurar monitoreo y auditoría de seguridad.
  - Documentar y presentar el proyecto.