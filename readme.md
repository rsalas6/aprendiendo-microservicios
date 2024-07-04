# Proyecto: Sistema de Procesamiento de Órdenes para una Tienda en Línea

## Descripción del Proyecto
Este proyecto consiste en construir un sistema de procesamiento de órdenes para una tienda en línea utilizando AWS, Python, Docker, microservicios con sistemas basados en eventos (event-driven), Kafka, SQS, SNS y MQ. El sistema deberá manejar el flujo completo de una orden desde la creación hasta la entrega, incluyendo el envío de notificaciones y la actualización del inventario.

## Componentes del Proyecto

1. **Front-end para el Cliente**
   - Una aplicación web donde los clientes puedan navegar productos, añadirlos al carrito y realizar pedidos.
   - Integrar autenticación de usuarios (registro, inicio de sesión).
   - Interfaz de usuario para seguimiento de órdenes y notificaciones en tiempo real.

2. **Microservicios**
   - **Order Service**: Gestión de órdenes (crear, actualizar, cancelar), almacenamiento de datos de órdenes en una base de datos.
   - **Inventory Service**: Gestión del inventario, actualización del stock en tiempo real basado en eventos de creación/cancelación de órdenes.
   - **Payment Service**: Procesar pagos (integración con servicios de pago como Stripe/PayPal), manejo de reembolsos.
   - **Notification Service**: Enviar notificaciones al cliente (correo electrónico, SMS, notificaciones push).
   - **Shipping Service**: Gestión del envío de productos, integración con proveedores de envío.
   - **User Service**: Gestión de usuarios, autenticación y autorización.
   - **Product Service**: Gestión de productos, catálogo de productos, actualización de precios e imágenes.

3. **Sistema de Mensajería y Procesamiento de Eventos**
   - **Apache Kafka**: Para la transmisión de eventos en tiempo real entre microservicios, asegurar la integridad y orden de los eventos.
   - **AWS SQS (Simple Queue Service)**: Para la gestión de colas y el almacenamiento de mensajes entre microservicios, manejo de fallos y reintentos.
   - **AWS SNS (Simple Notification Service)**: Para la gestión de notificaciones, transmisión de mensajes a múltiples suscriptores.
   - **AWS MQ**: Para la mensajería gestionada y la compatibilidad con protocolos tradicionales como AMQP y MQTT.

4. **Infraestructura en AWS**
   - **AWS ECS/EKS**: Para la orquestación de contenedores Docker, despliegue y gestión de microservicios.
   - **AWS RDS**: Base de datos relacional para almacenar información de órdenes, inventario, usuarios y productos.
   - **AWS DynamoDB**: Base de datos NoSQL para almacenamiento de sesiones de usuario, historial de eventos y datos de alta frecuencia.
   - **AWS Lambda**: Funciones serverless para tareas específicas como procesamiento de pagos, generación de informes y procesamiento de notificaciones.
   - **AWS API Gateway**: Para exponer las APIs de los microservicios de manera segura y escalable.
   - **AWS CloudWatch**: Monitoreo y logging de las aplicaciones y servicios.
   - **AWS IAM**: Gestión de identidades y accesos para la seguridad de los servicios.

## Flujo de Trabajo

1. **Creación de una Orden**
   - El cliente inicia sesión y selecciona productos para el pedido.
   - El `Order Service` recibe la solicitud de creación de la orden, valida la información del usuario y los productos.

2. **Publicación de Eventos**
   - El `Order Service` publica un evento en Kafka indicando que se ha creado una nueva orden.
   - Kafka distribuye este evento a los `Inventory Service`, `Payment Service` y `Shipping Service`.

3. **Actualización del Inventario**
   - El `Inventory Service` recibe el evento y actualiza el stock en la base de datos.
   - Si el inventario es suficiente, confirma la disponibilidad del producto, si no, publica un evento de falta de stock.

4. **Procesamiento del Pago**
   - El `Payment Service` procesa el pago utilizando una función Lambda simulada.
   - Si el pago es exitoso, se publica un evento de "pago realizado" en Kafka.
   - En caso de fallo en el pago, se publica un evento de "pago fallido" y el `Order Service` actualiza el estado de la orden.

5. **Notificaciones**
   - El `Notification Service` suscrito al evento de "pago realizado" envía una confirmación al cliente a través de SNS (correo electrónico/SMS).
   - Si se detecta un evento de "pago fallido", el `Notification Service` notifica al cliente para que intente nuevamente.

6. **Gestión del Envío**
   - El `Shipping Service` suscrito al evento de "pago realizado" organiza el envío del producto.
   - Publica un evento en Kafka una vez que el envío ha sido realizado.
   - Si hay un problema con el envío, publica un evento de "problema de envío".

7. **Actualización del Estado de la Orden**
   - El `Order Service` escucha los eventos de "pago realizado", "envío realizado", "pago fallido" y "problema de envío", y actualiza el estado de la orden en la base de datos.

8. **Historial y Seguimiento**
   - El `User Service` actualiza el historial de órdenes del usuario.
   - El `Order Service` actualiza el historial de eventos de la orden en DynamoDB para seguimiento en tiempo real.

## Guía Paso a Paso

### 1. Configurar el entorno
   - Configura un entorno en AWS (ECS/EKS, RDS, DynamoDB, SQS, SNS, MQ).
   - Prepara tu entorno local con Docker, Python y Kafka.

### 2. Desarrollar los Microservicios
   - Define las interfaces de los microservicios (API endpoints, eventos).
   - Implementa la lógica de negocio para cada microservicio.
   - Dockeriza cada microservicio y sube las imágenes a AWS ECR.

### 3. Implementar la Mensajería
   - Configura Kafka para la transmisión de eventos.
   - Implementa la lógica para publicar y consumir eventos en cada microservicio.
   - Configura SQS y SNS para colas de mensajes y notificaciones adicionales.

### 4. Desplegar en AWS
   - Utiliza ECS o EKS para desplegar tus microservicios.
   - Configura RDS para bases de datos relacionales y DynamoDB para almacenamiento NoSQL.
   - Implementa Lambda para tareas específicas y API Gateway para exponer APIs.

### 5. Integración y Pruebas
   - Realiza pruebas integrales para asegurar que todos los componentes se comunican correctamente.
   - Realiza pruebas de carga para verificar el rendimiento y la escalabilidad.
   - Implementa monitoreo y logging con CloudWatch para supervisar la salud del sistema.

## Recursos y Herramientas

- **AWS CLI**: Para gestionar servicios de AWS desde la línea de comandos.
- **Docker**: Para contenerizar aplicaciones.
- **Apache Kafka**: Para la mensajería en tiempo real.
- **Flask/FastAPI**: Frameworks para desarrollar microservicios en Python.
- **Terraform**: Opcionalmente, para gestionar la infraestructura como código.